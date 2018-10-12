#dic
import random

p={1:'r',2:'p',3:'s'}
y=0
c=0

while True:
	yc=input("you choice: r/p/s: ")
	cc=p[random.randint(1,3)]

	print("computer gave: ", cc)

	if(yc=='r' and cc=='p'):
		print("computer wins the game")
		c+=1
	elif(yc=='s' and cc=='p'):
		print("you win the game")
		y+=1
	elif(yc=='r' and cc=='s'):
		print("you win the game")
		y+=1
	elif(yc=='p' and cc=='r'):
		print("you win the game")
		y+=1
	elif(yc=='p' and cc=='s'):
		print("computer wins the game")
		c+=1
	elif(yc=='s' and cc=='r'):
		print("computer wins the game")
		c+=1
	elif(yc=='r' and cc=='r'):
		print("try again")
	elif(yc=='s' and cc=='s'):
		print("try again")
	elif(yc=='p' and cc=='p'):
		print("try again")

	print("you won the game against computer",y)
	print("computer wow the game against you",c)
	if(c==3 or y==3):
		break



	

