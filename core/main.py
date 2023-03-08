from pathlib import Path
from time import sleep

import keyboard
import numpy as np
import cv2
from mss import mss
from PIL import Image

GAME = {
    'top': 10,
    'left': 250,
    'width': 950,
    'height': 1050
}

sct = mss()


def keypress(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)


while True:
    # screen
    sct_img = np.array(sct.grab(GAME))
    # cv2.imshow('screen', np.array(sct_img))

    # analiza

    # ruch
    keypress('z')  # z
    sleep(0.05)

    # restart
    # method = cv2.TM_SQDIFF
    #
    # FILE_DIRECTORY = str(Path(__file__).parent.parent)
    # fail = cv2.imread(FILE_DIRECTORY + r'/images/fail2.png')
    # fail = cv2.cvtColor(fail, cv2.COLOR_BGR2GRAY)
    # sct_img = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)
    #
    # result = cv2.matchTemplate(sct_img, fail, method)

    # if (cv2.waitKey(1) & 0xFF) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
