#Develoer: Oscar Faini
#Script: this proram let you operate two numbers entered by the user according to a option menu

#clear screen class
import os

os.system("cls")

print("Enter first number: ")
x = int(input())

y = int(input("Enter second number: "))

print("[1]. Add")
print("[2]. Subs")
print("[3]. Mult")
print("[4]. Div")
print("please, enter any option")
op = input()

if op == '1':
  print("Add is: ", x+y)
elif op == '2':
  print("Subs is: ", x-y)
elif op == '3':
  print("Mult is: ", x*y)
elif op == '4':
  print("Div is: ", x/y)
else:
  print("Invalid option")
