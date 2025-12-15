# MoonRise Goblin 👹

A fun prank program featuring a goblin that follows your cursor and asks unexpected questions. The goblin appears on top of all windows and reacts when you try to open system applications.

## Features

- 🎯 Goblin follows your mouse cursor
- 💬 Random phrases in speech bubbles
- 🛡️ Defensive reaction when attempting to open Task Manager, Regedit, or Windows Defender
- 👻 Transparent window overlay on top of all applications
- 🔄 Auto-start on system boot (adds itself to Windows registry)
- 🎭 Multiple goblins spawn on interaction

## Requirements

- Python 3.7+
- Windows OS
- Python libraries:
  - pygame
  - pyautogui
  - requests
  - Pillow (PIL)
  - psutil
  - pywin32

## Installation

1. Clone the repository:

git clone https://github.com/[your-username]/krutiy-goblin.git
cd krutiy-goblin

2. Install dependencies:

pip install pygame pyautogui requests Pillow psutil pywin32

## Usage

Simply run the script:

python goblin.py

**Warning:** The program will automatically add itself to Windows startup via registry.

## Building to .exe

To create an executable file using PyInstaller:

1. Install PyInstaller:

pip install pyinstaller

2. Build the program:

pyinstaller --onefile --noconsole --icon=goblin.ico goblin.py

3. The compiled .exe file will be in the `dist/` folder

### Alternative method with cx_Freeze:

1. Install cx_Freeze:

pip install cx_Freeze

2. Create a `setup.py` file:

from cx_Freeze import setup, Executable

setup(
    name="KrutiyGoblin",
    version="1.0",
    description="Goblin Prank Program",
    executables=[Executable("goblin.py", base="Win32GUI")]
)

3. Build:

python setup.py build

## How to Stop the Program

- Press `Ctrl+Alt+Delete` → Task Manager
- Find the `python.exe` or `goblin.exe` process
- End the process
- Remove from startup: `Win+R` → `regedit` → `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` → delete "GoblinPrank"

## Disclaimer

⚠️ This program is created purely for entertainment purposes. Use it responsibly and only on your own computers or with the owner's permission. The author is not responsible for misuse.
