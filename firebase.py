#!/usr/bin/env python
#
# firebase.py
# Read from a list of firebase urls
#
# Author: random_robbie

import colorama
import sys
import re
import requests
from time import sleep
from colorama import init, Fore, Back, Style
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init(autoreset=True)

# Configuration
fname = "firebase.txt"
FILE = "/.json"
session = requests.Session()

def filter_result(str):
	str.strip() #trim
	str.lstrip() #ltrim
	str.rstrip() #rtrim
	return str


def test_fb (URL,FILE):
	print (Fore.YELLOW +"[*] Testing: "+URL+" [*]")
	try:
		
		URLi = "https://"+URL+""+FILE+""
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1"}
		response = session.get(URLi, headers=headers, verify=False)
		result = response.text
		if '"Permission denied"' not in result:
			if 'Please ensure that you spelled the name of your Firebase correctly' not in result:
				if '"error" : "404 Not Found"' not in result:
					text_file = open("./cfg/vun.txt", "a")
					text_file.write(""+URLi+"\n")
					text_file.close()
					print (Fore.GREEN +"[*] *********** Firebase Vulnerable... Found *********** [*]")
					#print (result)
				else:
					print (Fore.RED +"[*] Firebase URL does not exist  [*] ")
			else:
				print (Fore.RED +"[*] Firebase URL does not exist  [*] ")
		else:
				print (Fore.RED +"[*] Not Vulnerable [*] ")
	except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
			
	except Exception as e:
		print (Fore.RED +"[*] Error has occured for: "+URL+" [*]")
		print (e)
	



	
	
try:
	#READ MASSIVE FILE
	with open(fname) as f:
		for line in f:
			line2 = line.split(" ")
			URL = line2[0].replace("\n","")
			test_fb (URL,FILE)
		
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
