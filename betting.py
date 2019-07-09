# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs
import csv
from urllib import urlopen
from bs4 import BeautifulSoup
import pandas as pd



#get page and parse the response with bs4
url = "https://www.forebet.com/en/football-predictions-from-yesterday"

#request the page with urlopen urlib function and parse it with bs4.
response = urlopen(url)
parsed_page = BeautifulSoup(response, 'lxml')

def tr_0():
	rows = parsed_page.findAll("tr", {"class":"tr_0"})
	for row in rows:
		print (row.text)

def tr_1():
	rows = parsed_page.findAll("tr", {"class":"tr_1"})
	for row in rows:
		print (row.text)



tr_0()
tr_1()

