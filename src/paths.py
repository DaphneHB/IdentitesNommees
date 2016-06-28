# -*- coding: utf-8 -*-
"""
Created on Tue Jun 7 14:35 2016

@author: daphnehb
"""
import os

# constants
ABS_PATH_PRINC = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# on Linux and Mac
DATA_PATH_Unix = ABS_PATH_PRINC + "/data/"
INPUT_PATH_Unix = ABS_PATH_PRINC + "/data/input/"
OUTPUT_PATH_Unix = ABS_PATH_PRINC + "/data/output/"
USER_CHOSEN_PATH_Unix = ABS_PATH_PRINC + "/data/"

MODELS_PATH_Unix = ABS_PATH_PRINC + "/data/models/"

# TODO to check
# on Windows
"""
INPUT_PATH_Win = ABS_PATH_PRINC + "\data\input\"
OUTPUT_PATH_Win = ABS_PATH_PRINC + "\data\output\"
USER_CHOSEN_PATH_Win = ABS_PATH_PRINC + "\data\"
"""
