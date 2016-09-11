#!/usr/bin/python27
#coding: utf-8

import os
import re
import time
import sys

try: from lxml import html
except: os.system('pip install lxml==3.4.2')

try: import requests
except: os.system('pip install requests')

from requests import ConnectionError

# DEFINIÇÕES - FUNÇÕES
def href_replaced(href):
	for r in href:
		replaced.append(r)

def replace_id_link(replaced):
	for d in range(3,len(replaced)):
		hrefs.append(re.sub('[^0-9]', "", replaced[d] ))

def showSerials(hrefs, link):
	date = ''
	recent = ''
	print("")

	if not link:
		print("[ - ] Nada foi encontrado!")
		sys.exit()

	for i in range(3,len(hrefs),3):
		print ("["+link[i]+"] - ["+link[i+1]+"] - ["+link[i+2]+"] = ID: ["+hrefs[i-3]+"]")

		if not date:
			date = link[i+1]
			recent = (link[i]+" - "+link[i+1]+" - "+link[i+2]+" = ID: "+hrefs[i-3])
		else:
			if link[i+1] > date:
				date = link[i+1]
				recent = (link[i]+" - "+link[i+1]+" - "+link[i+2]+" = ID: "+hrefs[i-3])

	print("\n--------------------------------------")
	print("[ ++ ] Serial mais recente: "+str(recent))
	print("--------------------------------------")



#MAIN
if __name__ == '__main__':
	print ("\n[ * ] SERIALS FINDER v.05\n")

	url = 'http://www.serials.ws'
	replaced = []
	hrefs = []


	search = raw_input("Procurar por: ")
	http = requests.get(url+'?chto='+search)
	response = http.content
	h = html.fromstring(response)
	link = [ c.text_content() for c in h.xpath("//table[7]/tr/td") ]
	href = [ a.get('href') for a in h.xpath("//table[7]/tr/td/a") ]
	href_replaced(href)
	replace_id_link(replaced)
	showSerials(hrefs, link)

	code = raw_input("\nColoque o ID do programa: ")
	if not "Sorry" in response:

		try:
			request = requests.get(url+"/d.php?n="+code, proxies={ 'http':'47.88.189.216:3128' }, timeout=5)
			source = html.fromstring(request.content)
			getSerial = source.xpath("//textarea/text()")
			print ("\n------------------------------------------")
			print ("Serial: "+str(getSerial))
			print ("------------------------------------------")

		except ConnectionError:
			print("[-] Falha na conexao! Tente novamente.")

		except ReadTimeout:
			print("[-] Falha na conexao! Tente novamente.")

	else:
		print("[-] Proxy queimado! Tente outro.")