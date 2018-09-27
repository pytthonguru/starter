#printing function
a=int(input("enter the value of a "))
b=int(input("enter the value of b"))
def add():
	return a+b

def sub():
	return a-b

def mulitiplication():
	return a*b

def divion():
	return a%b

print("addition of ",a,"and",b,"=",add())
print("subtraction of ",a,"and",b,"=",sub())
print("mulitiplication of ",a,"and",b,"=",mulitiplication())
print("modules of",a,"and",b,"=",divion())