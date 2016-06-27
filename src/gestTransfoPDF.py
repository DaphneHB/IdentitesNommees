# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:01 2016

@author: daphnehb
"""

class BlockToVect :
    """
    Classe permettant de gérer les transformations PDF to HTML ou TXT ou XML
    (une méthode par tranfo possible)
    Les méthodes permettent de récupérer une liste de tuples associant à chaque bloc trouvé dans le texte un vecteur-tuple de descripteurs et d'informations
    """

    def __init__(self, filename):
        self.filename = filename
        # TODO gérer les erreurs de file

    def getText(self):
        """
        Récupère la string contenue du fichier filename correspondant à la facture dans un format lisible
        """
        # TODO gérer les erreurs de file
        with open(self.filename, "r") as myfile :
            text_recup = myfile.readlines()
        self.text_to_cut = text_recup


    def fromHtml(self):
        """
        Retourne une liste de tuple/vecteurs correspondant à l'application des descripteurs
        """
        if not self.filename.endwith("html") :
            # TODO raise NotHtmlFile(self.filename)
            pass

        pass
