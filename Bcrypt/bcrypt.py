#!/usr/bin/env python3
import bcrypt
import threading

def encryption(text):
	hashed = bcrypt.hashpw(text, bcrypt.gensalt(10)).decode('utf8')
	print(hashed)

def dencryption(hash,passlist):
	a=1
	passwords = open(passlist, 'r')
	for word in passwords:
		wds = word.strip().encode('utf8')
		print("Number of passwords tried: {0}".format(a),end='\r')
		a=a+1
		if bcrypt.checkpw(wds, hash):
			print("Password Matched With :",wds)
			break
	print("Completed")

if __name__ == '__main__':
	while True:
		print("------Bcrypt Hash Menu-------")
		print("1. Dencryption")
		print("2. Encryption")
		print("3. Exit")
		option = int(input("Enter The option: "))
		if option == 1 :
			hash = input("Enter your hash: ").encode('utf')
			passlist = input("Enter location of wordlist(press ENTER for default): ")
			if passlist == "":
				passlist = 'pass.txt'
			dencryption(hash,passlist)
		elif option == 2 :
			text = input("Enter text to encrypt: ").encode('utf8')
			encryption(text)
		elif option == 3:
			print("Exiting..........")
			break
		else:
			print("Enterd an invalid option")
