'''

@Date	: Sunday, June 22, 2013
@author	: The-Hydra (aka Abdel-Rahman Mohamed Moez)
@Version: 1.0

This script is for grabbing proxies IPs:PORTS and listing them
in well formatted way and exporting them into a text file.

You have the right to modify the script or use its idea ONLY BY GIVING ME THE CREDIT

'''

from bs4 import BeautifulSoup as BS
import urllib
import urllib2
import re
import os
import sys
import time


def get_external_ip():
	address = "http://www.ipchicken.com"
	string = urllib2.urlopen(address).read()
	EX_IP = re.search(r'(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})', string).group()
	return EX_IP

def list_proxy_list():
	proxyURL	= 'http://gatherproxy.com'
	soup		= BS(urllib2.urlopen(proxyURL))
	print "="*79
	print "IP "+"\t\tPORT"+" \tType"+"\t\tCountry, City"
	print "="*79
	for tag in soup.findAll('script'):
		try:
			PROXY_IP		= re.search(r'"PROXY_IP":"(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})\.(2[0-4]\d|25[0-5]|1?\d{1,2})"',str(tag)).group()[12:-1]
			PROXY_PORT		= re.search(r'"PROXY_PORT":"\d*"',str(tag)).group()[14:-1]
			PROXY_TYPE		= re.search(r'"PROXY_TYPE":"[a-zA-Z0-9-_]*"',str(tag)).group()[14:-1]
			PROXY_COUNTRY	= re.search(r'"PROXY_COUNTRY":"[a-zA-Z0-9-_]*"',str(tag)).group()[17:-1]
			if PROXY_TYPE == 'Elite': PROXY_COUNTRY = '\t'+PROXY_COUNTRY
			PROXY_CITY		= re.search(r'"PROXY_CITY":"[a-zA-Z0-9-_ ]*"',str(tag)).group()[14:-1]
			if test_proxy(PROXY_IP, PROXY_PORT) == True:

				OUTPUT = str(PROXY_IP+"\t"+str(PROXY_PORT)+"\t"+str(PROXY_TYPE)+"\t"+str(PROXY_COUNTRY)+", "+str(PROXY_CITY))
				print OUTPUT
		except: pass

def test_proxy(PROXY, PORT):
	proxy 	= urllib2.ProxyHandler({'http':PROXY+':'+PORT})
	auth	= urllib2.HTTPBasicAuthHandler()
	opener	= urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	install = urllib2.install_opener(opener)
	IP		= get_external_ip()
	if REAL_IP == IP:
		return False
	else:
		PROXY_FILE = open('PROXY_LIST.txt','a')
		PROXY_FILE.write(PROXY+":"+PORT+"\n")
		PROXY_FILE.close()
		return True

REAL_IP = get_external_ip()
print "="*79
print "[+] Your REAL IP: "+REAL_IP
#
#while 1: list_proxy_list()
