import sys
from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your main Python script
script = 'hands.py'

# Dependencies (add any other required libraries)
build_exe_options = {
    "includes": ["mediapipe", "wmi", "pyautogui", "pycaw"],
    "packages": ["mediapipe", "wmi", "pyautogui", "pycaw"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for GUI applications

executables = [Executable(script, base=base)]

setup(
    name="AICamera",
    version="1.0",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=executables
)
