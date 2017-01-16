#!/usr/bin/python
#coding: utf-8

__version__ = '2.0'

from bs4 import BeautifulSoup
import requests
import re
import sys
import os

def banner():
	print '''
		──────▄▀▄─────▄▀▄
		─────▄█░░▀▀▀▀▀░░█▄
		─▄▄──█░░░░░░░░░░░█──▄▄
		█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█

	     SERIALS FINDER 2.0 by asa/n0dz
	'''

# Limpeza de tela em diferentes sistemas
def clear():
	os.system("clear || cls")

# Modo de uso
def usage():
	clear()
	banner()
	print ("python %s %s"% (sys.argv[0], "\"product\""))
	sys.exit()

# Extrai o id do produto
def getID(link):
	for d in range(0,len(link)):
		return re.sub('[^0-9]', "", link)

# Mostra a lista de produtos encontrados
def getOptions(link, text, date, percent, searchto):
	if searchto in text.lower():
		print ( getID(link)+": "+text+" - "+date+" - "+percent )
	else:
		return None

# Função principal
def main():
	clear()
	banner()

	try: searchto = sys.argv[1]
	except: usage()

	try:
		url = ('http://www.serials.ws/')
		b = BeautifulSoup(requests.get(url+'?chto='+searchto).content, 'lxml')
		table = [ i for i in b.find_all('table') ]
		response = [ r for r in table[4].find_all('td') ]
		for i in range(3,len(response)-1,3):
			link = response[i].find('a').get('href')
			text = response[i].get_text()
			date = response[i+1].get_text()
			percent = response[i+2].get_text()
			getOptions(link, text, date, percent, searchto)

		id_product = raw_input("\n[+] Paste Product ID: ")
		clear()
		banner()
		s = BeautifulSoup(requests.get(url+'d.php?n='+id_product).content, 'lxml')
		text_area = s.find('textarea').get_text()
		print "[+] Result(s): "+text_area+"\n"

	except KeyboardInterrupt:
		print '\n - KeyboardInterrupt'
		sys.exit()

if __name__ == '__main__':
	main()
