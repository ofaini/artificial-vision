#Developed by Oscar Faini

from random import randint
import os

os.system("cls")

players=[]
points=[]
ganador=[]
print("Total players: ", players)

print("Please, select the level you want to play")
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


num_player = int(input("Number of players: "))
i=1
while i <= num_player:
  players.append(i)
  points.append(randint(1,12))
  i = i+1

x = len(points)

meta =0
print("Nivel del juego ",level)
print("jugadores: ",x)
print("Total of points: ",points)
print("****prueba ciclo*****")


j=0
while j < x:  
  print(j)
  meta = int(points[j])+randint(1,12)
  points[j] = meta
  meta = 0
  print(points)

  j = j+1
  
print("****prueba ciclo*****")
print("Total players: ", players)
print("Total of points: ",points)
print("Game level: ", op, " = ", level," points")
print("el valor de j es ",j)