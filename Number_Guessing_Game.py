import random as re 

num = re.randint(1, 100)
attempts = 0
print(num)
print("====================================")
print("Welcome to the Number Guessing Game ")
print("====================================")
while True :
    guess = int(input("Guess :"))
    attempts += 1
    if guess < num:
        print("Too Low!")
    elif guess > num:
        print("Too High!")
    else :
        print("Correct!")
        print("Attempts : ",attempts)
        break
