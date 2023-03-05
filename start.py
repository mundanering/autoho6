import subprocess
from pathlib import Path
from time import sleep
import pydirectinput as key

FILE_DIRECTORY = str(Path(__file__).parent)
LEPROC = FILE_DIRECTORY + r'\Locale.Emulator.2.5.0.1\LEProc.exe'
EOSD = FILE_DIRECTORY + r'\th6\eosd.exe'

if __name__ == '__main__':
    subprocess.Popen([LEPROC, EOSD])
    sleep(4.7)
    key.press('z')       # wejdz menu
    sleep(0.01)
    key.press('down')    # wybierz opcje extra start
    sleep(0.01)
    key.press('z')       # zatwierdz
    sleep(1.9)
    key.press('z')       # wybor postaci itd
    sleep(0.175)
    key.press('z')
    sleep(0.175)
    key.press('z')
