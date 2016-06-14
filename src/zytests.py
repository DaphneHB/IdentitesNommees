# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:16 2016

@author: daphnehb
"""

import tools


#TEST_FILE = "/data/txt/horiz.txt"
FNAME = "invoice-ZZMDAPHM-03-2016-0010129-2.pdf"

PDF_FILE = tools.INPUT_PATH_Unix+FNAME
DEST_PATH = tools.USER_CHOSEN_PATH_Unix
VERSION = "txt"

import pdf_ocr

# on génère la version demandée
import threads as th

generateur = th.Sous_Traitance(pdf_ocr.convert,[PDF_FILE, DEST_PATH, VERSION], start_time=0, fichier_import='pdf_ocr')


if VERSION!="txt" or VERSION!="text":

	# on génère aussi tout de même la version txt
	pdf_ocr.convert(PDF_FILE, DEST_PATH, "txt", stdout=True)
	
# on attend le thread
generateur.join()

print pdf_ocr.get_pdf_content(PDF_FILE)
