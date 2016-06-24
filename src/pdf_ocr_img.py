# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:14:57 2016

@author: daphnehb
"""
"""
Tests de lecture de PDF avec le traitement d'image
"""

IMNAME = "data/input/img-160302152757.png"
FNAME = "data/input/air france.pdf"

import sys

def rotation_pdf(filename,outfile=None):
    import PyPDF2
    # fichier temporaire
    outfilename = "file_rotate.pdf"

    minutesFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    page.rotateClockwise(180)

    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(page)
    resultPdfFile = open(outfilename, 'wb')
    pdfWriter.write(resultPdfFile)
    minutesFile.close()
    resultPdfFile.close()
    
    # on renomme le fichier de sortie
    if outfile is None :
        outfile = filename
    # recopier le fichier temporaire dans outfile et supprimer ce fichier temporaire
    # TODO

# Affichage du fichier IMNAME
with open(IMNAME) as monfichier:
    for i in range(10):
        pass #print monfichier.readline()
        
# "Faux" PDF -> PNG
def pdf_to_png(pdffile) :
    import subprocess
    import os
    import traceback
    import sys
    
    print "LAUNCHING!!!! ",len(sys.argv)
    if not len(sys.argv) >= 3:
        usage_exit()
    try:
        resolution = int(sys.argv[1])
    except ValueError:
        usage_exit()
    for filepath in sys.argv[1:]:
        (name, ext) = os.path.splitext(filepath)
        if ext.lower().endswith("pdf"):
            print "*** Converting %s..." % filepath
            gs_pdf_to_png(os.path.join(os.getcwd(), filepath), resolution)

# Absolute path to Ghostscript executable here or command name if Ghostscript is
# in your PATH.
GHOSTSCRIPTCMD = "gs"


def usage_exit():
        sys.exit("Usage: %s png_resolution pdffile1 pdffile2 ..." %
            os.path.basename(sys.argv[0]))


def gs_pdf_to_png(pdffilepath, resolution):
    if not os.path.isfile(pdffilepath):
        print "'%s' is not a file. Skip." % pdffilepath
    pdffiledir = os.path.dirname(pdffilepath)
    pdffilename = os.path.basename(pdffilepath)
    pdfname, ext = os.path.splitext(pdffilepath)

    try:    
        # Change the "-rXXX" option to set the PNG's resolution.
        # http://ghostscript.com/doc/current/Devices.htm#File_formats
        # For other commandline options see
        # http://ghostscript.com/doc/current/Use.htm#Options
        arglist = [GHOSTSCRIPTCMD,
                  "-dBATCH",
                  "-dNOPAUSE",
                  "-sOutputFile=%s.png" % pdfname,
                  "-sDEVICE=png16m",
                  "-r%s" % resolution,
                  pdffilepath]
        print "Running command:\n%s" % ' '.join(arglist)
        sp = subprocess.Popen(
            args=arglist,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    except OSError:
        sys.exit("Error executing Ghostscript ('%s'). Is it in your PATH?" %
            GHOSTSCRIPTCMD)            
    except:
        print "Error while running Ghostscript subprocess. Traceback:"
        print "Traceback:\n%s"%traceback.format_exc()

    stdout, stderr = sp.communicate()
    print "Ghostscript stdout:\n'%s'" % stdout
    if stderr:
        print "Ghostscript stderr:\n'%s'" % stderr

# PNG -> "Bon" PDF
from PIL import Image
import pytesseract 
print pytesseract.image_to_string(Image.open(IMNAME))