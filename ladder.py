import random
count=0
def myroll():
	return random.randint(1,6)


while(count<=100):
	n=input("press r roll the die")
	if(n=='r'):
		r=random.randint(1,6)
		count=count+r
		
		if(count>100):
			count=count-r
		else:
			print("u got",r)
			print("new position is",count)

		if(count==8):
			count==37
			print("u got ladder")
		elif(count==11):
			count=2
			print("sorry, u got snake")

		if(count==13):
			count==34
			print("u got ladder")
		elif(count==25):
			count=4
			print("sorry, u got snake")

		if(count==40):
			count=68
			print("u got ladder")
		elif(count==38):
			count=9
			print("sorry, u got snake")

		if(count==52):
			count=81
			print("u got ladder")
		elif(count==65):
			count=46
			print("sorry, u got snake")


		if(count==76):
			count=97
			print("u got ladder")
		elif(count==89):
			count=70
			print("sorry, u got snake")


		elif(count==93):
			count=64
			print("sorry, u got snake")	

		elif(count==95 and r>6):
			print("invaild input")
		elif(count==96 and r>5):
			print("invaild input")
		elif(count==97 and r>4):
			print("invaild inut")
		elif(count==98 and r>3):
			print("invaild input")
		elif(count==99 and r>2):
			print("invaild input")


		elif(count==100):
			print("u won the game")
			exit()


