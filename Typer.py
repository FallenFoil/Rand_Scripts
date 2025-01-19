import time
import sys
import keyboard

layouts = {
  'pt': [
    ['|', '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '»', '*', '`', 'ª', '^', ';', ':', '_'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç'],
    ['@', '£', '§', '€', '{', '[', ']', '}', '¨'],
    [],
    {
      '~': [['~'], ['space']],
      '^': [['left shift', '^'], ['space']],
      '`': [['left shift', '`'], ['space']]
    }
  ],
  'intl': [
    # shift
    ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?'],
    # shift
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    # ctrl + alt
    ['¡', '²', '³', '¤', '€', '¼', '½', '¾', '‘', '’', '¥', '×', 'ä', 'å', 'é', '®', 'þ', 'ü', 'ú', 'í', 'ó', 'ö', '«', '»', 'á', 'ß', 'ð', 'ø', '¶', '´', '¬', 'æ', '©', 'ñ', 'µ', 'ç', '¿'],
    ['Ä', 'Å', 'É', 'Þ', 'Ü', 'Ú', 'Í', 'Ó', 'Ö', 'Á', 'Ð', 'Ø', 'Æ', 'Ñ', 'Ç'],
    {
      '~': [['left shift', '~'], ['space']],
      '^': [['left shift', '^'], ['space']],
      '`': [['`'], ['space']],
      'Ç': [["'"], ['left shift', 'c']],
      '¹': [['left ctrl', 'left alt', 'left shift', '1']],
      '£': [['left ctrl', 'left alt', 'left shift', '4']],
      '÷': [['left ctrl', 'left alt', 'left shift', '=']],
      '§': [['left ctrl', 'left alt', 'left shift', 's']],
      '°': [['left ctrl', 'left alt', 'left shift', ';']],
      '¨': [['left ctrl', 'left alt', 'left shift', "'"]],
      '¦': [['left ctrl', 'left alt', 'left shift', '\\']],
      '¢': [['left ctrl', 'left alt', 'left shift', 'c']]
    }
  ]
}
# keyboard.press_and_release(keyboard.get_hotkey_name(['left ctrl', 'left alt', "'"]))

layout = 'intl'

def typer(text):
  char_set = layouts[layout]
  for char in text:
    if char in char_set[0]:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left shift', char]))
    elif char in char_set[1]:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left shift', char.lower()]))
    elif char in char_set[2]:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left ctrl', 'left alt', char]))
    elif char in char_set[3]:
      keyboard.press_and_release(keyboard.get_hotkey_name(['left ctrl', 'left alt', 'left shift', char.lower()]))
    elif char in char_set[4].keys():
      for shortcut in char_set[4][char]:
        keyboard.press_and_release('+'.join(shortcut))
    else:
      keyboard.press_and_release(char)

if len(sys.argv) == 1:
  print('Exiting!')
  exit(0)

if sys.argv[1] in layouts.keys():
  layout = sys.argv[1]
  time.sleep(3)
  typer(' '.join(sys.argv[2:]))
else:
  time.sleep(3)
  typer(' '.join(sys.argv[1:]))
