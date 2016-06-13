# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:19 2016

@author: daphnehb
"""
import os, stat
import exceptions as exc

def recup_basedirname_extension(path):
    """
    Retourne un tuple (triplet) : (basename, dirname, ectension) de l'arborescence de fichier entrée
    avec le dirname sans extension
    """
    path = os.path.realpath(path)
    path,extension = os.path.splitext(path)
    basename = os.path.basename(path)
    dirname = os.path.dirname(path)
    return (basename,dirname,extension)

def verify_path(path, last_dir=False, file_too = False):
    """
    Permet de vérifier l'arborescence entrée/choisie
    Vérifie que les dossiers parents existent
    Si file_too est à vrai, vérifie aussi que le fichier d'arrivée existe
    (utile pour l'existence de fichier d'entrée)
    Si un dossier n'existe pas, on le crée
    Si file_too = True et que le fichier n'existe pas, on retourne une erreur
    """
    # on récupère les éléments du chemin
    basen,dirn,ext = recup_basedirname_extension(path)
    # dans le cas où l'arborescence est uniquement une arborescence de dossier
    if os.path.isdir(basen) or last_dir:
        dirn = os .path.join(dirn,basen)
        basen = ""
    # on crée les dossiers s'ils n'existent pas
    if not os.path.exists(dirn):
        try:
            original_umask = os.umask(0)
            os.makedirs(dirn,0777)
        finally:
            os.umask(original_umask)
    if file_too:
        # vérification de l'existence du fichier
        if basen!="" and (not os.path.exists(path) or not os.path.isfile(path)):
            return 0
            #raise exc.FileNotExistingException(dirn,'{}{}'.format(basen,ext))
    return 1

def recup_destination(dest_path,extension):
    """
    Renvoie le chemin absolu de la destination selon le chemin demandé et avec comme dossier final un dossier de l'extension
    Crée aussi le dossier <dest_path>/<extension> s'il n'existe pas
    """
    dest_path = os.path.join(dest_path,extension)
    # on vérifie que le chemin demandé pour le fichier de sortie existe, si non on le crée
    verify_path(dest_path,last_dir=True)
    return dest_path
