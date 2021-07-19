import socket
from cv2 import *
import pickle


def simple_socket():
    s = socket.socket()
    print("Socket successfully created")
    s.bind(('', 12345))

    s.listen(5)
    print("socket is listening")

    c, addr = s.accept()

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # bytes_frame = pickle.dumps(frame)
        c.send(frame.tobytes())


simple_socket()
