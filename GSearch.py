from googlesearch 		import search
import os
import datetime, time

print("Device Name: " + os.name)
print(datetime.datetime.now())
print("Write Quit to exit!")

question = input("Search All Over The Web!  ")

if question =="Quit":
	quit()

for i in search(question, tld="com", num=1, stop=20, pause=0):
	print("Result: " + i)
uestion = input("Search All Over The Web!  ")

for i in search(question, tld="com", num=1, stop=20, pause=0):
	print("Result: " + i)
	
uestion = input("Search All Over The Web!  ")

for i in search(question, tld="com", num=1, stop=20, pause=0):
	print("Result: " + i)
