# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

import re


class Reg_Finder :
    """
    Représente l'analyseur de string à l'aide de regexp
    """
    # Regexp static pour différencier simplement les champs
    # pour un numero de téléphone ou de fax
	reg_tel_fax = ''
    # pour un numero rcs (siren)
	reg_rcs = ''
    # pour un taux
	reg_taux = ''
    # pour un montant
	reg_montant = ''
    # pour une adresse
	reg_adress = ''
    # pour un nom
	reg_nom = ''
    # pour le type d'une entreprise/société
	reg_type_soc = ''
    # pour une date
	reg_date = ''
    # pour une description/ un titre
	reg_descr = ''
    

    def __init__ (self, file) :
    	pass

    def isName (self, name) :
    	"""
    	Vérifie si ce champ peut être le nom
    	si oui,  actualise le nom
    	"""
    	pass
    
    def isTypeInc (self, type_entreprise) :
    	"""
    	Vérifie si ce champ peut être le type de l'entreprise
    	si oui,  actualise le type
    	"""
    	pass
    
    def isRCS (self, rcs) :
    	"""
    	Vérifie si ce champ peut être le numéro RCS
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isAddress (self, adresse) :
    	"""
    	Vérifie si ce champ peut être l'adresse
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isTelFax (self, tel_fax, isTel=True) :
    	"""
    	Vérifie si ce champ peut être le tel ou le fax
    	isTel is True si la probabilité qu'il s'agisse du tel est plus grande que la probabilité qu'il s'agisse du fax
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isTVA (self, tva) :
    	"""
    	Vérifie si ce champ peut être le numéro tva
    	si oui,  actualise le champ
    	"""
    	pass

    def isTitre (self, titre) :
    	"""
    	Vérifie si ce champ peut être le titre de la facture
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isNumFacture (self, numero) :
    	"""
    	Vérifie si ce champ peut être le numero de la facture
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isDate (self, date) :
    	"""
    	Vérifie si ce champ peut être la date de la facture
    	si oui,  actualise le nom
    	"""
    	pass
    
    def arePrestations (self, prests) :
    	"""
    	Vérifie si ce champ peut être les descriptions des prestations contenues dans la facture
    	si oui,  actualise le champ
    	"""
    	pass
    def isTVA (self, tva) :
    	"""
    	Vérifie si ce champ peut être le montant de la tva
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isTauxTVA (self, tauxTva) :
    	"""
    	Vérifie si ce champ peut être le taux tva
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isHT (self, ht) :
    	"""
    	Vérifie si ce champ peut être le montant HT
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isTTC (self, ttc) :
    	"""
    	Vérifie si ce champ peut être le montant TTC
    	si oui,  actualise le champ
    	"""
    	pass
    
    def isOthersTax (self, autres) :
    	"""
    	Vérifie si ce champ peut être d'autres taxes sur le total de la facture
    	si oui,  actualise le champ
    	"""
    	pass

