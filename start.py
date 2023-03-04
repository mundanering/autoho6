import subprocess
from pathlib import Path
import keyboard
from time import sleep

FILE_DIRECTORY = str(Path(__file__).parent)
LEPROC = FILE_DIRECTORY + r'\Locale.Emulator.2.5.0.1\LEProc.exe'
EOSD = FILE_DIRECTORY + r'\th6\eosd.exe'

if __name__ == '__main__':
    subprocess.Popen([LEPROC, EOSD])
    sleep(7)
    keyboard.send('enter')
    sleep(0.5)
    keyboard.send('ctrl+down')
    sleep(0.5)
    # jedyne co dziala
    keyboard.send('alt+tab')
    sleep(0.5)
    # tutaj tez dziala bo wyjdzie z gry
    keyboard.send('z')
    sleep(0.5)
    keyboard.send('z')
