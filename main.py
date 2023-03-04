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

while True:
    sct_img = sct.grab(GAME)
    # cv2.imshow('screen', np.array(sct_img))
    # 
    # if (cv2.waitKey(1) & 0xFF) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
