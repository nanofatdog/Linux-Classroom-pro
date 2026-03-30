# Use the official Ubuntu 22.04 as a base image
FROM ubuntu:22.04

# Set a non-interactive frontend for package installations to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install necessary software
# - openssh-server is added for SSH capability
RUN apt-get update && apt-get install -y \
    nano \
    vim \
    htop \
    tree \
    curl \
    git \
    python3 \
    python3-pip \
    python-is-python3 \
    build-essential \
    iputils-ping \
    iproute2 \
    net-tools \
    openssh-server \
    rsync \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Configure SSH Server to allow password authentication
RUN mkdir /var/run/sshd
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
# Disable DNS lookups for faster SSH connections
RUN echo "UseDNS no" >> /etc/ssh/sshd_config

# Expose the SSH port (good practice)
EXPOSE 22

# FIX: Remove the file that enables the 'externally-managed' environment error
RUN find /usr/lib/ -name "EXTERNALLY-MANAGED" -exec rm {} \;

# Create a non-root user 'student' for security
RUN useradd -m student

# Set a default password for the 'student' user
# The default password is set to 'student'. You can change it here.
RUN echo 'student:student' | chpasswd

# Create a shared directory for class materials
RUN mkdir -p /shared && chmod 777 /shared && chown student:student /shared

# Switch to the 'student' user to perform user-specific installations (Rust)
USER student
WORKDIR /home/student

# Install the Rust toolchain (rustc, cargo, etc.) as the student user
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add useful aliases and baseline configurations
RUN echo 'alias ll="ls -la"' >> ~/.bashrc
RUN echo 'alias cls="clear"' >> ~/.bashrc
RUN echo 'alias py="python3"' >> ~/.bashrc
RUN echo 'alias rb="cargo run"' >> ~/.bashrc

# Create helpful scripts for students
RUN echo '#!/bin/bash' > ~/classroom-info.sh
RUN echo 'echo "=== Linux Classroom Information ==="' >> ~/classroom-info.sh
RUN echo 'echo "Container IP: $(hostname -I | awk \"{print \\\$1}\")"' >> ~/classroom-info.sh
RUN echo 'echo "Hostname: $(hostname)"' >> ~/classroom-info.sh
RUN echo 'echo "Student user: $(whoami)"' >> ~/classroom-info.sh
RUN echo 'echo "Home directory: $HOME"' >> ~/classroom-info.sh
RUN echo 'echo "Python version: $(python3 --version 2>/dev/null || echo "Not available")"' >> ~/classroom-info.sh
RUN echo 'echo "Rust version: $(rustc --version 2>/dev/null || echo "Not available")"' >> ~/classroom-info.sh
RUN echo 'echo "Shared directory: /shared (if available)"' >> ~/classroom-info.sh
RUN echo 'echo "====================================="' >> ~/classroom-info.sh
RUN chmod +x ~/classroom-info.sh

# Create quick help script
RUN echo '#!/bin/bash' > ~/quick-help.sh
RUN echo 'echo "=== Linux Classroom Quick Help ==="' >> ~/quick-help.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "BASIC COMMANDS:"' >> ~/quick-help.sh
RUN echo 'echo "  pwd                 - Show current directory"' >> ~/quick-help.sh
RUN echo 'echo "  ls                  - List files"' >> ~/quick-help.sh
RUN echo 'echo "  cd [directory]      - Change directory"' >> ~/quick-help.sh
RUN echo 'echo "  mkdir [name]        - Create directory"' >> ~/quick-help.sh
RUN echo 'echo "  touch [file]        - Create file"' >> ~/quick-help.sh
RUN echo 'echo "  cat [file]          - Show file content"' >> ~/quick-help.sh
RUN echo 'echo "  cp [src] [dst]      - Copy file"' >> ~/quick-help.sh
RUN echo 'echo "  mv [src] [dst]      - Move/rename file"' >> ~/quick-help.sh
RUN echo 'echo "  rm [file]           - Remove file"' >> ~/quick-help.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "PYTHON COMMANDS:"' >> ~/quick-help.sh
RUN echo 'echo "  python3             - Start Python interpreter"' >> ~/quick-help.sh
RUN echo 'echo "  python3 script.py   - Run Python script"' >> ~/quick-help.sh
RUN echo 'echo "  pip install [pkg]   - Install Python package"' >> ~/quick-help.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "RUST COMMANDS:"' >> ~/quick-help.sh
RUN echo 'echo "  cargo new [name]    - Create new Rust project"' >> ~/quick-help.sh
RUN echo 'echo "  cargo run           - Build and run Rust project"' >> ~/quick-help.sh
RUN echo 'echo "  cargo build         - Build Rust project"' >> ~/quick-help.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "CLASSROOM COMMANDS:"' >> ~/quick-help.sh
RUN echo 'echo "  classroom-info      - Show container information"' >> ~/quick-help.sh
RUN echo 'echo "  myip                - Show container IP address"' >> ~/quick-help.sh
RUN echo 'echo "  cd /shared          - Go to shared classroom folder"' >> ~/quick-help.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "HELP:"' >> ~/quick-help.sh
RUN echo 'echo "  quick-help          - Show this help message"' >> ~/quick-help.sh
RUN echo 'echo "  man [command]       - Show manual for command"' >> ~/quick-help.sh
RUN echo 'echo "====================================="' >> ~/quick-help.sh
RUN chmod +x ~/quick-help.sh

