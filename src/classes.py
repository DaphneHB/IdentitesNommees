# coding=utf-8
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17 :04 2016

@author : daphnehb
"""


class Facture:
    """
	Représente une facture récupérée depuis un fichier pdf
	Modèle basé sur les attentes contenues dans le cahier des charges
	"""

    def __init__ ( self, file , simplifiee=True):
        # l'expéditeur de la facture  (objet Expediteur)
        self.expediteur = Expediteur ( )
        # le destinataire de la facture  (objet Destinataire)
        self.destinataire = Destinataire ( )
        # le montant total HT,  le taux total de tva,  le montant total de TVA
        # le total des autres taxes potentielles,  le montant total TTC
        # le moyen de paiement  (objet InfoFacture)
        self.infosFacture = InfosFacture ( )
        self.prestations = InfosPrestations(simplifiee=simplifiee)

class InfosFacture:
    """
	Représente les informations globales contenues dans la facture
	-> montants totaux  (HT,  TVA et TTC),  taux total TVA,  montant total autres taxes,  moyens de paiement
	"""

    def __init__ ( self ):
        # le titre facultatif de la facture  (par defaut "Facture <nom de l'expéditeur>")  (string)
        self.titre = None  # implied
        # le numero de la facture  (string)
        self.numero = None  # required
        # la date de la facture - plusieurs formats possibles  (string)
        self.date = None  # required
        # montant total brut - hors taxes  (string,  pour avoir le symbole)
        self.montantHT = None  # required
        # taux de la tva total  (string)
        self.tauxTVA = None  # required
        # montant total de la tva  (string)
        self.montantTVA = None  # required
        # montant total des autres taxes  (string)
        self.autres_taxes = None  # implied
        # montant total de la facture - toutes taxes comprises  (string)
        self.montantTTC = None  # required

    def isTitre ( self, titre ):
        """
        Vérifie si ce champ peut être le titre de la facture
        si oui,  actualise le champ
        """
        pass

    def isNumFacture ( self, numero ):
        """
        Vérifie si ce champ peut être le numero de la facture
        si oui,  actualise le champ
        """
        pass

    def isDate ( self, date ):
        """
        Vérifie si ce champ peut être la date de la facture
        si oui,  actualise le nom
        """
        pass

    def isTVA ( self, tva ):
        """
		Vérifie si ce champ peut être le montant de la tva
		si oui,  actualise le champ
		"""
        pass

    def isTauxTVA ( self, tauxTva ):
        """
		Vérifie si ce champ peut être le taux tva
		si oui,  actualise le champ
		"""
        pass

    def isHT ( self, ht ):
        """
		Vérifie si ce champ peut être le montant HT
		si oui,  actualise le champ
		"""
        pass

    def isTTC ( self, ttc ):
        """
		Vérifie si ce champ peut être le montant TTC
		si oui,  actualise le champ
		"""
        pass

    def isOthersTax ( self, autres ):
        """
		Vérifie si ce champ peut être d'autres taxes sur le total de la facture
		si oui,  actualise le champ
		"""
        pass


class Expediteur:
    """
	Représente l'expéditeur de la facture
	"""

    def __init__ ( self ):
        # le nom prenom du destinataire  (string)
        self.nom = None  # required
        # le type d'entreprise et son capital  (string)
        self.type_entreprise = None  # implied
        # le numéro et ville RCS  (string)
        self.RCS = None  # required
        # le numéro SIREN  (string)
        self.SIREN = None  # implied
        # l'adresse  (num,  rue,  cp,  ville) du destinataire  (string)
        self.adresse = None  # required
        # le numéro de téléphone du destinataire  (et son fax?)  (string)
        self.tel_fax = None  # implied
        # le numéro TVA du destinataire - FRXX<RCS> (XXXXX)?  (string)
        self.num_TVA = None  # required

    def isName ( self, name ):
        """
		Vérifie si ce champ peut être le nom
		si oui,  actualise le nom
		"""
        pass

    def isTypeInc ( self, type_entreprise ):
        """
		Vérifie si ce champ peut être le type de l'entreprise
		si oui,  actualise le type
		"""
        pass

    def isRCS ( self, rcs ):
        """
		Vérifie si ce champ peut être le numéro RCS
		si oui,  actualise le champ
		"""
        pass

    def isSIREN ( self, siren ):
        """
		Vérifie si ce champ peut être le numéro SIREN
		si oui,  actualise le champ
		"""
        pass

    def isAddress ( self, adresse ):
        """
		Vérifie si ce champ peut être l'adresse
		si oui,  actualise le champ
		"""
        pass

    def isTelFax ( self, tel_fax, isTel=True ):
        """
		Vérifie si ce champ peut être le tel ou le fax
		isTel is True si la probabilité qu'il s'agisse du tel est plus grande que la probabilité qu'il s'agisse du fax
		si oui,  actualise le champ
		"""
        pass

    def isTVA ( self, tva ):
        """
		Vérifie si ce champ peut être le numéro tva
		si oui,  actualise le champ
		"""
        pass


class Destinataire:
    """
	Représente le destinataire de la facture
	"""

    def __init__ ( self ):
        # le nom prenom du destinataire  (string)
        self.nom = None  # required
        # le type d'entreprise et son capital  (string)
        self.type_entreprise = None  # implied
        # le numéro et ville RCS  (string)
        self.RCS = None  # implied
        # l'adresse  (num,  rue,  cp,  ville) du destinataire  (string)
        self.adresse = None  # required
        # le numéro de téléphone du destinataire  (et son fax?)  (string)
        self.tel_fax = None  # implied
        # le numéro TVA du destinataire - FRXX<RCS> (XXXXX)?  (string)
        self.num_TVA = None  # implied

    def isName ( self, name ):
        """
		Vérifie si ce champ peut être le nom
		si oui,  actualise le nom
		"""
        pass

    def isTypeInc ( self, type_entreprise ):
        """
		Vérifie si ce champ peut être le type de l'entreprise
		si oui,  actualise le type
		"""
        pass

    def isAddress ( self, adresse ):
        """
		Vérifie si ce champ peut être l'adresse
		si oui,  actualise le champ
		"""
        pass

    def isTelFax ( self, tel_fax, isTel=True ):
        """
		Vérifie si ce champ peut être le tel ou le fax
		isTel is True si la probabilité qu'il s'agisse du tel est plus grande que la probabilité qu'il s'agisse du fax
		si oui,  actualise le champ
		"""
        pass

    def isTVA ( self, tva ):
        """
		Vérifie si ce champ peut être le numéro tva
		si oui,  actualise le champ
		"""
        pass


class InfosPrestations:
    """
	Représente toutes les prestations de la facture,  ie achats/ventes contenu sur la facture sans leurs montants propres
	"""
    self.prestations = list ( )

    def __init__ ( self, simplifiee=True ):
        self.simplifiee = simplifiee
        # nature des prestations,  leurs descriptions  (list string)
        # la liste des prestations contenues dans la facture
        # simplifiee is False : (list<objet prestation>)
        # simplifiee is True : (list<string>)
        self.nature = list()  # required

    def isNature ( self, nature ):
        """
		Vérifie si ce champ peut être la description de la prestation
		si oui,  ajoute cette nature à la liste des prestations déjà connues
		"""
        pass

    def addPrestation(self, **kwargs):
        """
        Ajoute une prestation à la liste tenant compte de sa simplification ou nom
        Et de sa description, montants, taux ...
        :param kwargs:
        :return:
        """
        pass

class Prestation:
    """
	Représente une prestation,  ie un des achats/ventes contenu sur la facture
	"""

    def __init__ ( self ):
        # la nature de la prestation,  sa description  (string)
        self.nature = None  # required
        # montant brut de la prestation - hors taxes  (string,  pour avoir le symbole)
        self.montantHT = None  # implied
        # taux de la tva  (string)
        self.tauxTVA = None  # implied
        # montant de la tva pour cette prestation  (string)
        self.montantTVA = None  # implied
        # montant d'autres taxes  (string)
        self.autres_taxes = None  # implied
        # montant total - toutes taxes comprises  (string)
        self.montantTTC = None  # required

    def isNature ( self, nature ):
        """
		Vérifie si ce champ peut être la description de la prestation
		si oui,  actualise le champ
		"""
        pass

    def isHT ( self, ht ):
        """
		Vérifie si ce champ peut être le total HT
		si oui,  actualise le champ
		"""
        pass

    def isTauxTVA ( self, tauxTVA ):
        """
		Vérifie si ce champ peut être le taux tva pour cette prestation
		si oui,  actualise le champ
		"""
        pass

    def isTVA ( self, tva ):
        """
		Vérifie si ce champ peut être le montant tva pour cette prestation
		si oui,  actualise le champ
		"""
        pass

    def isOthersTax ( self, autres ):
        """
		Vérifie si ce champ peut être d'autres taxes incluses dans le montant final
		si oui,  actualise le champ
		"""
        pass

    def isTotal ( self, total ):
        """
		Vérifie si ce champ peut être le montant total TTC pour cette prestation
		si oui,  actualise le champ
		"""
        pass
