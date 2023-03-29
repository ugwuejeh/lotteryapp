import random

low = 0
high =50
option =30
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    
    if guess < option:
        print(f"{guess} Sorry try again!")

    elif guess > option:
        print(f"{guess} sorry try again!")

    else:
        
     print(f"Congratulations, you have Won!!!", "Your lucky number is", option)

     break

print(f"you are a lucky winner")