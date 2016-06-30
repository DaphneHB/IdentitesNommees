# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:22 2016

@author: daphnehb
"""

import math
import collections

def entropie(vect) :
    compt = collections.Counter(vect)

    for xi in


# data : tableau ( films , features ) , id2titles :
# dictionnaire id -> titre film , fields : id feature -> nom
[ data , id2titles , fields ]= cPickle . load ( file (" imdb_extrait .pkl") )
# la derniere colonne est le vote
datax = data [: ,:32]
datay = np . array ([1 if x [33] >6.5 else -1 for x in data ])