#!/usr/bin/env python3
#coding: utf-8

'''
	biblioteca sem o uso de imports para iniciantes em programação a fim de estudos de código
'''

class medidasDispersao():

	def __init__(self, values):
		self.values = values

	def media(self):
		try:
			var_media = sum(self.values)/len(self.values)
			return float("{:.4}".format(var_media))
		except TypeError:
			print("TypeError: Insira uma lista como argumento")
			exit()

	def moda(self):
		return max(set(self.values), key=self.values.count)
	
	def desvio(self):
		mediaAtm = self.media()
		desvio = [ (d-mediaAtm) for d in self.values ]
		return desvio

	def variancia(self):
		desvioVr = self.desvio()
		variancia = [ pow(v,2) for v in desvioVr ]
		divisaoValues = sum(variancia)/(len(variancia)-1)
		return float("{:.4}".format(divisaoValues))

	def desvioPadrao(self):
		varianciaDv = self.variancia()
		raizQuadrada = ( varianciaDv ** (1/2.0) )
		return float("{:.4}".format(raizQuadrada))