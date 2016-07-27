# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:01 2016

@author: daphnehb
"""

import re
from reg_search import Regex_Tools


class BlockToVect:
    """
    Classe permettant de gérer les transformations PDF to HTML ou TXT ou XML
    (une méthode par tranfo possible)
    Les méthodes permettent de récupérer une liste de tuples associant à chaque bloc trouvé dans le texte un vecteur-tuple de descripteurs et d'informations
    Creation du vecteur (bloc_de_text, nb lignes ,x/left,y/top,width,height, reg_flags)
    """

    # Liste des regexp

    def __init__ ( self, filename ):
        self.filename = filename
        self.text_to_cut = ""
        # TODO gérer les erreurs de file
        self.getText ( )

    def getText ( self ):
        """
        Récupère la string contenue du fichier filename correspondant à la facture dans un format lisible
        """
        # TODO gérer les erreurs de file
        with open ( self.filename, "r" ) as myfile:
            text_recup = "".join ( myfile.readlines ( ) )
        self.text_to_cut = BlockToVect.decodage ( text_recup )
        # print 'Nom du fichier ',self.filename
        # print 'Contenu du fichier',text_recup

    @staticmethod
    def decodage ( string_to_decode ):
        # print "avant",string_to_decode
        # si le codec de la string n'est pas unicode on la decode
        try:  # TODO meilleure façon de gérer l'encodage ?
            string_to_decode = string_to_decode.decode ( "utf-8" )
        except UnicodeEncodeError:
            pass
        # print "apres",string_to_decode
        from unicodedata import normalize
        return normalize ( 'NFKD', string_to_decode ).encode ( 'ascii', 'ignore' )

    def fromHtml ( self ):
        """
        Retourne une liste de tuple/vecteurs correspondant à l'application des descripteurs
        """
        if not self.filename.endswith ( "html" ):
            # TODO raise NotHtmlFile(self.filename)
            pass
        # liste contenant les vecteurs représentatifs qui sera renvoyé en fin
        text_vecteurs = list ( )

        # on a notre propre outils de regex
        reg_tool = Regex_Tools ( )

        # on récupère la partie dans le body
        self.text_to_cut = re.findall ( r"<body.*?>(.+)</body>", self.text_to_cut, re.DOTALL | re.M )[0]
        print  self.text_to_cut
        # on découpe selon les div non-greedy en récupérant leur position
        # fct = lambda x : str(x[0])+str(x[1])
        # print "\n*****************\n".join(map(fct,re.findall(r"<div.*?(left:.+?)\">(.+?)</div>", self.text_to_cut, re.DOTALL | re.M)))
        txt_divs = re.findall ( r"<div.*?(left:.+?)\">(.+?)</div>", self.text_to_cut, re.DOTALL | re.M )
        # pour chaque div on récupère ses tailles et positions et contenu
        for div in txt_divs:
            # on vérifie s'il n'y a bien que 2 champs à traiter
            if len ( div ) != 2:
                continue
            # on récupère les champs à étudier
            infos = div[0]
            txt = div[1]
            print '***********'

            # tuple représentant cette div avec toutes ses caractéristiques
            div_tuple = tuple ( )
            # on retire toutes les balise span et br
            txt, nb_lignes = self.simplifierHtml ( txt )
            # si le texte obtenu est vide, on ne le considère pas
            if txt == "":
                continue
            # on ajoute le texte comme premier element du vecteur
            div_tuple = div_tuple + (txt, nb_lignes)
            # on recupere les infos de la div (position et taille)
            infos = self.get_div_infos ( infos )
            # on ajoute les infos au tuple
            div_tuple = div_tuple + infos
            # on récupère tous les flag pour toutes les regex
            regex_flags = reg_tool.apply_flags ( txt )
            # on ajoute les flags au tuple
            div_tuple = div_tuple + regex_flags
            print "--------------> ", div_tuple
            # on ajoute le tuple formé
            txt_divs.append ( div_tuple )

        return txt_divs

    def get_div_infos ( self, infos_div ):
        """
        Renvoie les informations de taille et de position de la div
        :param infos_div:
        :return:
        """
        # on récupère les informations en liste de nombres floatants
        nums = map ( float, re.findall ( r':(\d+[\.,]?\d*)px;', infos_div ) )
        """
        left_x = re.findall(r'left:(\d+[\.,]?\d*)px', infos_div)
        top_y = re.findall(r'top:(\d+[\.,]?\d*)px', infos_div)
        width = re.findall(r'width:(\d+[\.,]?\d*)px', infos_div)
        height = re.findall(r'height:(\d+[\.,]?\d*)px', infos_div)
        """
        return tuple ( nums )  # (left_x, top_y, width, height)

    def simplifierHtml ( self, txt ):
        """
        Simplifie le format du texte en entrée pour un texte html
        Remplacement des balises <br> par des \n (sauts de ligne)
        Remplacament des balises <span> par des \n (sauts de ligne)
        Comptage des lignes
        :param txt: texte à modifier et à analyser
        :return: texte modifié, nombre de lignes du texte
        """
        # text_res = re.sub(r'<br>','',txt)
        # on transforme n'importe quelle balise en rien
        text_res = re.sub ( r'<.+?>', '', txt )
        # on retire les sauts de lignes de début et de fin de bloc
        text_res = re.sub ( r'(^\n+|\n+$)', '', text_res )
        # on compte le nombre de lignes en séparant tout le texte par \n
        nb_lignes = len ( text_res.split ( "\n" ) )
        # print "SIMPLIFICATION (",nb_lignes," lignes) : ",text_res
        return text_res, nb_lignes


bl = BlockToVect ( "/home/innopolis/Documents/IdentitesNommees/data/html/air france.html" )

bl.fromHtml ( )

# print BlockToVect.decodage("La chêvre hébétée bêla sur un agneau de façon éphémère, où se croyait-elle ?")
