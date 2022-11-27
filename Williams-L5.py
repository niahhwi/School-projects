import random 
def menu():
    print("1.Easy: 1-10")
    print("2.Medium: 1-20")
    print("3.Hard: 1-50")
    print("4.Quit playing")

print("Select a mode for the guessing game")
menu()

mode = int(input("Which mode would you like to play?: "))

def easy():
    guess = random.randint(1,10)
    x = 0
    for easy in range(6):
        if x == 5:
            print("You lost")
            break
        num = int(input("Guess a number 1-10: "))
        if guess == num:
            print("Congratulations, you guessed correctly!")
            break 
        elif guess > num and easy:
            print("You guessed too low")
        else:
            print("You guessed too high")
        x = x+1

def medium():
    guess = random.randint(1,20)
    x = 0
    for medium in range(6):
        if x == 5:
            print("You lost")
            break
        num = int(input("Guess a number 1-20: "))
        if guess == num:
            print("Congratulations, you guessed correctly!")
            break
        elif guess > num:
            print("You guessed too low")
        else:
            print("You guessed too high")
        x = x + 1
        
def hard():
    guess = random.randint(1,50)
    print(guess)
    x = 0
    for hard in range(6):
        if x == 5:
            print("You lost")
            break
        num = int(input("Guess a number 1-50: "))
        if guess == num:
            print("Congratulations, you guessed correctly!")
            break
        elif guess > num:
            print("You guessed too low")
        else:
            print("You guessed too high")
        x = x + 1
def end():
    print("Thank you for playing!")
     
if mode == 1:
    easy()
elif mode == 2:
    medium()
elif mode == 3:
    hard()
else:
    print("Thank you for playing")

print()
print("Select a mode for the guessing game")
menu()
mode = int(input("Which mode would you like to play?: "))

if mode == 1:
    easy()
elif mode == 2:
    medium()
elif mode == 3:
    hard()
else:
    print("Thank you for playing")



