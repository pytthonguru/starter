import random


while True:
	i=input("press a to roll a die")
	if(i=='a'):
		print("you got",random.randint(1,6))

	else:
		print("you have been exited")
		exit()