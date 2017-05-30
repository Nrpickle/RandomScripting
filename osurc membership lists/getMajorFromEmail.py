'''
Nick McComb | www.nickmccomb.net
Written May 2017 for OSURC

Requirements:
bs4
requests
pandas

'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

def getMajorFromEmail(email):
	url = "http://directory.oregonstate.edu/?type=search&cn=&surname=&mail=" + email.replace("@", "%40")
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	if len(soup.find_all('dd')) < 2:
		return 'No record found.'
	dt_all = soup.find_all('dt')[2]
	dd_all = soup.find_all('dd')[2]

	dept = str(dd_all).replace('</dd>','').replace('<dd>','').replace('&amp;','&')
	return dept

if __name__ == "__main__":
	print getMajorFromEmail("Becrafta@oregonstate.edu")
	
