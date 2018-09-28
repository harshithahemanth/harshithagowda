#dic
import random

p={1:'r',2:'p',3:'s'}

while True:
	yc=input("you choice: r/p/s: ")
	cc=p[random.randint(1,3)]

	print("computer gave: ", cc)

	if(yc=='r' and cc=='p'):
		print("computer wins the game")
	elif(yc=='s' and cc=='p'):
		print("you win the game")
	elif(yc=='r' and cc=='s'):
		print("you win the game")
	elif(yc=='p' and cc=='r'):
		print("computer wins the game")

	

