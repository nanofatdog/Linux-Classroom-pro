# Teacher Guide - Enhanced Linux Classroom

## New Student-Friendly Features

### **Enhanced User Interface**
- **Modern, responsive design** with intuitive layout
- **Welcome tutorial** for first-time students
- **Tabbed sidebar** with Lessons, Help, Quick Commands, and Student Tools
- **Dark/light theme** optimized for learning
- **Interactive command cards** with one-click copy to terminal

### **Student Learning Tools**
- **Interactive beginner tutorial** (`linux-tutorial` command)
- **Quick help system** (`quick-help` command)
- **Classroom information** (`classroom-info` command)
- **Step-by-step lessons** in both English and Thai
- **Built-in aliases** for common commands (`ll`, `cls`, `py`, `rb`)

### **Enhanced Terminal Experience**
- **Better terminal controls** (clear, zoom, fullscreen)
- **Keyboard shortcuts** (Ctrl+L to clear, Ctrl+Space to toggle sidebar)
- **Command history** with up/down arrows
- **Auto-complete** with Tab key
- **Visual feedback** when copying commands

## Access Points

### **For Students**
- **Main interface (English lessons)**: `http://localhost:5000/`
- **Thai lessons**: `http://localhost:5000/thai`
- **English lessons**: `http://localhost:5000/english`
- **Classic interface**: `http://localhost:5000/classic`

### **For Teachers**
- **Teacher dashboard**: `http://localhost:5000/dashboard`
- **System status API**: `http://localhost:5000/status`

## New Classroom Commands

Students have access to these helpful commands:

| Command | Description | Example |
|---------|-------------|---------|
| `quick-help` | Shows all basic Linux commands | `quick-help` |
| `linux-tutorial` | Interactive step-by-step tutorial | `linux-tutorial` |
| `classroom-info` | Container information and IP | `classroom-info` |
| `myip` | Quick IP address display | `myip` |
| `helpme` | Suggests help commands | `helpme` |

**Aliases:**
- `ll` = `ls -la` (detailed file listing)
- `cls` = `clear` (clear terminal)
- `py` = `python3`
- `rb` = `cargo run`

## Lesson Systems

### **English Lessons** (20 lessons)
Located in `static/lessons_en.json`
- Covers Linux basics, Python, Rust, networking, scripting
- Step-by-step with practical examples
- Progressive difficulty

### **Thai Lessons** (50 lessons)  
Located in `static/lessons.json`
- Comprehensive coverage from basics to advanced
- Includes Python and Rust programming
- Original lesson set

## Teacher Dashboard Features

### **Real-time Monitoring**
- Active student sessions with IP addresses
- Container resource usage
- Session duration and activity
- Data transfer statistics

### **System Health**
- CPU and memory usage
- Docker container statistics
- Network status
- Server uptime

### **Management**
- Auto-refresh (every 30 seconds)
- Manual refresh option
- System information display

## Classroom Management Tips

### **First Class Setup**
1. Start the server: `python app.py`
2. Share the main URL with students: `http://[your-server]:5000/`
3. Monitor sessions on the dashboard: `http://[your-server]:5000/dashboard`
4. For Thai students: share `/thai` endpoint

### **During Class**
- Use the dashboard to monitor student activity
- Check for stuck students (long inactive sessions)
- Monitor system resources to prevent overload
- Use shared folder (`/shared`) for class materials

### **Troubleshooting**
- **Student can't connect**: Check Docker is running, check logs
- **Terminal not responding**: Student can refresh page
- **Slow performance**: Check resource limits, monitor dashboard
- **Command not working**: Check student container logs

## Student Learning Path

### **Recommended Progression**
1. **Complete beginners**: Start with `linux-tutorial` command
2. **Follow lessons**: Lessons 1-5 (Linux basics)
3. **Programming intro**: Lessons 7-8 (Python), 9-10 (Rust)
4. **Advanced topics**: Lessons 11-20 (permissions, scripting, git)

### **Assessment Ideas**
- Ask students to complete specific tasks from lessons
- Use shared folder for assignment submissions
- Have students SSH to each other's containers (networking practice)
- Review Python/Rust programs created in class

## Technical Details

### **Resource Limits**
Each student container is limited to:
- **CPU**: 50% of one CPU core
- **Memory**: 512MB RAM
- **Swap**: 1GB total
- **Network**: Isolated classroom network

### **Security Features**
- Non-root user (`student`) with limited privileges
- Isolated Docker containers
- Read/write access only to home and shared directories
- SSH between containers only (classroom network)

### **Logging**
- Server logs: `classroom.log`
- Docker container logs available via dashboard
- Session activity tracking

## Quick Start for Teachers

```bash
# Clone/update repository
git clone https://github.com/nanofatdog/Linux-Classroom-in-a-Browser.git
cd Linux-Classroom-in-a-Browser

# Install dependencies
pip install -r requirements.txt

# Build Docker image with new features
python install.py

# Start server
python app.py

# Access interfaces:
# - Student classroom: http://localhost:5000/
# - Teacher dashboard: http://localhost:5000/dashboard
# - Thai lessons: http://localhost:5000/thai
```

## Files to Review

- `STUDENT_GUIDE.md` - Student orientation document
- `ENHANCEMENTS_SUMMARY.md` - Technical changes made
- `NEW_FEATURES_GUIDE.md` - Quick feature reference
- `templates/index_improved.html` - New UI template
- `static/lessons_en.json` - English lessons
- `Dockerfile` - Enhanced container setup

## Support

For issues or questions:
1. Check `classroom.log` for errors
2. Monitor the teacher dashboard
3. Review student guide for common issues
4. Check Docker status: `docker ps`, `docker logs`

---

The enhanced Linux Classroom provides a more engaging, student-friendly learning environment while giving teachers better tools for monitoring and management.