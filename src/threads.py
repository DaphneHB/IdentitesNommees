# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:33 2016

@author: daphnehb
"""

from threading import Thread
import time


class Sous_Traitance(Thread) :
	"""
	Classe de sous-traitement d'une tâche telle que l'exécution d'une fonction pouvant être longue
	"""
	def __init__(self, funtion_to_call, args=None, start_time=-1, fichier_import=None) :
		Thread.__init__(self)
		# nom de la fontion
		self.funtion_to_call = funtion_to_call
		# arguments à mettre en paramètre de la fonction
		self.funtion_args = args
		# fichier à importer pour pouvoir appeler la fonction (string)
		self.fichier_import = fichier_import
		# start_time : temps après lequel le programme doit lancer la fonction
		# 0 -> immédiat; -1 -> on le rappelle
		self.start_time = start_time
		self.initTime()

	def initTime(self) :
		if self.start_time==-1 :
			return
		else :
			time.sleep(self.start_time)
			self.start()

	def run(self) :

		if not self.fichier_import is None :
			self.module = __import__(self.fichier_import)
			
		function = self.funtion_to_call

		try :
			if self.funtion_args is None :
				function()
			else : # cas où il y a des arguments
				if type(self.funtion_args) is list \
				or type(self.funtion_args) is tuple :

					function(*self.funtion_args)
				else :
					function(self.funtion_args)
		except Exception as e:
			print "Excepted threads sous-traitant : ",e
			pass
			# TODO gérer l'erreur qd la fct est mal appelée