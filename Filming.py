from cv2 import *
import numpy as np


def start_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # gray = cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1)
        frame = cv2.flip(frame, 1)

        width, height, _ = frame.shape

        img = frame

        gauss = np.random.normal(0, 0.2, img.size)
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')

        img_gauss = cv2.add(img, gauss)

        cv2.imshow('frame', img_gauss)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


start_camera()

