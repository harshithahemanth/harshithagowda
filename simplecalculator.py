#program for simple calculator

i=int(input("enter the value of i: "))
j=int(input("enter the valve of j: "))
o=input("what do you want to do ? +,-,/,x: ")

def add():
	return i+j
def sub():
	return i-j
def multi():
	return i*j
def div():
	return i/j

if(o=='+'):
	print("addition=",add())
elif(o=='-'):
	print("subtraction=",sub())
elif(o=='x'):
	print("multipication=",multi())
elif(o=='/'):
	print("division=",div())