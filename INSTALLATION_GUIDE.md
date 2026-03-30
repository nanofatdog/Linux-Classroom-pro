# Installation Guide - Enhanced Linux Classroom

## Quick Installation

### **For New Installation**
```bash
# Clone the repository
git clone https://github.com/nanofatdog/Linux-Classroom-in-a-Browser.git
cd Linux-Classroom-in-a-Browser

# Install Python dependencies
pip install -r requirements.txt

# Build the Docker image
python install.py

# Start the server
python app.py
```

### **For Upgrading Existing Installation**
```bash
# Update the code
cd Linux-Classroom-in-a-Browser
git pull origin main  # or download latest version

# Update Python dependencies
pip install -r requirements.txt

# Rebuild Docker image with new features
python install.py

# Restart server
python app.py
```

## System Requirements

### **Minimum Requirements**
- **OS**: Windows 10/11, Linux (Ubuntu/Debian), or macOS
- **Docker**: Docker Desktop (Windows/macOS) or Docker Engine (Linux)
- **Python**: Python 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended for multiple students)
- **Storage**: 2GB free space

### **Recommended for Classrooms**
- **CPU**: 4+ cores
- **RAM**: 8GB+ 
- **Storage**: 10GB+ free space
- **Network**: Stable internet connection

## Detailed Installation Steps

### **Step 1: Install Docker**

#### **Windows 10/11**
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Follow installer instructions (WSL 2 will be enabled automatically)
3. After installation, start Docker Desktop and wait for it to be "Running"

#### **Linux (Ubuntu/Debian)**
```bash
sudo apt-get update
sudo apt-get install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Logout and login again for group changes to take effect
```

#### **macOS**
1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Install and launch Docker Desktop
3. Ensure Docker is running (whale icon in menu bar)

### **Step 2: Install Python**

#### **Windows**
- **Option 1 (Recommended)**: Install from Microsoft Store (search "Python 3.11")
- **Option 2**: Download from [python.org](https://python.org/downloads/)
  - Check "Add Python to PATH" during installation

#### **Linux**
```bash
sudo apt-get install python3 python3-pip -y
```

#### **macOS**
```bash
# Using Homebrew
brew install python3

# Or download from python.org
```

### **Step 3: Clone and Setup Classroom**

```bash
# Clone repository
git clone https://github.com/nanofatdog/Linux-Classroom-in-a-Browser.git
cd Linux-Classroom-in-a-Browser

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 4: Build Docker Image**

```bash
# Build the classroom Docker image
python install.py
```
This will:
1. Check Docker is running
2. Create classroom network
3. Build Ubuntu image with Python, Rust, and tools
4. Take 5-15 minutes depending on internet speed

### **Step 5: Start the Server**

```bash
# Start on default port (5000)
python app.py

# Start on custom port
python app.py --port 8080

# Start on specific IP address
python app.py --host 0.0.0.0 --port 8080

# Start with HTTPS (requires certificates)
python app.py --https --cert cert.pem --key key.pem
```

## Access Points After Installation

### **Default Access**
- **Student Interface**: `http://localhost:5000/` (or your server IP)
- **Teacher Dashboard**: `http://localhost:5000/dashboard`
- **Thai Lessons**: `http://localhost:5000/thai`
- **Classic Interface**: `http://localhost:5000/classic`
- **Status API**: `http://localhost:5000/status` (JSON)

### **Network Access**
If hosting for a classroom:
```bash
# Bind to all network interfaces
python app.py --host 0.0.0.0 --port 5000
```
Then students can access via: `http://[server-ip]:5000/`

## Configuration Options

### **Server Configuration**
Command line arguments for `app.py`:
- `--host` - Host to bind to (default: 0.0.0.0)
- `--port` - Port to listen on (default: 5000)
- `--https` - Enable HTTPS mode
- `--cert` - SSL certificate file (default: cert.pem)
- `--key` - SSL private key file (default: key.pem)

### **Docker Configuration**
Edit `Dockerfile` to:
- Add more software packages
- Change default password
- Modify resource limits
- Add custom scripts

### **Lessons Customization**
- English lessons: `static/lessons_en.json`
- Thai lessons: `static/lessons.json`
- Add your own lessons by editing these files

## Troubleshooting

### **Common Issues**

#### **1. Docker Not Running**
```
Error: Cannot connect to Docker daemon
```
**Solution:**
- Windows/macOS: Start Docker Desktop
- Linux: `sudo systemctl start docker`
- Check: `docker ps` should show no errors

#### **2. Port Already in Use**
```
Error: Address already in use
```
**Solution:**
- Use different port: `python app.py --port 8080`
- Find and stop process using port 5000

#### **3. Python Module Errors**
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
pip install -r requirements.txt
```

#### **4. Image Build Failure**
```
Error during Docker build
```
**Solution:**
- Check internet connection
- Ensure Docker has enough disk space
- Try: `docker system prune` to clean up

#### **5. Student Can't Connect**
**Solution:**
- Check firewall allows port 5000
- Ensure server is bound to 0.0.0.0
- Verify Docker container is running

### **Logs and Diagnostics**
- **Server logs**: `classroom.log`
- **Docker logs**: `docker ps` then `docker logs [container_id]`
- **System status**: Visit `/dashboard` or `/status`

## Maintenance

### **Regular Updates**
```bash
# Pull latest changes
git pull origin main

# Rebuild Docker image
python install.py

# Restart server
```

### **Cleaning Up**
```bash
# Remove Docker image
python uninstall.py

# Clean Docker system
docker system prune -a
```

### **Backup Lessons**
- Backup `static/lessons.json` and `static/lessons_en.json`
- Backup any custom scripts in Dockerfile

## Production Deployment

### **For Persistent Service**
Use process manager like `systemd` (Linux):

Create `/etc/systemd/system/linux-classroom.service`:
```ini
[Unit]
Description=Linux Classroom Server
After=docker.service
Requires=docker.service

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/Linux-Classroom-in-a-Browser
ExecStart=/usr/bin/python3 app.py --host 0.0.0.0 --port 5000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable linux-classroom
sudo systemctl start linux-classroom
```

### **Behind Reverse Proxy (Nginx)**
Example Nginx configuration:
```nginx
server {
    listen 80;
    server_name classroom.yourschool.edu;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

## Support

### **Getting Help**
- Check logs: `tail -f classroom.log`
- Monitor dashboard: `http://localhost:5000/dashboard`
- Review student guide: `STUDENT_GUIDE.md`
- Review teacher guide: `TEACHER_GUIDE.md`

### **Useful Commands**
```bash
# Check server status
curl http://localhost:5000/status

# Check Docker containers
docker ps

# View server logs
tail -f classroom.log

# Rebuild if needed
python install.py
```

## Next Steps

1. **Test the installation**: Visit `http://localhost:5000/`
2. **Review student guide**: Share `STUDENT_GUIDE.md` with students
3. **Monitor with dashboard**: Use teacher dashboard during class
4. **Customize lessons**: Edit lesson files for your curriculum
5. **Scale up**: For large classes, consider more powerful hardware

---

Your enhanced Linux Classroom is now ready! Students can start learning immediately with the interactive tutorial and guided lessons.