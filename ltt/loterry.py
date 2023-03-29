import random

low = 0
high = 50
option = 30
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    # option += 1
    if guess < option:
        print(f"{guess} Sorry try again!")

    elif guess > option:
        print(f"{guess} sorry try again!")
    # else: 
    if guess == option:
        
        print(f"Congratulations, you have Won!!!") 
        break
print(f"Your Lucky number is {option}")