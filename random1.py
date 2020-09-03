#Develoer: Oscar Faini
#Script: this program let us to generate one random number

#randint => generates Z numbers.
#uniform => generates R numbers.

#libraries
import os
from random import randint, uniform

#functions
def rand_integer():
  nz = randint(1,10)
  return nz

def rand_real():
  nr = uniform(1,10)
  return nr

def number_list():
  i=1
  while i <= 10:
    x = randint(1,100)
    print(x)
    i=i+1

#main
os.system("cls")
z = rand_integer()
r = rand_real()
print("The Z number is: ",z)
print("The R number is: ",r)
print("**************")
number_list()