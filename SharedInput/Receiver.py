from pynput.keyboard import Key, Controller as KeyboardController
import socket

keyboard = KeyboardController()


s = socket.socket()
s.bind(('', 25566))
s.listen(5)
c, addr = s.accept()


def get_key(key):
    if key == "Key.backspace":
        return Key.backspace
    elif key == "Key.space":
        return Key.space
    elif key == "Key.up":
        return Key.up
    elif key == "Key.down":
        return Key.down
    elif key == "Key.left":
        return Key.left
    elif key == "Key.right":
        return Key.right
    elif key == "Key.enter":
        return Key.enter
    elif key == "Key.home":
        return Key.home
    elif key == "Key.end":
        return Key.end
    elif key == "Key.tab":
        return Key.tab
    elif key == "Key.caps_lock":
        return Key.caps_lock
    elif key == "Key.ctrl_l":
        return Key.ctrl_l
    elif key == "Key.ctrl_r":
        return Key.ctrl_r
    elif key == "Key.alt_l":
        return Key.alt_l
    elif key == "Key.alt_r":
        return Key.alt_r
    elif key == "Key.shift":
        return Key.shift
    elif key == "Key.shift_r":
        return None
    elif key == "Key.delete":
        return Key.delete
    else:
        return key


while True:
    key = c.recv(13).decode()
    key = str(key)
    print(f"1{key} {type(key)}")
    key = get_key(key)
    print(f"2{key} {type(key)}")
    tmp = 'o'
    print(f"3{tmp} {type(tmp)}")
    # if key is not None:
        # keyboard.press(key)
        # keyboard.release(key)
