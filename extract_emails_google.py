#!/usr/bin/python
#coding: utf-8
#dork: site:.br +@ (hotmail|outlook|gmail) br ext:txt

import os
import mechanize
from bs4 import BeautifulSoup
import re
import urllib
import argparse
from random import randint
import platform

def banner():
	print '''
		──────▄▀▄─────▄▀▄
		─────▄█░░▀▀▀▀▀░░█▄
		─▄▄──█░░░░░░░░░░░█──▄▄
		█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█

	     EXTRACT EMAILS 1.0 by asa/n0dz
	'''

# Limpeza de tela em diferentes sistemas
def clear():
	system = (platform.system()).lower()
	if "linux" in system:
		os.system("clear")
	elif "win" in system:
		os.system("cls")

def main():
	clear()
	banner()
	parser = argparse.ArgumentParser(description='Extract emails')
	parser.add_argument('-d', '--dork', metavar='"INSERT DORK"')
	parser.add_argument('-m', '--mode', help='h/hour, d/day, w/week, m/month, y/year', default="0")
	args = parser.parse_args()
	if not args.dork:
		parser.print_help()
		exit()

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	next_page = 0
	print("\n[+] Searching in Google...")
	while True:
		src = br.open("https://www.google.com.br/search?q="+urllib.quote(args.dork)+"&tbs=qdr:%s&start=%s" % (args.mode[0],next_page) )
		bs = BeautifulSoup(src.get_data(), 'lxml')
		for i in bs.find_all('a'):
			if "/url?" in i.get('href') and not "webcache.googleusercontent.com" in i.get('href'):
				extract = re.findall(r"q=(.*\.txt)", i.get('href'))
				for link in extract:
					extract_emails(link, br)

		page = (raw_input("\n[*] Next page (Y/n)?: ")).lower()
		if page == "n":
			break
		else:
			next_page = next_page+10

def extract_emails(link, br):
	src = br.open(link)
	print ("[+] Extracting %s" % link)
	emails = re.findall(r"[a-zA-Z0-9_.\-]+@[a-zA-Z]+\.[a-z]+\.br", src.get_data())
	with open("%d_emails.txt"%len(emails),'w') as f:
		for email in emails:
			f.write(email+"\n")
	f.close()

if __name__ == '__main__':
	main()
