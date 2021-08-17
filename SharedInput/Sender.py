from pynput.keyboard import Key, KeyCode, Controller as KeyboardController, Listener
import socket
import time

keyboard = KeyboardController()
sending = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 25566))


def on_press(key):
    global sending
    if sending:
        time.sleep(0.2)
        s.send(str(key).encode())

    print(f"{str(key)} {type(str(key))}")


def on_release(key):
    global sending
    if key == Key.print_screen:
        if sending:
            sending = False
            print("stop sending")
        else:
            print("start sending")
            sending = True

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()