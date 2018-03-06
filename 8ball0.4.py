import random

#All possible answers below are from https://en.wikipedia.org/wiki/Magic_8-Ball
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yep", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
print(random.choice(answers))

#I am attempting to prevent the premature closing of the program, FIND BETTER WAY AFTER LEARNING MORE
finish = input("\nPress any key to end program. ")
