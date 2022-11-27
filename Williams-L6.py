#Ke'niah Williams
#November 11th,2022
#Create a lottery game that reads a file with 3 random numbers the user will win a reward based on how many number were guessed correctly and the order

import random
# Generate 3 digits separately then combine them to form a 3 digit number
pickone = random.randint(0,9)
picktwo = random.randint(0,9)
pickthree = random.randint(0,9)
winningnumber = str(pickone) + str(picktwo) + str(pickthree)
print(f"Computer number is {winningnumber}")
# Read the number input from file and store in a variable
file = open('user_pick.txt','r')
usernumber= file.read()
file.close()
print(f"User number is {usernumber}")

#Compare number in file against computer generated number
if usernumber == winningnumber:
    print("Congratulations, you've won $10,000")
else:
    count = 0
    for number in winningnumber:
        if number in usernumber:
            count += 1
print(f"Count is {count}")

if count == 3:
    print("Congratulations, you've won $1,000")
elif count == 2:
    print("Congratulations you've won $100")
elif count == 1:
    print("Congratulations, you've won $1")
else:
    print("Not a winner")

