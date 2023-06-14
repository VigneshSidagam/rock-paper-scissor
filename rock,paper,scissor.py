#ROCK,PAPER AND SCISSORS GAME
name = input("enter your name:")
import random
def func():
    user = input("enter your choice(rock,paper,scissor):")
    b = ["rock", "paper","scissor"]
    computer = random.choice(b)
    if user==computer:
        print(f"{name} and computer,both choices are same, so the game is tie")
    elif user=="rock":
        if computer =="paper":
            print(f"Paper folds the rock, and {name} lose the game")
        else:
            print(f"Rock smashes the scissors, and {name} won the game")
    elif user=="paper":
        if computer =="rock":
            print(f"Paper folds the rock, and {name} won the game")
        else:
            print(f"Scissor cuts the paper, and {name} lose the game")
    else:
        if computer =="rock":
            print(f"Rock smashes the scissors, and {name} lose the game")
        else:
            print(f"Scissor cuts the paper, and {name} won the game")
func()
print()
ask = input("Do you want to play again(yes/no):")
while ask =="yes":
    func()
    ask = input("Do you want to play again(yes/no):")
    print()
else:
    print("THANK YOU")

