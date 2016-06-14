# -*- coding: utf-8 -*-
"""
Created on Thu Jun 9 13 :46 2016

@author : daphnehb
"""

import sys
import tools

# VERSION 1
"""
from textract import process
text = process('/tmp/mydocument.pdf')
# ! UTF-8 non capturé, accents illlisibles + marquage des sauts de lignes et caractères spcéciaux avec \
"""

# VERSION 2
def get_pdf_content(pdf_path, page_nums=[0]) :
    """
    Récupère le texte sans mise en page contenu dans le fichier PDF pdf_path
    Gère les accent
    ! N'affiche pas les sauts de lignes (mots collés d'une ligne sur l'autre)
    """
    import PyPDF2
    content = ''
    p = file(pdf_path, "rb")
    pdf = PyPDF2.PdfFileReader(p)
    for page_num in page_nums :
        content += pdf.getPage(page_num).extractText()
    return content

# VERSION 3
# pdfminer version (command line)
import subprocess as sub
"""
Lit un fichier PDF et en retourne son texte horizontal par défaut
Options :
-V retourne aussi le texte vertical
"""
#sub.Popen(['pdf2txt.py', '-V', PDF_FILE])

# VERSION 4
# pdfminer version
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, dest_path, type_out="txt",stdout=False, pages=None) :
    """
    Enregistre le contenu txt du PDF en un fichier de type outtype dans data/<outtype>
    Types acceptés "txt", "html", "xml"
    Lit aussi le texte vertical
    ! Lecture de la facture uniquement possible pour du txt
    """
    # on vérifie que le fichier pdf d'entrée existe bien
    tools.verify_path(fname,file_too=True)
    if not pages :
        pagenums = set()
    else :
        pagenums = set(pages)
    basen,_,ext = tools.recup_basedirname_extension(fname)
    # oon retire le . avant l'extension
    ext = ext[1 :]
    # input option
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    imagewriter = None
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    # on autorise la lecture verticale
    laparams.detect_vertical = True

    outtype = type_out
    # on modifie la destination, le nom du dossier étant comme l'extension
    dest_path = tools.recup_destination(dest_path,outtype)

    # le fichier de sortie est alors nommé selon le fichier d'entrée avec la nouvelle extension
    # et dans le dossier correspondant à l'extension attendue
    outfile = '{}{}.{}'.format(dest_path,basen,outtype)
    if not stdout :
        output = file(outfile, 'w')
    else :
        output = sys.stdout
    
    manager = PDFResourceManager(caching=caching)
    if outtype == 'txt' or outtype=="text" :
        converter = TextConverter(manager, output, codec=codec, laparams=laparams,
                               imagewriter=imagewriter)
    elif outtype == 'xml' :
        converter = XMLConverter(manager, output, codec=codec, laparams=laparams,
                              imagewriter=imagewriter)
    elif outtype == 'html' :
        converter = HTMLConverter(manager, output, codec=codec, scale=scale,
                               layoutmode=layoutmode, laparams=laparams,
                               imagewriter=imagewriter)
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums,caching=caching) :
        interpreter.process_page(page)
    infile.close()
    converter.close()
    output.close
    return 1

