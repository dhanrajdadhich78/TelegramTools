#!/bin/env python3
# code by : 

"""

you can re run setup.py 
if you have added some wrong value

"""
redColor="\033[1;31m"
greenColor="\033[1;32m"
cyanColor="\033[1;36m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{redColor}╔═╗{cyanColor}┌─┐┌┬┐┬ ┬┌─┐
	{redColor}╚═╗{cyanColor}├┤  │ │ │├─┘
	{redColor}╚═╝{cyanColor}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' this may take some time ...')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' it will take upto 10 min to install csv merge.')
	input_csv = input(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' do you want to enable csv merge (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(greenColor+"[+] Installing requierments ...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
	banner()
	print(greenColor+"[+] requierments Installed.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(greenColor+"[+] enter api ID : "+redColor)
	cpass.set('cred', 'id', xid)
	xhash = input(greenColor+"[+] enter hash ID : "+redColor)
	cpass.set('cred', 'hash', xhash)
	xphone = input(greenColor+"[+] enter phone number : "+redColor)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(greenColor+"[+] setup complete !")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' merging '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' big files can take some time ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' saved file as "output.csv"\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/dhanrajdadhich78/TelegramTools/master/.image/.version")
	if source.text == '1':
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' alredy latest version')
	else:
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' removing old files ...')
		os.system('rm *.py');time.sleep(3)
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' getting latest files ...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/dhanrajdadhich78/TelegramTools/master/GetGroupUserData.py
			curl -s -O https://raw.githubusercontent.com/dhanrajdadhich78/TelegramTools/master/setup.py
			curl -s -O https://raw.githubusercontent.com/dhanrajdadhich78/TelegramTools/master/SendMessageToAll.py
			chmod 777 *.py
			""");time.sleep(3)
		print(greenColor+'\n['+cyanColor+'+'+greenColor+']'+cyanColor+' update compled.\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' selected module : '+redColor+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' selected module : '+redColor+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(greenColor+'['+cyanColor+'+'+greenColor+']'+cyanColor+' selected module : '+redColor+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""$ python3 setup.py -m file1.csv file2.csv
			
	( --config  / -c ) setup api configration
	( --merge   / -m ) merge 2 .csv files in one 
	( --update  / -u ) update tool to latest version
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
	else:
		print('\n'+greenColor+'['+redColor+'!'+greenColor+']'+cyanColor+' unknown argument : '+ sys.argv[1])
		print(greenColor+'['+redColor+'!'+greenColor+']'+cyanColor+' for help use : ')
		print(greenColor+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+greenColor+'['+redColor+'!'+greenColor+']'+cyanColor+' no argument given : '+ sys.argv[1])
	print(greenColor+'['+redColor+'!'+greenColor+']'+cyanColor+' for help use : ')
	print(greenColor+'['+redColor+'!'+greenColor+']'+cyanColor+' https://github.com/dhanrajdadhich78/TelegramTools#-how-to-install-and-use')
	print(greenColor+'$ python3 setup.py -h'+'\n')
