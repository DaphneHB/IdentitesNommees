# -*- coding: utf-8 -*-
"""
Created on Tue Jun 7 14:35:58 2016

@author: daphnehb
"""
#from xlwt import Workbook
from openpyxl import Workbook
import exceptions as exc
import os
import string


def csv_to_xls_vOLD(csv_filename, xls_filename=None, separateur=",") :
    """
    Transformation d'un fichier CSV, avec sep comme séparation, en un fichier xsl (Excel)
    Retourne le nom du fichier xls et son arborescence
    """
    # on vérifie que fichier d'entrée est bien un fichier CSV
    if not csv_filename.lower().endswith(".csv"):
        raise exc.NotCSVFileException(csv_filename)

    if xls_filename is None:
        # TODO demander à l'utilisateur ce qu'il veut donner comme nom
        # on créé un nouveau nom
        pre, ext = os.path.splitext(csv_filename)
        xls_filename = str(pre) + ".xls"

    with open(csv_filename,"r") as csv_file:
        # on crée l'objet qui fera le fichier Excel
        book = Workbook()
        # TODO : une feuille par facture (=> une liste de CSV en parametre)?
        feuille = book.add_sheet('feuille 1')
        # ajout des en-têtes
        """feuille.write(0,0,'id')
        feuille.write(0,1,'x')
        feuille.write(0,2,'y')
        feuille.write(0,3,'test')"""
        # pour chaque ligne du fichier d'entrée on met les valeurs dans le fichier excel
        for num_ligne,ligne in enumerate(csv_file.readlines()):
            # recuperation de la reference à la ligne du fichier Excel
            ref_ligne = feuille.row(num_ligne)
            # on recupere la ligne-liste sans \n final, et séparant les cases selon le séparateur
            ligne = ligne.rstrip("\n").split(separateur)
            # remplisage de la ligne cellule par cellule
            for num_cell,cell in enumerate(ligne):
                print cell
                ref_ligne.write(num_cell,str(cell))

        #feuille.col(0).width = 10000
        book.save(xls_filename)
        return xls_filename

def csv_to_xls(csv_filename, xls_filename=None, separateur=",") :
    """
    Transformation d'un fichier CSV, avec sep comme séparation, en un fichier xsl (Excel)
    Retourne le nom du fichier xls et son arborescence
    """
    # on vérifie que fichier d'entrée est bien un fichier CSV
    if not csv_filename.lower().endswith(".csv"):
        raise exc.NotCSVFileException(csv_filename)

    if xls_filename is None:
        # TODO demander à l'utilisateur ce qu'il veut donner comme nom
        # on créé un nouveau nom
        pre, ext = os.path.splitext(csv_filename)
        xls_filename = str(pre) + ".xls"

    excel_columns = list(string.ascii_uppercase)
    with open(csv_filename,"r") as csv_file:
        # on crée l'objet qui fera le fichier Excel
        book = Workbook()
        # TODO : une feuille par facture (=> une liste de CSV en parametre)?
        # for feuille in book.get_sheet_names()
        feuille = book.active
        # ajout des en-têtes
        """feuille.write(0,0,'id')
        feuille.write(0,1,'x')
        feuille.write(0,2,'y')
        feuille.write(0,3,'test')"""

        # pour chaque ligne du fichier d'entrée on met les valeurs dans le fichier excel
        for num_ligne,ligne in zip(excel_columns,csv_file.readlines()):
            # recuperation de la reference à la ligne du fichier Excel
            #ref_ligne = feuille.row(num_ligne)
            # on recupere la ligne-liste sans \n final, et séparant les cases selon le séparateur
            ligne = ligne.rstrip("\n").split(separateur)
            # remplisage de la ligne cellule par cellule
            for num_cell,cell in enumerate(ligne, start=1):
                num_case = str(num_ligne) + str(num_cell)
                feuille[num_case] = str(cell)

        #feuille.col(0).width = 10000
        book.save(xls_filename)
        return xls_filename


############ TESTS
csv_to_xls("csv_sample.csv", "xls_sample.xls")
from win32com.client import Dispatch

xl = Dispatch("Excel.Application")
xl.Visible = True # otherwise excel is hidden

# newest excel does not accept forward slash in path
wb = xl.Workbooks.Open(r"xls_sample.xls")
wb.Close()
xl.Quit()

"""
# création de la feuille 1
feuil1 = book.add_sheet('feuille 1')

# ajout des en-têtes
feuil1.write(0,0,'id')
feuil1.write(0,1,'x')
feuil1.write(0,2,'y')
feuil1.write(0,3,'test')

# ajout des valeurs dans la ligne suivante
ligne1 = feuil1.row(1)
ligne1.write(0,'1')
ligne1.write(1,'235.0')
ligne1.write(2,'424.0')
ligne1.write(3,'a')


# ajustement éventuel de la largeur d'une colonne


# éventuellement ajout d'une autre feuille 2
feuil2 = book.add_sheet('feuille 2')



# création matérielle du fichier résultant
book.save('monsimple.xls')
"""
