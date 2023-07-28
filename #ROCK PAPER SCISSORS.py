#ROCK PAPER SCISSORS
import random

options=("rock","papper","scissors")
isRunning=True

while isRunning:
    player=None
    computer=random.choice(options)
    
    while player not in options:
        player=input("Enter a chocie(rock,papper,scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print("It is tie !")
    elif player=="rock" and computer=="scissors":
        print(" You Win !")
    elif player=="papper" and computer=="rock":
        print(" You Win !")
    elif player=="scissors" and computer=="papper":
        print(" You Win !")
    else:
        print(" You Lose !")            
    if not input("Play again ? (y/n): ").lower()=="y":
        isRunning=False
print("Thanks For Playing")        
