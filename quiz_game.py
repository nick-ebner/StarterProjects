import random;

top_of_range = int(input("Type a number: "))

target = random.randint(0,top_of_range)
guesses = 5

while True:

    print(f"You have {guesses} guesses")
    guess = int(input("Type a number: "))

    if guess == target:
        print(f"Congratulations! {guess} is the correct answer")
        quit()
    
    if guess > target:
        print("That guess is too high. Please try again!")
    else:
        print("That guess is too low. Please try again!")
    
    guesses = guesses-1
    if guesses == 0:
        print(f"You lose! The correct answer was {target}!")
        break