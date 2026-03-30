# Student Guide - Linux Classroom in a Browser

## Welcome!

You're about to start learning Linux, Python, and Rust in a safe, interactive environment. This guide will help you get started quickly.

## Quick Start

### 1. **Access the Classroom**
- Open your browser and go to: `http://[server-address]:5000/`
- You'll see a welcome tutorial - follow it for a quick orientation
- The interface has two main parts:
  - **Left Sidebar**: Lessons, help, and tools
  - **Right Side**: Linux terminal

### 2. **Your First Commands**
Once connected, try these basic commands:

```
pwd                     # Show current directory
ls                      # List files
whoami                  # Show your username
quick-help              # Show classroom help
```

### 3. **Interactive Learning**
- Click the **"Lessons"** tab in the sidebar
- Start with Lesson 1 and follow the instructions
- Each lesson has examples you can try in the terminal
- Use the Previous/Next buttons to navigate

## Helpful Features

### **Quick Help Tab**
- Click the **"Help"** tab for common Linux commands
- Click any command card to copy it to your terminal
- Organized by category: File operations, text editors, search tools

### **Quick Commands Tab**
- Ready-to-use commands with explanations
- One-click copy to terminal
- Includes Python and Rust examples

### **Student Tools Tab**
- Classroom-specific commands:
  - `classroom-info` - Show container details
  - `myip` - Display your container IP address
  - `cd /shared` - Go to shared classroom folder
- Useful shortcuts (aliases):
  - `ll` = `ls -la` (detailed file list)
  - `cls` = `clear` (clean terminal)
  - `py` = `python3`
  - `rb` = `cargo run`

## Learning Path

### **For Complete Beginners**
1. Run `linux-tutorial` in the terminal for an interactive guide
2. Complete Lessons 1-5 in the sidebar
3. Practice creating files and directories
4. Try the Python and Rust introduction lessons

### **If You Know Basic Linux**
1. Skip to advanced lessons (Lesson 6+)
2. Try the Python or Rust tutorials
3. Experiment with shell scripting
4. Practice with networking commands

## Tips & Tricks

### **Keyboard Shortcuts**
- `Ctrl+L` - Clear terminal screen
- `Tab` - Auto-complete commands and file names
- `↑/↓` arrows - Browse command history
- `Ctrl+C` - Cancel/stop current command
- `Ctrl+Space` - Toggle sidebar visibility

### **Terminal Controls**
Use the buttons above the terminal:
- **Clear** (eraser icon) - Clean the terminal
- **Zoom** (+/-) - Adjust font size
- **Fullscreen** - Expand terminal view

### **Getting Help**
- Type `quick-help` in terminal for command reference
- Use `man [command]` for Linux manual pages (e.g., `man ls`)
- Check the web interface help tabs
- For classroom-specific help: `helpme`

## Classroom Features

### **Shared Folder**
- All students can access `/shared` directory
- Great for collaborative work or class materials
- Navigate: `cd /shared`

### **Connect with Classmates**
- Each container has its own IP address
- Find your IP: `myip`
- Connect to classmates: `ssh student@[their-ip]`
- Password: `student`

### **Your Environment**
- Ubuntu 22.04 Linux
- Python 3 with pip
- Rust with Cargo
- Common tools: vim, nano, git, curl, htop, tree
- Isolated container - experiment safely!

## Common Tasks

### **Create and Run a Python Program**
```bash
# Create a Python file
echo 'print("Hello from Python!")' > hello.py

# Run it
python3 hello.py
```

### **Create and Run a Rust Program**
```bash
# Create new Rust project
cargo new my_project
cd my_project

# Build and run
cargo run
```

### **Edit a File**
```bash
# With nano (easier)
nano myfile.txt

# With vim (more powerful)
vim myfile.txt
# In vim: Press 'i' to insert, Esc then ':wq' to save and quit
```

### **Find Files**
```bash
# Find all .txt files
find . -name "*.txt"

# Search for text in files
grep "search term" file.txt
```

## Troubleshooting

### **Terminal Not Responding?**
- Try `Ctrl+C` to cancel current command
- Check your internet connection
- Refresh the browser page if needed
- Make sure Docker is running on the server

### **Command Not Found?**
- Check spelling
- Some commands need to be installed (most are pre-installed)
- Use `which [command]` to check if it exists

### **Need More Help?**
- Ask your teacher/instructor
- Check the web interface help sections
- Use the built-in help: `[command] --help`

## Remember

1. **Safe Environment** - Your container is isolated, so experiment freely!
2. **Progress Saved** - Your work persists during your session
3. **Reset on Exit** - The container is cleaned up when you leave
4. **Have Fun!** - Learning Linux should be enjoyable

## Quick Reference Card

```
Essential Commands:
pwd, ls, cd, mkdir, touch, cat, cp, mv, rm

Classroom Help:
quick-help, linux-tutorial, classroom-info, myip

Programming:
python3, pip, rustc, cargo, git

Editors:
nano, vim

Tools:
htop, tree, curl, wget, ssh
```

---

**Happy Learning!** 🐧🚀

Start with `linux-tutorial` or explore the lessons in the sidebar!