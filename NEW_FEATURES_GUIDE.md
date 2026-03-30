# New Features Guide - Linux Classroom in a Browser

## Quick Start for Enhanced Version

### 1. Installation & Upgrade

```bash
# Clone/update the repository
git clone https://github.com/nanofatdog/Linux-Classroom-in-a-Browser.git
cd Linux-Classroom-in-a-Browser

# Install/update Python dependencies
pip install -r requirements.txt

# Build the enhanced Docker image
python install.py

# Start the server
python app.py
```

### 2. Access Points

- **Student Classroom**: `http://localhost:5000/` (or your server IP:port)
- **Teacher Dashboard**: `http://localhost:5000/dashboard`
- **Status API**: `http://localhost:5000/status` (JSON)

### 3. New Student Features

#### Container Information Commands
Once connected to your terminal, try these new commands:

```bash
# Show detailed container information
classroom-info

# Quick IP address display
myip

# List available aliases (type 'alias' to see all)
ll      # ls -la
cls     # clear
py      # python3
rb      # cargo run
```

#### Shared Directory
- Access the shared folder: `/shared`
- All students can read/write to this directory
- Useful for class materials and collaborative work

#### Enhanced SSH Between Containers
- Containers are on the same network (`classroom-net`)
- SSH to other students: `ssh student@[container_ip]`
- Password: `student`

### 4. Teacher Dashboard Features

#### Real-time Monitoring
- View all active student sessions
- See container IP addresses and client IPs
- Monitor session duration and activity
- Track data transfer (bytes sent/received)

#### System Resources
- CPU usage percentage
- Memory usage and availability
- Docker container statistics
- Server uptime and status

#### Auto-refresh
- Toggle auto-refresh on/off
- Default: 30-second updates
- Manual refresh button available

### 5. System Administration

#### Resource Limits
Each student container is limited to:
- **CPU**: 50% of one CPU core
- **Memory**: 512 MB RAM
- **Swap**: 1 GB total memory+swap
- Prevents any single student from overloading the system

#### Network Management
- Automatic network creation (`classroom-net`)
- Subnet: 172.20.0.0/16
- Graceful fallback to default bridge if network unavailable

#### Logging
- Detailed logs in `classroom.log` file
- Timestamps and session IDs for troubleshooting
- Error tracking and system events

### 6. Advanced Usage

#### Custom Server Configuration
```bash
# Custom port
python app.py --port 8080

# Specific host binding
python app.py --host 0.0.0.0 --port 8080

# HTTPS mode (requires certificate files)
python app.py --https --cert cert.pem --key key.pem
```

#### Monitoring via API
```bash
# Get JSON status
curl http://localhost:5000/status

# Example response includes:
# - Active sessions count
# - System resource usage
# - Docker information
# - Individual session details
```

#### Troubleshooting
- Check `classroom.log` for errors
- Verify Docker is running: `docker ps`
- Ensure network exists: `docker network ls | grep classroom-net`
- Rebuild image if needed: `python install.py`

### 7. Security Notes

- Each student gets an isolated Docker container
- Containers auto-remove when sessions end
- Resource limits prevent denial-of-service
- SSH between containers uses student/student credentials
- No root access within containers

### 8. Performance Tips

- For large classes, consider increasing system resources
- Monitor `classroom.log` for warnings
- Use the dashboard to identify resource-intensive sessions
- Consider running on a dedicated server for production use

### 9. Future Updates

Check the `IMPROVEMENTS_PLAN.md` file for planned enhancements including:
- Student progress tracking
- File upload/download capabilities
- Integrated development environment
- Assessment tools

---

**Need Help?**
- Check the logs: `tail -f classroom.log`
- Review the README.md for basic installation
- Examine the ENHANCEMENTS_SUMMARY.md for detailed changes
- Monitor the dashboard for real-time system status