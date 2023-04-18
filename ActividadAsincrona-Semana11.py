#Inicio del programa
print("**********************************")
print("Bucle While y For, Numeros enteros")
print("**********************************")

#Capturar la cantidad de numeros a procesar
num=input("Ingresa la cantidad de numeros a procesar ->")

#Captura los valores y verifica que sean numeros
while num.isdigit() != True:
   
    print("[-] Error, Vuelve a intentarlo nuevamente")
    print()
    num=input("Ingresa la cantidad de numeros a procesar ->")

#Convertir str a int   
num=int(num)

#Contadores
positivo=0
negativo=0
nulos=0

#Iniciar el bucle de los numeros
for i in range(num):
    
#Capturar los valores digitados
    i=i+1
    print()
    dato= input(f"Digita el {i}° numero:")
 
    parar=True

#Verificar numeros y letras

    while parar:
     try:
#Entra en "try" si son valores positivos o negativos

         dato=int(dato)
         parar=False
    
     except:

#Entra a "except" si son letras o cualquier otro caracter diferente a un numero

       print("[-] ERROR, ingresa un numero entero")
       print()
       dato=input(f"Digita el {i}° numero:")
   
#Contar los numeros entre positivos, negativos y nulos
    if dato>0:
        positivo+=1
    elif dato<0:
        negativo+=1
    else:
        nulos+=1
        
#Imprimir los resultados obtenidos   
print("") 
print("-------------------------------------------")   
print(f"La cantidad de numeros positivos fueron: {positivo}")
print()
print(f"La cantidad de numeros negativos fueron: {negativo}")
print()
print(f"La cantidad de numeros nulos fueron: {nulos}")
print("-------------------------------------------")    


        

