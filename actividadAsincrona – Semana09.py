print()
print("**********************************************")
print("Operadores de comparación y operadores lógicos")
print("**********************************************")
print()

#Pedir nombre al usuario
nombre=input("Ingresa tu nombre: \n")
print()

#Pedir nombre al apellido
ape=input("Ingresa tu apellido: \n")
print()

#Pedir nombre al edad
edad=int(input("Digita tu edad: \n"))
print()

#Pedir nombre al sexo
sexo=input("Digita tu sexo, F 'Femenino' M 'Masculino': \n").lower()
print()

#Imprimir resultado
print(f"Tu nombre es {nombre} {ape} tienes {edad} años de edad y tu sexo es {sexo}")

print()

#Definir segun el sexo si es  Niño/a, mujer/hombre, abuelo/a, señor/a

   
if sexo=="m" or sexo=="masculino":

  print(f"{nombre} eres un Niño, hombre, abuelo, señor")
  print()
            
elif sexo=="f" or sexo=="femenino":

  print(f"{nombre} eres un Niña, mujer, abuela, señora")
  print()
    
else:
    print("Error sexo no compatible")
    print()
    
if edad>=0 and edad<=2:
        
     print(f"{nombre} eres un bebé")
     
elif edad>=3 and edad<=5:
    
    print(f"{nombre} estas en la infancia")
 
elif edad>=6 and edad<=11:
    
    print(f"{nombre} estas en la niñez")
    
elif edad>=12 and edad<=18:
    
    print(f"{nombre} eres un/a adolecente")
    
elif edad>=19 and edad<=26:
    
    print(f"{nombre} estas en la juventud")
    
elif edad>=27 and edad<=40:
    
    print(f"{nombre} eres un adulto joven")
    
elif edad>=41 and edad<=55:
    
    print(f"{nombre} eres un adulto")
    
elif edad>=56 and edad<=65:
    
    print(f"{nombre} eres una persona mayor")
    
elif edad>=66 and edad<=100:
    
    print(f"{nombre} eres un abuelo/a")
    
else:
    print()
    print(f"{nombre} digitaste una edad no compatible")
    
    
if edad%2==0:
    print()
    print(f"La edad de {nombre} es par")
    
else:
    print()
    print(f"La edad de {nombre} es impar")
    