# Create beginner tutorial script
RUN echo '#!/bin/bash' > ~/linux-tutorial.sh
RUN echo 'echo "=== Linux Beginner Tutorial ==="' >> ~/linux-tutorial.sh
RUN echo 'echo ""' >> ~/linux-tutorial.sh
RUN echo 'echo "STEP 1: Explore your environment"' >> ~/linux-tutorial.sh
RUN echo 'echo "Try these commands in order:"' >> ~/linux-tutorial.sh
RUN echo 'echo "1. pwd                      # Where am I?"' >> ~/linux-tutorial.sh
RUN echo 'echo "2. ls                       # What files are here?"' >> ~/linux-tutorial.sh
RUN echo 'echo "3. ls -la                   # Show all files with details"' >> ~/linux-tutorial.sh
RUN echo 'echo "4. cd ~                     # Go to home directory"' >> ~/linux-tutorial.sh
RUN echo 'echo ""' >> ~/linux-tutorial.sh
RUN echo 'echo "STEP 2: Create and manage files"' >> ~/linux-tutorial.sh
RUN echo 'echo "5. mkdir test_folder        # Create a folder"' >> ~/linux-tutorial.sh
RUN echo 'echo "6. cd test_folder           # Enter the folder"' >> ~/linux-tutorial.sh
RUN echo 'echo "7. touch hello.txt          # Create a file"' >> ~/linux-tutorial.sh
RUN echo 'echo "8. echo \"Hello Linux!\" > hello.txt  # Write to file"' >> ~/linux-tutorial.sh
RUN echo 'echo "9. cat hello.txt            # Read the file"' >> ~/linux-tutorial.sh
RUN echo 'echo ""' >> ~/linux-tutorial.sh
RUN echo 'echo "STEP 3: Try Python"' >> ~/linux-tutorial.sh
RUN echo 'echo "10. python3 --version       # Check Python version"' >> ~/linux-tutorial.sh
RUN echo 'echo "11. python3                 # Start Python (type exit() to quit)"' >> ~/linux-tutorial.sh
RUN echo 'echo "12. echo \"print(\\\"Hello from Python!\\\")\" > hello.py"' >> ~/linux-tutorial.sh
RUN echo 'echo "13. python3 hello.py        # Run Python script"' >> ~/linux-tutorial.sh
RUN echo 'echo ""' >> ~/quick-help.sh
RUN echo 'echo "Type these commands in the terminal above. Happy learning!"' >> ~/linux-tutorial.sh
RUN chmod +x ~/linux-tutorial.sh

# Add aliases to bashrc
RUN echo 'alias classroom-info="~/classroom-info.sh"' >> ~/.bashrc
RUN echo 'alias myip="hostname -I | awk \"{print \\\$1}\""' >> ~/.bashrc
RUN echo 'alias quick-help="~/quick-help.sh"' >> ~/.bashrc
RUN echo 'alias linux-tutorial="~/linux-tutorial.sh"' >> ~/.bashrc
RUN echo 'alias helpme="echo \"Try: quick-help, linux-tutorial, or classroom-info\""' >> ~/.bashrc

# Create a welcome message for when students login
RUN echo 'echo ""' >> ~/.bashrc
RUN echo 'echo "=== Welcome to Linux Classroom! ==="' >> ~/.bashrc
RUN echo 'echo "You are in an isolated Ubuntu Linux container."' >> ~/.bashrc
RUN echo 'echo ""' >> ~/.bashrc
RUN echo 'echo "Quick Start Commands:"' >> ~/.bashrc
RUN echo 'echo "  quick-help       - Show all basic commands"' >> ~/.bashrc
RUN echo 'echo "  linux-tutorial   - Step-by-step beginner tutorial"' >> ~/.bashrc
RUN echo 'echo "  classroom-info   - Show container information"' >> ~/.bashrc
RUN echo 'echo "  myip             - Show your container IP address"' >> ~/.bashrc
RUN echo 'echo ""' >> ~/.bashrc
RUN echo 'echo "Need help? Check the web interface for interactive lessons!"' >> ~/.bashrc
RUN echo 'echo "====================================="' >> ~/.bashrc
RUN echo 'echo ""' >> ~/.bashrc

# Switch back to root before setting the final CMD
USER root

# Add Cargo's bin directory to the student's PATH by adding it to their bash profile
RUN echo 'export PATH="/home/student/.cargo/bin:${PATH}"' >> /home/student/.bashrc
# Also add it for root user (for troubleshooting)
RUN echo 'export PATH="/root/.cargo/bin:${PATH}"' >> /root/.bashrc

# The command to run when the container starts:
# 1. Start the SSH daemon service as root.
# 2. Switch to the 'student' user and launch their default login shell.
CMD service ssh start && su - student

