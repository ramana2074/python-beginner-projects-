import random
print("Lets start our Number Guessing game")
a = input("Enter a number ")
if a.isdigit():
    a = int(a)

    if a <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number= random.randint(0 , a)
guesses=0
while True:
    guesses+=1
    x = input("Guess the number ")
    if x.isdigit():
        x = int(x)
    else:
        print('Please type a number next time.')
        continue

    if(x==random_number):
        print("you got it right")
        break;
    elif (x < random_number):
        print("Guess higher")
    else:
        print("Guess lower")
print("you guessed it right after "+str(guesses)+" guesses")
print("Thank you for playing")