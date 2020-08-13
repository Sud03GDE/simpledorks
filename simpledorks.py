#!/usr/python3

import subprocess
import webbrowser

subprocess.run (["clear"])

print ("Simple google operators to look up automated with python3.")

def MainMenu():
	print ("1. Site")
	print ("2. Inurl")
	print ("3. Intitle")
	print ("4. Link")
	print ("5. Cache")
	print ("6. Filetype")
	
	#menu input
	selection=int(input("Choose 1-6: "))

	#define function before calling it 
	#site function
	def site():
		website=input ("Site to lookup: ")	
		webbrowser.open ("www.google.com/search?q=site:" + website)

	#site call
	if selection==1:
		site()

	#inurl function
	def inurl():
		website=input ("Website: ")
		url=input ("Inurl for website: ")
		webbrowser.open ("www.google.com/search?q=site:" + (website) + (" ") + ("inurl:") + (url))
	
	#inurl call
	if selection==2: 
		inurl()
	
	#intitle function
	def intitle():
		website=input ("Website: ")
		title=input ("Intitle, useful for specific name: ")
		webbrowser.open ("www.google.com/search?q=site:" + (website) + (" ") + ("intitle:") + (title))

	#intitle call
	if selection==3:
		intitle()

	#link function
	def link():
		knil=input ("Link, Find content linking towards a specific website: ")
		webbrowser.open ("www.google.com/search?q=link:" + (knil))

	#link call
	if selection==4:
		link()
	
	#cache function
	def cache():
		cash=input ("Cache, find old versions of websites: ")
		webbrowser.open ("www.google.com/search?q=cache:" + (cash))

	#cache call
	if selection==5:
		cache()

	#filetype function
	def filetype():	
		keyword=input ("Search for certain files with keywords: ")
		fil=input ("Filetype: ")
		webbrowser.open ("www.google.com/search?q=" + (keyword) + (" ") + ("filetype:") + (fil))

	#filetype call
	if selection==6:
		filetype()


	#invalid character
	else:
        	print ("Invalid character")
	       	subprocess.run (["clear"])
        	MainMenu()

MainMenu()
