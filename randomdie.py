import random


while True:
	i=input("enter x to exit ")
	if(i=='x'):
		print("bye")
		exit()


	else:
		print("you got",random.randint(1,6))