# -*- coding: utf-8 -*-
"""
Created on Tue Jun 7 13:55 2016

@author: daphnehb
"""
from enum import Enum

class SystemesExploit (Enum) :
    """
    Enumération représentant le système d'exploitation de l'utilisateur
    """
    Macintosh = "Mac OS X"
    Windows = "Windows"
    Linux = "Linux"

    def __str__(self):
        return "Système {}".format(self)

# print SystemesExploit.Linux

class TYPE_REGEXP (Enum) :
	"""
	Enumération représentant le type de mot reconnu par la regexp
	"""
	DATE, \
	LIEU, \
	ADRESSE, \
	MONTANT, \
	NOM, \
	TYPE_SOCIETE, \
	DESCRIPTION, \
	TAUX, \
	TEL, \
	FAX, \
	RCS, \
	AUTRE = range(12)
