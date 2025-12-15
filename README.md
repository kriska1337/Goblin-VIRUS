
# Goblin‑VIRUS 👹  
A playful Windows‑only “prank” program that spawns a goblin that follows the mouse cursor, shows random speech‑bubble messages, and reacts when the user tries to open system tools such as Task Manager, Regedit or Windows Defender.  


## 🎯 Features  

| Feature | Description |
|---------|-------------|
| **🎯 Cursor‑following goblin** | The goblin image tracks the mouse pointer and stays on top of all windows. |
| **💬 Random phrases** | Speech‑bubble messages pop up at unpredictable intervals. |
| **🛡️ Defensive reaction** | When the user attempts to open Task Manager, Regedit, or Windows Defender the goblin displays a special warning or spawns extra copies. |
| **👻 Transparent overlay** | The goblin is drawn with an alpha channel, allowing it to sit “over” any application. |
| **🔄 Auto‑run on boot** | The script adds a registry entry (`Run`) so it starts automatically with Windows. |
| **🎭 Multiple goblins** | Repeated interactions can spawn extra goblins for extra fun. |

---

## 📦 Requirements  

Create a **`requirements.txt`** file (or install directly) with the following packages:

```text
pygame==2.6.0
pyautogui==0.9.54
requests==2.32.2
Pillow==10.4.0
psutil==6.1.0
pywin32==306
```

*All dependencies are compatible with Python 3.7 + (tested on Python 3.9‑3.12 on Windows 10/11).*

To install them in a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## 🚀 Quick start  

1. **Clone the repository**  

   ```bash
   git clone https://github.com/kriska1337/Goblin-VIRUS.git
   cd Goblin-VIRUS
   ```

2. **Install the dependencies**  

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program**  

   ```bash
   python main.py
   ```

   *The script will automatically add itself to the Windows startup registry.*

---

## 📦 Building an executable  

### Using PyInstaller  

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=goblin.ico main.py
# The binary will appear in the ./dist folder
```

### Using cx_Freeze  

1. Install cx_Freeze:  

   ```bash
   pip install cx_Freeze
   ```

2. Create **`setup.py`**  

   ```python
   from cx_Freeze import setup, Executable

   setup(
       name="Goblin-VIRUS",
       version="1.0",
       description="Goblin prank program",
       executables=[Executable("main.py", base="Win32GUI")]
   )
   ```

3. Build:  

   ```bash
   python setup.py build
   ```

---

## 🛑 How to stop the program  

1. Press **Ctrl + Alt + Del** → open **Task Manager**.  
2. Locate the `python.exe` (or `goblin.exe` if you built a .exe) process and end it.  
3. Remove the auto‑run entry:  

   - `Win + R` → `regedit` →  
     `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` →  
     delete the value named **“GoblinVIRUS”**.

---

## ⚠️ Disclaimer  

> ⚠️ This program is intended **solely for entertainment**.  
> Use it responsibly, only on computers you own or on systems where the owner has given explicit permission. The author is not liable for any misuse.

---  

