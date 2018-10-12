#tictakto
import random
a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print('.......')
	print(a[0]+'|'+a[1]+'|'+a[2]+'|')
	print('......')
	print(a[3]+'|'+a[4]+'|'+a[5]+'|')
	print('......')
	print(a[6]+'|'+a[7]+'|'+a[8]+'|')
	print('.......')
printboard()

p1 = True

while(True):
	printboard()

	if p1:
		p=input("player1, choose your place : ")
		if p in a:
			a[int(p)-1]='x'
			p1= not p1

	else:
		p=input("player 2, choose your place : ")
		if p in a:
			a[int(p)-1]='0'
			p1=not p1
	for i in(0,3,6):
		        if(a[i]==a[i+1] and a[i]==a[i+2]):
		        	print("game over")
		        	printboard()
		        	exit()

	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			print("game over")
			printboard()
			exit()

	if(a[0]==a[4] and a[0]==a[8]):
		print("game over")
		printboard()
		exit()

	if(a[2]==a[4] and a[2]==a[6]):
		print("game over")
		printboard()
		exit()

	else:
		print("you have entered an invalid position")
		continue


