import keyboard
import pyautogui
from pynput import keyboard as pynput_keyboard

# Function to switch language layout
def switch_layout(layout_code):
    pyautogui.press(layout_code)

# Define the layout code for Russian and English layouts (you may need to adjust these based on your system)
russian_layout_code = 'alt+shift'  # Change this to the appropriate shortcut for your system
english_layout_code = 'ctrl+shift'  # Change this to the appropriate shortcut for your system

# Global variable to track the current active keyboard
active_keyboard = None

# Callback function to detect the active keyboard
def on_activate_keyboard(key):
    global active_keyboard
    active_keyboard = key.name

# Start the keyboard listener
keyboard_listener = pynput_keyboard.Listener(on_activate=on_activate_keyboard)
keyboard_listener.start()

try:
    while True:
        # Check if the active keyboard is connected
        pyautogui.press('alt+shift')

except KeyboardInterrupt:
    # Stop the keyboard listener when Ctrl+C is pressed
    keyboard_listener.stop()
