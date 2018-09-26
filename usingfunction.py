#using functions

a=int(input("enter the valve of a"))
b=int(input("enter the value of b"))


def add():
	c=a+b
	return c

def sub():
	c=a-b
	return c
 
def mutli():
	c=a*b
	return c 

def div():
	c=a/b
	return c

print("addition of a and b",add())
print("subtraction of a and b",sub())
print("multipication of a and b",mutli())
print("divition of a and b",div())


