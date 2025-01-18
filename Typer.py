import time
import sys
import keyboard

def typer(text):
  for char in text:
    if char == '!':
      keyboard.press_and_release('shift+1')
    elif char == '@':
      keyboard.press_and_release('shift+2')
    elif char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left shift'], char.lower()))
    else:
      keyboard.press_and_release(char)

time.sleep(3)
typer(' '.join(sys.argv[1:]))
