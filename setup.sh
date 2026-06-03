#!/data/data/com.termux/files/usr/bin/bash

# =================================================================
# 📱 ATOM Group Cleaner - One-Click Installer & Runner for Termux
# 🛡️ Developer: ATOM Clean
# 🥛 Zero Intervention - Clean Group and Messages
# =================================================================

# ANSI Color Codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # Reset Color

clear

# --- Text Typing Animation Helper ---
animate_text() {
    local text="$1"
    local color="$2"
    local delay=0.03
    for ((i=0; i<${#text}; i++)); do
        echo -ne "${color}${text:$i:1}${NC}"
        sleep $delay
    done
    echo ""
}

# --- ASCII Art Banner ---
echo -e "${CYAN}"
echo "    ___  ______ ____  ___  ___"
echo "   /   |/_  __/ __ \/   |/   |"
echo "  / /| | / / / / / / /| / /| |"
echo " / ___ |/ / / /_/ / ___ / ___ |"
echo "/_/  |_/_/  \____/_/  |_/_/  |_|"
echo " 🥛🛡️ ATOM - Termux Setup 🥛🛡️"
echo -e "${NC}"

sleep 0.3
animate_text ">>> Initializing installation sequence..." "${BLUE}"
sleep 0.2

# 1. Update Packages if needed
echo -e "${BLUE}[*] 1/3 Checking and installing Python...${NC}"
pkg install python -y > /dev/null 2>&1
echo -e "${GREEN}[+] Python is ready!${NC}"
echo ""

# 2. Install Telethon
echo -e "${BLUE}[*] 2/3 Installing Telethon library...${NC}"
pip install telethon --quiet
echo -e "${GREEN}[+] Telethon library is ready!${NC}"
echo ""

# 3. Downloading Cleaner Script
echo -e "${BLUE}[*] 3/3 Downloading group_cleaner.py script...${NC}"
# Use curl to fetch the latest group_cleaner.py from GitHub
# We'll use a placeholder URL which the user will replace with their actual GitHub raw URL
curl -s -o group_cleaner.py "https://raw.githubusercontent.com/atomxtols/atom-group-cleaner/main/group_cleaner.py"

if [ -f "group_cleaner.py" ]; then
    echo -e "${GREEN}[+] Script downloaded successfully!${NC}"
else
    echo -e "${RED}[-][Error] Failed to download group_cleaner.py. Checking backup local execution...${NC}"
fi
echo ""

animate_text ">>> Starting Group Cleaner Client..." "${GREEN}"
sleep 0.5

# Run the python script
python group_cleaner.py
