import os
import shutil
import subprocess

import ttrpg

from pathlib import Path
from ttrpg.config import *

PATH_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_ACTIVATE_SRC = Path(PATH_DIR, DIR_SCRIPTS, "activate_this.py")
FILE_ACTIVATE = Path(DIR_VIRT, "bin", "activate_this.py")

def load_virt():
  """ Load virtual environment, create if missing. """
  if not Path(DIR_VIRT).is_dir():
    call(f"python -m venv {DIR_VIRT}")
    shutil.copyfile(FILE_ACTIVATE_SRC, FILE_ACTIVATE)
    # Load virtual environment.
    _load_virt()
    # Upgrade pip.
    call(f"python -m pip install --upgrade pip")
    # Install dependencies.
    call(f"python -m pip install -r requirements.txt")
    return
  # Load the virtual environment.
  _load_virt()


def call(command):
  """ Small auto-split wrapper around subprocess.call. """
  if type(command) == str:
    command = command.split()
  return subprocess.call(command)


def _load_virt():
  """ Small internal method for loading the virtual environment. """
  with open(FILE_ACTIVATE) as fh:
    exec(fh.read(), {'__file__': FILE_ACTIVATE})

load_virt()
