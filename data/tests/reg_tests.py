# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

rcs1 = "RCS PARIS B 582028833"
rcs2 = "Paris 356 000 000 RCS"
rcs3 = "au RCS de Paris B. de n°423 093 459"
not_rcs2 = "TVA FR 81 423 093 459"
not_rcs1 = "3 8000 000 000 €"

import re


reg_rcs = '([0-9]{3}){3}'

compiler_rcs = re.compile(reg_rcs)
rcs = rcs3
print "\nRCS\n"
print re.findall('(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)',rcs, re.I )
print re.search('(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)',rcs, re.I ).group()

print "\nTel"
reg_tel = ' ?(0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4}) ?'
tel = '0224 55 56 57'
print re.findall(reg_tel,tel)
print re.search('0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4}', '0224 55 55 55').group()

print "\nTaux\n"
reg_to = 'TVA [^\d]*(\d{2}([,\.]\d*)?[ ]?%)'
str_to = 'TVA 20.00 %'
ret_to_fall = re.findall(reg_to,str_to,re.I)
ret_to = re.search(reg_to,str_to,re.I)
print ret_to
print ret_to_fall
print ret_to.group()

print "\nDate\n"
reg_dat = '(\d{2}[/\. -](\d{2}|\w+)[ /\.-]\d{2,4})'
str_dat = 'du 21 Mars 2013'
ret_dat_fall = re.findall(reg_dat,str_dat,re.I)
ret_dat = re.search(reg_dat,str_dat,re.I)
print ret_dat
print ret_dat_fall
print ret_dat.group()

print "\nMontant\n"
reg_montant = '((\d| \d)+([,\.](\d| \d)+)?)'
str_montant = '3 8000 000 000 €'
ret_montant_fall = re.findall(reg_montant,str_montant,re.I)
ret_montant = re.search(reg_montant,str_montant,re.I)
print ret_montant
print ret_montant_fall
print ret_montant.group()

print "\nAdresse\n"
reg_rue = '(\d*( ?\w+ ?)+)\s'
reg_cp = '(\d{5} [^\n]{2,})'
reg_adresse = '(\d*( ?\w+ ?)+[ \n]*\d{5} [^\n]{2,})'
str_adresse = '302 rue de Charenton 75012 Paris'
ret_adresse_fall = re.findall(reg_adresse,str_adresse,re.I)
ret_adresse = re.search(reg_adresse,str_adresse,re.I)
print ret_adresse
print ret_adresse_fall
print ret_adresse.group()

print "\nDescr\n"
reg_descr = '(^[^\n]+)'
str_descr = 'Abonnements, forfaits et options<br>Communications<br>Services ponctuels ou occasionnels'
ret_descr_fall = re.findall(reg_descr,str_descr,re.I)
ret_descr = re.search(reg_descr,str_descr,re.I)
print ret_descr
print ret_descr_fall
print ret_descr.group()

print "\nNom\n"
reg_nom = '(\d*( ?\w+ ?)+[ \n]*\d{5} [^\n]{2,})'
str_nom = '302 rue de Charenton F-75012 Paris'
ret_nom_fall = re.findall(reg_nom,str_nom,re.I)
ret_nom = re.search(reg_nom,str_nom,re.I)
print ret_nom
print ret_nom_fall
print ret_nom.group()

print "\nSociété\n"
reg_societe = '(\d*( ?\w+ ?)+[ \n]*\d{5} [^\n]{2,})'
str_societe = '302 rue de Charenton F-75012 Paris'
ret_societe_fall = re.findall(reg_societe,str_societe,re.I)
ret_societe = re.search(reg_societe,str_societe,re.I)
print ret_societe
print ret_societe_fall
print ret_societe.group()
