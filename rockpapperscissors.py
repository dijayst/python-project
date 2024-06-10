import  random
from colorama import Fore,Back,Style

name=input("enter your name: ")
print("welcome " + name + " lets play rock paper scissors")
games=["rock","paper","scissors"]

while True:
    
    player=input(Fore.BLUE + "enter either rock,paper,scissors:")
    r1=random.choice (games)
    
    if  player==r1:
        print("you chose " + player)
        print("computer chose " + r1 )
        print(Fore.YELLOW + name + " its a draw")
    
    elif player=="rock" and r1=="scissors" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.RED + name + " you lost")
        
    elif player=="rock" and r1=="paper" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.RED + name + " you won")
    
    elif player=="paper" and r1=="scissors" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.RED + name + " you lost")
    
    elif player=="scissors" and r1=="scissors" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.RED + name + " it a draw")
    elif player=="paper" and r1=="paper" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.GREEN + name + " it a draw")
    elif player=="rock" and r1=="rock" :
         print("you chose " + player)
         print("computer chose " + r1 )
         print(Fore.RED + name + " it a draw")
    