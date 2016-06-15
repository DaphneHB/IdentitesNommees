# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

import re


class Reg_Finder :
    """
    Représente l'analyseur de string à l'aide de regexp
    Utilisant re.search(reg,str,re.I).group() pour récupérer la plus grosse parcelle
    Puis en décodant la sting string..decode("utf-8", "ignore")
    """
    # Regexp static pour différencier simplement les champs
    # pour un numero de téléphone ou de fax
    # accepte les séparateurs . espace et - et les XXXX XX XX XX, XXXX XXX XXX, XX XX XX XX XX etc
	reg_tel_fax = '(0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4})'
    # pour un numero rcs (siren)
	reg_rcs = '(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)'
    # pour un taux TVA avec le symbole %
	reg_taux = 'TVA [^\d]*(\d{2}([,\.]\d*)?[ ]?%)'
    # pour un montant sans symbole
	reg_montant = '((\d| \d)+([,\.](\d| \d)+)?)'
    # pour une adresse
    # ne récupère pas les adresse du style F-75009
	reg_adress = '(\d*( ?\w+ ?)+[ \n]*\d{5} [^\n]{2,})'
	# pour le numero , nom et type de rue
	reg_rue = '(\d*( ?\w+ ?)+)\s'
	# pour le code postal (5 chiffres)
	reg_cp = '(\d{5} [^\n]{2,})'
    # pour un nom
	reg_nom = ''
    # pour le type d'une entreprise/société
	reg_type_soc = ''
    # pour une date
	reg_date = '(\d{2}[/\. -](\d{2}|\w+)[ /\.-]\d{2,4})'
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

