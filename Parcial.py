print("********************************")
print("Parcial #2 - Ejercicio propuesto")
print("********************************")

num=input("Ingresa la cantidad de numeros a procesar: ")

while num.isdigit() != True:
    print("[-] Error, Digita un numero positivo")
    print()
    num=input("Ingresa la cantidad de numeros a procesar: ")

num=int(num)

valor=0
for i in range(num):
    
   i=i+1
   print(1,"/",i)
   valor+=1/i
  
print()
print("La sumatoria de toda las fracciones es de: ",valor)
