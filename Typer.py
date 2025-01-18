import time
import sys
import keyboard

def typer(text):
  for char in text:
    if char in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?']:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left shift', char]))
    elif char in ['€']:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left ctrl', 'left alt', char]))
    elif char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left shift', char.lower()]))
    else:
      keyboard.press_and_release(char)

time.sleep(3)
typer(' '.join(sys.argv[1:]))
