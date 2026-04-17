import random
b = int(input("Enter the range of guessing a number : "))
a = random.randint(1, b)
guess = 0
Try =1
while guess != a:
    guess = int(input("Enter your guess: "))
    if guess < a:
        print("Too low! Try again.")
        Try +=1
    elif guess > a:
        print("Too high! Try again.")
        Try +=1
    else:
        print("Congratulations! You guessed the number in",Try,"tries.")
