import random
a={1:"r",2:"p",3:"s"}
u=input("enter a random value form p,r,s")
if(u=='p' or u=='r' or u=='s'):
	c=a[random.randint(1,3)]
	print("u choose ",u,"computer choose",c)
	if(u==c):
		print("it is tie")
	elif((c=='r' and u=='p') or(c=='p' and u=='s') or (c=='s' and u=='r')):
		print("user is the winner")
	else:
		print("computer is the winner")
else:
	print("pls enter a valid key")