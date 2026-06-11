#Guess the Number Game
'''import random

secret_number=random.randint(1,10)
print("Guess a number between 1 and 10")
while True:
    guess=int(input("Enter your guess:"))

    if guess==secret_number:
        print("Congratulations! You guessed correct number")
        break
    elif guess<secret_number:
        print("Your number is too low")
    else:
        print("Your number is too big")'''


#Rock,paper,scissor game
import random
choices=["rock","paper","scissor"]

computer=random.choice(choices)
user=input("Enter rock,paper,or scissor:").lower()
print("Computer choice:",computer)

if user==computer:
    print("its a tie")
elif(user == "rock" and computer == "scissors") or \
    (user == "paper" and computer == "rock") or \
    (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins")