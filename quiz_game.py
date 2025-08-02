import random;

print("-----------Welcome to the Number Guessing Game!-----------") 
print("I'm thinking of a number between 0 and 25. What level of \ndifficulty would you like to play with?\n\t1 - Easy (10 guesses)\n\t2 - Medium (7 guesses)\n\t3 - Hard (5 guesses)")
selection = int(input("\nEnter a number: "))
if selection == 1:
    guesses = 10
elif selection == 2:
    guesses = 7
elif selection == 3:
    guesses = 5
target = random.randint(0,25)
while True:
    print(f"\nYou have {guesses} guesses")
    guess = int(input("Type a number: "))
    if guess == target:
        print(f"---------Congratulations! {target} is the correct answer---------")
        quit()

    guesses = guesses-1
    if guess > 0:
        if guess > target:
            print("That guess is too high. Please try again!")
        else:
            print("That guess is too low. Please try again!")
    else:
        print(f"------------You lose! The correct answer was {target}------------") 
        break