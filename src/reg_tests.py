# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

rcs1 = "RCS PARIS B 582028833"
rcs2 = "Paris 356 000 000 RCS"
rcs3 = "au RCS de Paris B. de n°423 093 459"
num_tva = "TVA FR 81 423 093 459"
montant = "3 8000 000 000 €"

import re
caract_saut = '<br>'
bloc_text = "Free SAS au capital de 3.441.812 Euros − B 421 938 861 Paris RCS − Siège social: 8 rue de la Ville l’Evêque 75008 Paris − N° de TVA intra communautaire: FR 604 219 388 61".decode('utf-8',"ignore")


reg_rcs = '([0-9]{3}){3}'

compiler_rcs = re.compile(reg_rcs)
rcs = bloc_text
print "\nRCS\n"
print re.findall('(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)',rcs, re.I )
print re.search('(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)',rcs, re.I ).group()

print "\nTel"
reg_tel = ' ?(0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4}) ?'
tel = '0147278540'
print re.findall(reg_tel,tel)
print re.search('0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4}', '0147278540').group()

print "\nTaux\n"
reg_to = 'TVA [^\d]*(\d{2}([,\.]\d*)?[ ]?%)'
str_to = 'TVA 20.00 %'
ret_to_fall = re.findall(reg_to,str_to,re.I)
ret_to = re.search(reg_to,str_to,re.I)
print ret_to
print ret_to_fall
print ret_to.group()

print "\nNumTVA\n"
reg_numTva = '((TVA )?[Nn] ?[u°]\w* .* FR[ \.-]?(\d[ \.-]?){11})'
str_numTva = bloc_text
ret_numTva_fall = re.findall(reg_numTva,str_numTva)
ret_numTva = re.search(reg_numTva,str_numTva,re.I)
print ret_numTva
print ret_numTva_fall
print ret_numTva.group()

print "\nNum\n"
reg_numFact = '([Nn] ?[u°]\w* ?[ \.-]?(\d[ \.-]?)+[ \B])'
str_numFact = 'Facture n°599831845 du 02 Janvier 2016'.decode('utf-8','ignore')
ret_numFact_fall = re.findall(reg_numFact,str_numFact)
ret_numFact = re.search(reg_numFact,str_numFact,re.I)
print ret_numFact
print ret_numFact_fall
print ret_numFact.group()

print "\nDate\n"
reg_dat = '(\d{1,2}[/\. -](\d{1,2}|[A-Za-z]+)[ /\.-]\d{4})'
str_dat = 'Facture n°599831845 du 02 Janvier 2016'
ret_dat_fall = re.findall(reg_dat,str_dat,re.I)
ret_dat = re.search(reg_dat,str_dat,re.I)
print ret_dat
print ret_dat_fall
print ret_dat.group()

print "\nMontant\n"
reg_montant = '(\d+([,\. -]?\d+)*( \w+)?)'
str_montant = bloc_text
ret_montant_fall = re.findall(reg_montant,str_montant,re.I)
ret_montant = re.search(reg_montant,str_montant,re.I)
print ret_montant
print ret_montant_fall
print ret_montant.group()

# TODO ,pb 
print "\nAdresse\n"
reg_rue = '(\d{,4}( ?\w+-? ?)+)'
reg_cp = '(\d{5} [a-zA-Z -]{2,})'
reg_adresse = '(\d{,4} ?(\w+\'?-? ?)+[ %s]?\d{5} [a-zA-Z -]{2,})' % (caract_saut, )
str_adresse = bloc_text
ret_adresse_fall = re.findall(reg_rue,str_adresse,re.I)
ret_adresse = re.search(reg_rue,str_adresse,re.I)
print ret_adresse
print ret_adresse_fall
print ret_adresse.group()

print "\nDescr\n"
reg_descr = '(^[^%s]+)' % (caract_saut, )
str_descr = 'Abonnements, forfaits et options%sCommunications%sServices ponctuels ou occasionnels%s' % (caract_saut, caract_saut, caract_saut)
ret_descr_fall = re.findall(reg_descr,str_descr,re.I)
ret_descr = re.search(reg_descr,str_descr,re.I)
print ret_descr
print ret_descr_fall
print ret_descr.group()

print "\nSociété\n"
reg_societe = '(\w* \w*[A-Z]\w+ .* capital \w+[ -]? \d+([,\. -]?\d+)*( \w+)?)'
str_societe = bloc_text
ret_societe_fall = re.findall(reg_societe,str_societe,re.I)
ret_societe = re.search(reg_societe,str_societe,re.I)
print ret_societe
print ret_societe_fall
print ret_societe.group()



print "************************************"
"""
Toujours décoder le format de la string en entré en décodant la sting string.decode("utf-8", "ignore") ( avant chaque test)
Attention decodage une fois seulement sinon UnicodeError
"""
import reg_search as rx

rClass = rx.Reg_Finder("html")

print rClass.isRCS(bloc_text)
