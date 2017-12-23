from os import system
from random import randint

#this say function is the most important part of kids programming
#it uses the built in OSX say command to convert text to speech
def say(something):
    system('say "%s"' % something)

#how big a number should we guess?
max_number = 10
max_scramble = 3
first_line = "Guess a number between 1 and %d" % max_number
print(first_line)
say(first_line)
number = randint(1, max_number)
print(number)
not_solved = True

#keep looping unil we guess correctly
while not_solved:
    answer = input('?')
    you_said = "You typed %d" % answer
    #say(you_said)
    if answer > number:
        print("the number is lower")
        number = number - randint(1, max_scramble)
#        say("The number is lower")
    elif answer < number:
        print("the number is higher")
        number=number+randint(1, max_scramble)
#        say("The number is higher")
    else:
        print("you got it right")
#        say("You got it right")
        not_solved = False
