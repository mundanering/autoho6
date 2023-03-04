import subprocess
from pathlib import Path
import os

FILE_DIRECTORY = str(Path(__file__).parent)
EOSD = FILE_DIRECTORY + r'\th6\eosd.exe'


if __name__ == '__main__':
    subprocess.run(EOSD)
