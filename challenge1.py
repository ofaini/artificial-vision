#Develoer: Oscar Faini
#Script: Number race

#libraries
import os
import time
from random import randint

op = ''

def menu():
  print("[1]. Add 50 to win")
  print("[2]. Add 70 to win")
  print("[3]. Add 100 to win")
  print("please, enter any option")
  op = int(input())
  if op == 1:
    level = 50
  elif op == 2:
    level = 70
  elif op == 3:
    level = 100
  else:
    time.sleep(1)
    print("Opcion incorrecta")
    level = 0
    menu()
  player1 = 0
  player2 = 0
  
  while player1<level or player2<level:    
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    player1 = player1+dice1+dice2
    print("Player 1, your score is: ",player1)
      
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    player2 = player2+dice1+dice2
    print("Player 2, your score is: ",player2)    
    time.sleep(1)

    if player1>=level and player2>=level:
      time.sleep(2)
      print("both reached the goal, It's a draw!!")
      break
    elif player1>=level:
      time.sleep(2)
      print("Player1, You won!!\nYou reach: ",player1," points")
      break
    elif player2>=level:
      time.sleep(2)
      print("Player2, You won!!\nYou reach: ",player2," points")
      break  


def play():
  os.system("cls")
  m = menu()
  again = input("\n\nWant to play again? (Y/N)")
  if again == 'Y' or again == 'y':
    os.system("cls")
    play()
  else:
    print("\n\nGood Bye!\nDevelopment by Oscar Faini")

#main
os.system("cls")
m = play()