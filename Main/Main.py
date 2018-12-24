# A Python Sudoku solver
# Authors: Rahman Al-Shabazz, Jeri Oyenuga (2018)

# Import required modules
import numpy as np
import pandas as pd

# Import out checking functions
# (When using Pycharm, make sure to select main folder as source folder in settings)
import CheckFunctions as check

# Initialise our variables

grid = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9]])

solution = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9]])

possibilities = np.ndarray(shape=(9,9,1), dtype=list)