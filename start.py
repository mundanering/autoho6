import subprocess
from pathlib import Path
from time import sleep
import keyboard


def keypress(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)


FILE_DIRECTORY = str(Path(__file__).parent)
LEPROC = FILE_DIRECTORY + r'\Locale.Emulator.2.5.0.1\LEProc.exe'
EOSD = FILE_DIRECTORY + r'\th6\vpatch.exe'


if __name__ == '__main__':
    subprocess.Popen([LEPROC, EOSD])
    sleep(5)
    keypress('z')       # wejdz menu
    sleep(0.2)
    keypress('down')    # wybierz opcje extra start
    sleep(0.1)
    for i in range(17):
        keypress('z')
        sleep(0.1)
