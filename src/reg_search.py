# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:31 2016

@author: daphnehb
"""

import re


class Regex_Tools:
    """
    Représente l'analyseur de string à l'aide de regexp
    Utilisant re.search(reg,str,re.I).group() pour récupérer la plus grosse parcelle
    """

    def __init__(self):
        pass

    # Caractère représentant un saut de ligne selon la configuration fichier choisie
    caract_saut = r'\n'
    # Regexp static pour différencier simplement les champs
    # pour un numero de téléphone ou de fax
    # accepte les séparateurs . espace et - et les XXXX XX XX XX, XXXX XXX XXX, XX XX XX XX XX etc
    reg_tel_fax = r'(0[0-9]{1,3}([ \.-]?[0-9]{2,3}){2,4})'
    # pour un numero rcs (siren)
    reg_rcs = r'(RCS ?( .*)?\d{3} ?\d{3} ?\d{3})|(\d{3} ?\d{3} ?\d{3}( .* )? ?RCS)'
    # pour un taux TVA avec le symbole %
    reg_tauxTVA = r'(TVA [^\d]*\d{1,4}[,\.]?\d*[ ]?%)'
    # pour n'importe quel taux
    reg_taux = r'(\d{1,4}[,\.]?\d*[ ]?%)'
    # pour un montant sans symbole
    reg_montant = r'(\d+([,\. -]?\d+)*( \w+)?)'
    # pour une adresse
    # ne récupère pas les adresse du style F-75009
    reg_adress = r'(\d{,4} ?[\w+\' -]+[, %s]*\d{5} [a-zA-Z -]{2,})' % (caract_saut,)
    # pour le numero , nom et type de rue
    reg_rue = r'(\d{,4} ?[\w+\' -]+)'
    # pour le code postal (5 chiffres)
    reg_cp = r'(\d{5} [a-zA-Z -]{2,})'
    # pour le type d'une entreprise/société
    reg_type_soc = r'(\w* \w*[A-Z]\w+ .* capital \w+[ -]? \d+([,\. -]?\d+)*( \w+)?)'
    # pour une date
    reg_date = r'(\d{1,2}[/\. -](\d{1,2}|[A-Za-z]+)[ /\.-]\d{4})'
    # pour une description/un titre/un nom
    reg_descr = r'^[A-Z].*'
    # représente un numero identifiant récupéré sur la facture
    reg_num = r'([Nn] ?[u°]\w* ?[ \.-]?(\d[ \.-]?)+[ \B])'
    # le numéro de tva de l'entreprise
    reg_numTva = r'(FR[ \.-]?(\d[ \.-]?){11})'  # en début : (TVA )?[Nn] ?[u°]\w* .*

    # liste de toutes les regexp à appliquer
    # détermine l'ordre des flags dans le vecteur des features
    reg_flags = {reg_tel_fax, reg_rcs,
                 reg_tauxTVA, reg_taux,
                 reg_montant, reg_adress,
                 reg_type_soc, reg_date,
                 reg_descr, reg_num,
                 reg_numTva}

    def recup_flag_test(self, flag, bloc_text):
        reg_flag_test = {Regex_Tools.reg_tel_fax: self.isTelFax,
                         Regex_Tools.reg_rcs: self.isRCS,
                         Regex_Tools.reg_tauxTVA: self.isTauxTVA,
                         Regex_Tools.reg_taux: self.isTaux,
                         Regex_Tools.reg_montant: self.isMontant,
                         Regex_Tools.reg_adress: self.isAddress,
                         Regex_Tools.reg_type_soc: self.isTypeInc,
                         Regex_Tools.reg_descr: self.isDescription,
                         Regex_Tools.reg_num: self.isNumFacture,
                         Regex_Tools.reg_numTva: self.isNumTVA,
                         Regex_Tools.reg_date: self.isDate}
        if not reg_flag_test.has_key(flag):
            return None
        else:
            return reg_flag_test[flag](bloc_text)

    def apply_flags(self, bloc_text):
        """
        Pour chaque flag de regex possible dans la liste reg_flags,
        Test sur le bloc de text et récupération des flags actifs et inactifs en un tuple
        :param bloc_text: bloc de texte extrait du html sur lequel appliquer les regex
        :return: tuple (_,_,_,_) présentant pour chaque flag 0 ou 1 le résultat de la regexp correspondante
        """
        resultat_flags = []
        # pour chaque flag envisageable
        for flag in Regex_Tools.reg_flags:
            # on l'applique au bloc de texte
            res, _ = self.recup_flag_test(flag,bloc_text)
            # s'il y a eu un soucis avec les flags
            if res is None:
                continue
            # on enregistre le résultat dans resultat_flags
            resultat_flags.append(res)
        return tuple(resultat_flags)

    def isDescription(self, descrp):
        """
        Vérifie et retourne si ce champ peut être ou contenir le nom, une description ou un titre
        si oui, renvoie 1 et la partie de la string correspondant
        si non, retourne 0 et None
        """

        recherche = re.search(Regex_Tools.reg_descr, descrp)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isTypeInc(self, type_entreprise):
        """
        Vérifie et retourne si ce champ peut être ou contenir le type de l'entreprise
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_type_soc, type_entreprise)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isRCS(self, rcs):
        """
        Vérifie et retourne si ce champ peut être ou contenir le numéro RCS
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_rcs, rcs)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isAddress(self, adresse):
        """
        Vérifie et retourne si ce champ peut être ou contenir l'adresse
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_adress, adresse)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isTelFax(self, tel_fax, isTel=True):
        """
        Vérifie et retourne si ce champ peut être ou contenir le tel ou le fax
        isTel is True si la probabilité qu'il s'agisse du tel est plus grande que la probabilité qu'il s'agisse du fax
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_tel_fax, tel_fax)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isNumTVA(self, tva):
        """
        Vérifie et retourne si ce champ peut être ou contenir le numéro tva
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_numTva, tva)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isNumFacture(self, numero):
        """
        Vérifie et retourne si ce champ peut être ou contenir le numero de la facture,
        c'est-à-dire un numéro sans spécificité explicite
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_num, numero)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isDate(self, date):
        """
        Vérifie et retourne si ce champ peut être ou contenir la date de la facture
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_date, date)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isTauxTVA(self, tauxTva):
        """
        Vérifie et retourne si ce champ peut être ou contenir le taux tva
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_tauxTVA, tauxTva)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isTaux(self, taux):
        """
        Vérifie et retourne si ce champ peut être ou contenir un taux
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_taux, taux)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()

    def isMontant(self, montant):
        """
        Vérifie et retourne si ce champ peut être ou contenir le montant HT
        si oui, renvoie 1
        si non, retourne 0
        """
        recherche = re.search(Regex_Tools.reg_montant, montant)
        if recherche is None:
            return 0, None
        else:
            return 1, recherche.group()
