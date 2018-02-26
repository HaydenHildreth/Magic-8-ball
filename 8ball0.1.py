import random

#Random number
z = random.randint(1,10)

#All possible answers below are from https://en.wikipedia.org/wiki/Magic_8-Ball
if z < 5:
	print ("It is certain.")
elif z <10:
	print ("Reply hazy try again.")
elif z <15:
	print ("As I see it, yes.")
elif z <20:
	print ("Don't count on it.")
elif z <25:
	print ("It is decidedly so.")
elif z <30:
	print ("Ask again later.")
elif z <35:
	print ("Most likely.")
elif z <40:
	print ("My reply is no.")
elif z <45:
	print ("Without a doubt.")
elif z <50:
	print ("Better not tell you now.")
elif z <55:
	print ("Outlook good.")
elif z <60:
	print ("My sources say no.")
elif z <65:
	print ("Yes definitely.")
elif z <70:
	print ("Cannot predict now.")
elif z <75:
	print ("Yes.")
elif z <80:
	print ("Outlook not so good.")
elif z <85:
	print ("You may rely on it.")
elif z <90:
	print ("Concentrate and ask again.")
elif z <95:
	print ("Signs point to yes.")
else:
	print ("Very doubtful.")

#I am attempting to prevent the premature closing of the program, FIND BETTER WAY AFTER LEARNING MORE
finish = input("\nPress any key to end program.")
