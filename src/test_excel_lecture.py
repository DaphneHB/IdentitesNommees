# -*- coding: utf-8 -*-
"""
Created on Tue Jun 7 14:35:58 2016

@author: daphnehb
"""

import xlrd
# ouverture du fichier Excel
wb = xlrd.open_workbook('testxy.xls')

# feuilles dans le classeur
print wb.sheet_names()
#[u'Feuil1', u'Feuil2', u'Feuil3']

# lecture des données dans la première feuille
sh = wb.sheet_by_name(u'Feuil1')
for rownum in range(sh.nrows):
    print sh.row_values(rownum)
"""
[u'id', u'x', u'y', u'test']
[1.0, 235.0, 424.0, u'a']
[2.0, 245.0, 444.0, u'b']
[3.0, 255.0, 464.0, u'c']
[4.0, 265.0, 484.0, u'd']
[5.0, 275.0, 504.0, u'e']
[6.0, 285.0, 524.0, u'f']
[7.0, 295.0, 544.0, u'g']
"""
# lecture par colonne
colonne1 = sh.col_values(0)
print colonne1
#[u'id', 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

colonne2=sh.col_values(1)
print colonne2
#[u'x', 235.0, 245.0, 255.0, 265.0, 275.0, 285.0, 295.0]

# extraction d'un élément particulier
print colonne1[1],colonne2[1]
