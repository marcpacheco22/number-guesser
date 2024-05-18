import random 

## this means you are importing a module

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ("please type a number larger than 0 ")
        quit()
else:
    print("please type a number")
    quit()



##if you do randrange(-1, 10) it will not include 10
##if you do not specify a start to the range it will start at 0
##if you do random.rantint(-1,10) it will include 10

random_number = random.randint(0, top_of_range)
guesses = 0

## continue brings you back to the top of the loop
##elif checks and if not true moves to next line

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("please type a number")
        continue

    if user_guess == random_number:
        print ("good job you got it")
        break
    elif user_guess > random_number:
        print("your guess is too high ")
    else:
        print("your guess is too low")
        

print("you got it in", guesses, "guesses")


