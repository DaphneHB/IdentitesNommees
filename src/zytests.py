# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:16 2016

@author: daphnehb
"""

import tools


#TEST_FILE = "/data/txt/horiz.txt"
FNAME = "Facture n° 2016010501503.pdf"

PDF_FILE = tools.INPUT_PATH_Unix+FNAME
DEST_PATH = tools.USER_CHOSEN_PATH_Unix
VERSION = "html"

import pdf_ocr

pdf_ocr.generatorPDFtoTxt(PDF_FILE,DEST_PATH,VERSION)