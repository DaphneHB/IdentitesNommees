# -*- coding: utf-8 -*-
"""
Created on Thu Jun 9 13:46 2016

@author: daphnehb
"""

PDF_FILE = "data/input/FCT_76596181_19193189.pdf"

"""
from textract import process
text = process('/tmp/mydocument.pdf')
# ! UTF-8 non capturé, accents illlisibles + marquage des sauts de lignes et caractères spcéciaux avec \
"""


def get_pdf_content(pdf_path, page_nums=[0]):
    """
    Récupère le texte sans mise en page contenu dans le fichier PDF pdf_path
    Gère les accent
    ! N'affiche pas les sauts de lignes (mots collés d'une ligne sur l'autre)
    """
    import PyPDF2
    content = ''
    p = file(pdf_path, "rb")
    pdf = PyPDF2.PdfFileReader(p)
    for page_num in page_nums:
        content += pdf.getPage(page_num).extractText()
    return content
#print get_pdf_content(PDF_FILE)

# pdfminer version (command line)
import subprocess as sub
sub.Popen(['pdf2txt.py', PDF_FILE])
