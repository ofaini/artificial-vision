import os

os.system("cls")

def add_placa(x):
  placas_list.append(x)
  print("Placas: ",placas_list)
  print("len ",len(placas_list))

#listas
placas_list = [123, 'AXZ', 'PUJ333']
fruits_list = ['apple','orange','banana']
numbers_list = [1,2,3,4]

print("Placas: ",placas_list)
print("len ",len(placas_list))
print("Frutas: ",fruits_list)
print("len: ",len(fruits_list))
print("Numeros: ",numbers_list)
print("len: ",numbers_list)

for element in range(len(placas_list)):
  print (placas_list[element])


#main
print('::::::::::::::::::::::::::::::')
placa = input("ingrse la placa: ")
add_placa(placa)