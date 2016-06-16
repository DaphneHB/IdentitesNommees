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
    """
    # Caractère représentant un saut de ligne selon la configuration fichier choisie
    caract_saut = r'<br>'
    # Regexp static pour différencier simplement les champs
    # pour un numero de téléphone ou de fax
    # accepte les séparateurs . espace et - et les XXXX XX XX XX, XXXX XXX XXX, XX XX XX XX XX etc
    reg_tel_fax = r'(0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4})'
    # pour un numero rcs (siren)
    reg_rcs = r'(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)'
    # pour un taux TVA avec le symbole %
    reg_tauxTVA = r'(TVA [^\d]*(\d{2}([,\.]\d*)?[ ]?%))'
    # pour n'importe quel taux
    reg_taux = r'([^\d]*(\d{2}([,\.]\d*)?[ ]?%)'
    # pour un montant sans symbole
    reg_montant = r'(\d+([,\. -]?\d+)*( \w+)?)'
    # pour une adresse
    # ne récupère pas les adresse du style F-75009
    reg_adress = r'(\d{,4} ?(\w+\'?-? ?)+[ %s]?\d{5} [a-zA-Z -]{2,})' % (caract_saut, )
    # pour le numero , nom et type de rue
    reg_rue = r'(\d{,4}( ?\w+-? ?)+)'
    # pour le code postal (5 chiffres)
    reg_cp = r'(\d{5} [a-zA-Z -]{2,})'
    # pour le type d'une entreprise/société
    reg_type_soc = r'(\w* \w*[A-Z]\w+ .* capital \w+[ -]? \d+([,\. -]?\d+)*( \w+)?)'
    # pour une date
    reg_date = r'(\d{1,2}[/\. -](\d{1,2}|[A-Za-z]+)[ /\.-]\d{4})'
    # pour une description/un titre/un nom
    reg_descr = r'^.*'
    # représente un numero identifiant récupéré sur la facture
    reg_num = r'([Nn] ?[u°]\w* ?[ \.-]?(\d[ \.-]?)+[ \B])'
    # le numéro de tva de l'entreprise
    reg_numTva = r'((TVA )?[Nn] ?[u°]\w* .* FR[ \.-]?(\d[ \.-]?){11})'


    def __init__ (self, type_extension, filename=None) :
    	if type_extension == "html" :
    		self.caract_saut = "<br>"
    	elif type_extension == "xml" :
    		self.caract_saut = "\n"
    	elif type_extension == "txt" or type_extension == "text" :
    		self.caract_saut = "\n"
    	else :
    		self.caract_saut = "\n"
    	self.filename = filename
    	
    def isName (self, name) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le nom
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isTypeInc (self, type_entreprise) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le type de l'entreprise
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
     
    def isRCS (self, rcs) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le numéro RCS
    	si oui, renvoie la partie de la string correspondant
    	si non, retourne False
    	"""
    	recherche = re.search(Reg_Finder.reg_rcs,rcs)
    	if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isAddress (self, adresse) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir l'adresse
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isTelFax (self, tel_fax, isTel=True) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le tel ou le fax
    	isTel is True si la probabilité qu'il s'agisse du tel est plus grande que la probabilité qu'il s'agisse du fax
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isTVA (self, tva) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le numéro tva
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()

    def isTitre (self, titre) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le titre de la facture
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isNumFacture (self, numero) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le numero de la facture
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isDate (self, date) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir la date de la facture
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def arePrestations (self, prests) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir les descriptions des prestations contenues dans la facture
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
     prests est une simple string, renvoie une liste de 'prestations extraites'
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()

    def isTVA (self, tva) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le montant de la tva
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isTauxTVA (self, tauxTva) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le taux tva
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isMontant (self, montant) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le montant HT
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     type_entreprise = type_entreprise.decode("utf-8","ignore")
     recherche = re.search(Reg_Finder.reg_type_soc,type_entreprise)
     if recherche is None :
    		return False
    	else :
    		return recherche.group()
    
    def isHT (self, ht) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le montant HT
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
     pass
 
    def isTTC (self, ttc) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir le montant TTC
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
    	pass
    
    def isOthersTax (self, autres) :
    	"""
    	Vérifie et retourne si ce champ peut être ou contenir d'autres taxes sur le total de la facture
    	si oui, renvoie la partie de la string correspondant
	si non, retourne False
    	"""
    	pass

