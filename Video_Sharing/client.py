import socket
from cv2 import *
import pickle
import numpy as np

def simple_client():
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))

    while True:
        #frame = pickle.loads(s.recv(921600))

        frame = s.recv(921600)
        frame = np.frombuffer(frame, dtype=np.uint8)
        frame = np.reshape(frame, newshape=(480, 640, 3))

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    s.close()


simple_client()
