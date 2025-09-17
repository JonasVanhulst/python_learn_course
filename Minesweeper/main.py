# Filename: main.py
# Author: Jonas Vanhulst
# Created: 2025-09-25
# Description: Minesweeper game programmed in python.

# General imports
import os
import sys

# Custom imports
from lib.minesweeper import *

if __name__ == "__main__":
    # Adding the path to the custom import file
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
    
    # Printing welkom message to the user
    print_header()
    
    # Launching the minesweeper game
    play_minesweeper()
