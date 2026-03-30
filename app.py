import docker
from flask import Flask, render_template, jsonify
from flask_sock import Sock
import threading
import argparse
import os
import sys
import time
import logging
from datetime import datetime
from collections import defaultdict

# Try to import psutil for system monitoring (optional)
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    psutil = None
    PSUTIL_AVAILABLE = False
    logging.warning("psutil not installed. System monitoring will be limited.")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('classroom.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Global session tracking
active_sessions = {}
session_counter = 0

# --- Setup ---
app = Flask(__name__)
sock = Sock(app)
# Initialize Docker client from environment variables
try:
    client = docker.from_env()
    docker_available = True
    logger.info("Docker client initialized successfully")
except docker.errors.DockerException:
    print("เกิดข้อผิดพลาด: ไม่สามารถเชื่อมต่อกับ Docker daemon ได้")
    print("กรุณาตรวจสอบว่า Docker กำลังทำงานอยู่หรือไม่")
    print("กำลังทำงานในโหมดจำกัด (หน้าต่างทดสอบเท่านั้น)")
    logger.warning("Docker not available, running in limited mode")
    docker_available = False
    # Create a dummy client to avoid crashes
    class DummyDockerClient:
        def __init__(self):
            self.containers = DummyContainers()
            self.networks = DummyNetworks()
            self.images = DummyImages()
            
        def info(self):
            return {
                'ContainersRunning': 0,
                'ContainersStopped': 0,
                'Images': 0,
                'ServerVersion': 'Docker not available'
            }
    
    class DummyContainers:
        def run(self, *args, **kwargs):
            raise docker.errors.DockerException("Docker not available")
            
    class DummyNetworks:
        def get(self, name):
            raise docker.errors.NotFound("Docker not available")
        def create(self, *args, **kwargs):
            raise docker.errors.APIError("Docker not available")
            
    class DummyImages:
        pass
    
    client = DummyDockerClient()

# Ensure classroom network exists
def ensure_classroom_network():
    """Create classroom-net network if it doesn't exist."""
    if not docker_available:
        logger.warning("Docker not available, skipping network creation")
        return None
    
    network_name = "classroom-net"
    try:
        # Try to get the network
        network = client.networks.get(network_name)
        logger.info(f"Network '{network_name}' already exists")
        return network
    except docker.errors.NotFound:
        logger.info(f"Network '{network_name}' not found, creating...")
        try:
            # Create network with specific subnet
            ipam_pool = docker.types.IPAMPool(subnet='172.20.0.0/16')
            ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
            network = client.networks.create(
                network_name,
                driver="bridge",
                ipam=ipam_config,
                check_duplicate=True
            )
            logger.info(f"Created network '{network_name}' with subnet 172.20.0.0/16")
            return network
        except docker.errors.APIError as e:
            logger.error(f"Failed to create network '{network_name}': {e}")
            # If network creation fails, we'll still try to run containers
            # They'll use default bridge network if classroom-net doesn't exist
            return None
    except Exception as e:
        logger.error(f"Error checking network '{network_name}': {e}")
        return None

# Create network on startup
classroom_network = ensure_classroom_network()


# --- Routes ---
@app.route('/')
def index():
    """Serves the premium HTML page with English lessons (default)."""
    return render_template('index_premium.html')

@app.route('/premium')
def premium():
    """Serves the premium HTML page with English lessons."""
    return render_template('index_premium.html')

@app.route('/premium/thai')
def premium_thai():
    """Serves the premium HTML page with Thai lessons."""
    return render_template('index_premium.html')

@app.route('/improved')
def improved():
    """Serves the improved HTML page with English lessons."""
    return render_template('index_improved.html')

@app.route('/improved/thai')
def improved_thai():
    """Serves the improved HTML page with Thai lessons."""
    return render_template('index_improved.html')

@app.route('/classic')
def classic():
    """Serves the classic HTML page for backward compatibility."""
    return render_template('index.html')

@app.route('/english')
def english():
    """Alias for premium interface with English lessons."""
    return render_template('index_premium.html')

@app.route('/thai')
def thai():
    """Serves the premium HTML page with Thai lessons."""
    return render_template('index_premium.html')

@app.route('/status')
def status():
    """Returns JSON status of the classroom server."""
    try:
        # Get Docker info
        if docker_available:
            docker_info = client.info()
            docker_data = {
                'containers_running': docker_info['ContainersRunning'],
                'containers_stopped': docker_info['ContainersStopped'],
                'images': docker_info['Images'],
                'version': docker_info['ServerVersion'],
                'available': True
            }
        else:
            docker_data = {
                'containers_running': 0,
                'containers_stopped': 0,
                'images': 0,
                'version': 'Docker not available',
                'available': False
            }
        
        # Prepare session data
        sessions_data = []
        for session_id, session_info in active_sessions.items():
            session_duration = datetime.now() - session_info['start_time']
            sessions_data.append({
                'session_id': session_id,
                'container_id': session_info['container_id_short'],
                'container_ip': session_info['container_ip'],
                'client_ip': session_info['client_ip'],
                'start_time': session_info['start_time'].isoformat(),
                'last_activity': session_info['last_activity'].isoformat(),
                'duration_seconds': int(session_duration.total_seconds()),
                'bytes_sent': session_info['bytes_sent'],
                'bytes_received': session_info['bytes_received']
            })
        
        # Get system info (psutil optional)
        system_info = {}
        if PSUTIL_AVAILABLE:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            system_info = {
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'memory_total_gb': round(memory.total / (1024**3), 2),
                'memory_available_gb': round(memory.available / (1024**3), 2)
            }
        else:
            system_info = {
                'cpu_percent': 0.0,
                'memory_percent': 0.0,
                'memory_total_gb': 0.0,
                'memory_available_gb': 0.0,
                'note': 'psutil not installed for system monitoring'
            }
        
        return jsonify({
            'status': 'running',
            'server_time': datetime.now().isoformat(),
            'active_sessions': len(active_sessions),
            'total_sessions': session_counter,
            'sessions': sessions_data,
            'docker': docker_data,
            'system': system_info
        })
    except Exception as e:
        logger.error(f"Error generating status: {e}")
        return jsonify({'error': str(e), 'status': 'error'}), 500

@app.route('/dashboard')
def dashboard():
    """Teacher dashboard page."""
    return render_template('dashboard.html')


@sock.route('/terminal')
def terminal(ws):
    """Handles the WebSocket connection for the terminal."""
    global session_counter
    session_id = session_counter
    session_counter += 1
    
    session_start = datetime.now()
    client_ip = ws.environ.get('REMOTE_ADDR', 'unknown')
    
    logger.info(f"New terminal session #{session_id} from IP: {client_ip}")
    
    # Check if Docker is available
    if not docker_available:
        error_msg = "Docker is not available. Terminal functionality disabled."
        logger.error(error_msg)
        ws.send(f"\r\n\x1b[1;31m{error_msg}\x1b[0m\r\n")
        ws.send("\r\n\x1b[1;33mPlease start Docker daemon and restart the server.\x1b[0m\r\n")
        ws.close()
        return
    
    try:
        # Prepare container configuration
        container_config = {
            "image": "ubuntu-classroom",
            "detach": True,
            "tty": True,
            "stdin_open": True,
            "auto_remove": True,
            # Resource limits to prevent abuse
            "mem_limit": '512m',        # 512 MB memory limit
            "memswap_limit": '1g',      # 1 GB total memory+swap limit
            "cpu_period": 100000,       # CPU quota period (100ms)
            "cpu_quota": 50000,         # 50% of CPU (half of one core)
            # Security options
            "read_only": False         # Allow writing to filesystem
        }
        
        # Add network if classroom network exists
        if classroom_network is not None:
            container_config["network"] = "classroom-net"
            logger.info(f"Using classroom-net network for session #{session_id}")
        else:
            logger.warning(f"classroom-net network not found, using default bridge for session #{session_id}")
        
        # Create container
        container = client.containers.run(**container_config)
        
        container_id_short = container.id[:12]
        logger.info(f"Created container {container_id_short} for session #{session_id}")
        
        # Get container IP address
        container.reload()
        
        # Determine container IP based on network configuration
        if classroom_network is not None and "classroom-net" in container.attrs['NetworkSettings']['Networks']:
            container_ip = container.attrs['NetworkSettings']['Networks']['classroom-net']['IPAddress']
            logger.info(f"Container {container_id_short} IP: {container_ip} (classroom-net)")
        else:
            # Fallback to default bridge network IP
            network_settings = container.attrs['NetworkSettings']
            if 'Networks' in network_settings and 'bridge' in network_settings['Networks']:
                container_ip = network_settings['Networks']['bridge']['IPAddress']
            else:
                # Last resort: get first network IP
                networks = network_settings['Networks']
                if networks:
                    first_network = list(networks.keys())[0]
                    container_ip = networks[first_network]['IPAddress']
                else:
                    container_ip = 'unknown'
            logger.info(f"Container {container_id_short} IP: {container_ip} (bridge/default)")
        
        # Store session information
        active_sessions[session_id] = {
            'container_id': container.id,
            'container_id_short': container_id_short,
            'container_ip': container_ip,
            'client_ip': client_ip,
            'start_time': session_start,
            'last_activity': datetime.now(),
            'bytes_sent': 0,
            'bytes_received': 0
        }
        
        # Send welcome message with useful information
        welcome_msg = f"""
Connected to your personal Linux environment!
Session ID: {session_id}
Container ID: {container_id_short}
Container IP: {container_ip}
You can SSH to other students using: ssh student@[their_container_ip]
Default password: student

Welcome! You have a full Ubuntu 22.04 environment with Python 3 and Rust installed.
Type 'help' for available commands or check the lessons panel.

\r\n\r\n"""
        ws.send(welcome_msg)
        
    except docker.errors.ImageNotFound:
        error_msg = "เกิดข้อผิดพลาด: ไม่พบ Docker image 'ubuntu-classroom'"
        logger.error(error_msg)
        ws.close(message="Server configuration error. Please run 'python install.py' first.")
        return
    except docker.errors.APIError as e:
        error_msg = f"Docker API error: {str(e)}"
        logger.error(error_msg)
        ws.close(message="Server error. Please contact administrator.")
        return
    except Exception as e:
        error_msg = f"Unexpected error creating container: {str(e)}"
        logger.error(error_msg)
        ws.close(message="Internal server error.")
        return

    # Attach to container
    try:
        s = container.attach_socket(params={
            'stdin': 1,
            'stdout': 1,
            'stderr': 1,
            'stream': 1
        })
        container_socket = s._sock
    except Exception as e:
        logger.error(f"Failed to attach to container {container.id[:12]}: {e}")
        ws.close(message="Failed to connect to container.")
        # Clean up container
        try:
            container.stop(timeout=2)
        except:
            pass
        # Remove from active sessions
        if session_id in active_sessions:
            del active_sessions[session_id]
        return

    def forward_container_to_ws():
        """Forward container output to WebSocket."""
        try:
            while True:
                data = container_socket.recv(4096)  # Increased buffer size
                if not data:
                    break
                # Update session activity
                if session_id in active_sessions:
                    active_sessions[session_id]['bytes_received'] += len(data)
                    active_sessions[session_id]['last_activity'] = datetime.now()
                
                ws.send(data.decode('utf-8', errors='ignore'))
        except (ConnectionResetError, BrokenPipeError, OSError):
            # Normal connection closure
            pass
        except Exception as e:
            logger.error(f"Thread error in session #{session_id}: {e}")
        finally:
            # Signal WebSocket closure
            try:
                ws.close()
            except:
                pass

    # Start forwarding thread
    thread = threading.Thread(target=forward_container_to_ws)
    thread.daemon = True
    thread.start()

    # Main loop: forward WebSocket messages to container
    try:
        while True:
            data = ws.receive()
            if data is None:
                break
                
            # Update session activity
            if session_id in active_sessions:
                active_sessions[session_id]['bytes_sent'] += len(data)
                active_sessions[session_id]['last_activity'] = datetime.now()
            
            # Send to container
            try:
                container_socket.sendall(data.encode('utf-8'))
            except BrokenPipeError:
                logger.warning(f"Broken pipe for session #{session_id}, container may have exited")
                break
            except Exception as e:
                logger.error(f"Error sending data to container in session #{session_id}: {e}")
                break
                
    except Exception as e:
        logger.info(f"WebSocket closed for session #{session_id}: {e}")
    finally:
        # Cleanup
        logger.info(f"Cleaning up session #{session_id}, container {container.id[:12]}")
        
        # Close sockets
        try:
            container_socket.close()
        except:
            pass
        
        try:
            s.close()
        except:
            pass
        
        # Stop container
        try:
            container.stop(timeout=5)
            logger.info(f"Container {container.id[:12]} stopped.")
        except docker.errors.NotFound:
            logger.info(f"Container {container.id[:12]} already removed.")
        except Exception as e:
            logger.error(f"Error stopping container {container.id[:12]}: {e}")
        
        # Remove from active sessions
        if session_id in active_sessions:
            session_duration = datetime.now() - active_sessions[session_id]['start_time']
            logger.info(f"Session #{session_id} ended. Duration: {session_duration}")
            del active_sessions[session_id]

# --- Run the App ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Linux Classroom Web App",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--host',
        type=str,
        default='0.0.0.0',
        help='Host to bind to (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to listen on (default: 5000)'
    )
    parser.add_argument(
        '--https',
        action='store_true',
        help='Enable HTTPS mode. Requires --cert and --key.'
    )
    parser.add_argument(
        '--cert',
        type=str,
        default='cert.pem',
        help='Path to SSL certificate file (default: cert.pem)'
    )
    parser.add_argument(
        '--key',
        type=str,
        default='key.pem',
        help='Path to SSL private key file (default: key.pem)'
    )

    args = parser.parse_args()

    ssl_context = None
    if args.https:
        if os.path.exists(args.cert) and os.path.exists(args.key):
            ssl_context = (args.cert, args.key)
            print(f"HTTPS enabled using cert: {args.cert} and key: {args.key}")
        else:
            print("คำเตือน: ต้องการใช้ HTTPS แต่ไม่พบไฟล์ certificate หรือ key")
            print(f"ตรวจสอบที่: {args.cert}, {args.key}")
            print("ไม่สามารถเริ่มระบบในโหมด HTTPS ได้")
            sys.exit(1)

    # Use 'werkzeug' for production, but Flask's default is fine for this use case
    app.run(host=args.host, port=args.port, debug=False, ssl_context=ssl_context)

