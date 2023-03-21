print()
print("Estructura de control IF ELSE")
print()

#Crear 10 datos de personas (Países, Gentilicios)
#extraerSubCadena= per1[10:21] print(extraerSubCadena)

per1="salvador" 

per2="alemania"

per3="rusia"

per4="belgica"

per5="españa" 

per6="costa rica"

per7="peru" 

per8="paraguay" 

per9="mexico" 

per10="panama" 


#Crear 10 datos de animales (Especie, tipo)

especie1="mamifero"
tipo1="Girafa"
tipo2="Cerdo"

especie2="canina"
tipo3="Zorro"
tipo4="Perro"

especie3="reptil"
tipo5="Lagarto"
tipo6="Serpiente"

especie4="ave"
tipo7="Aguila"
tipo8="Torogoz"

especie5="anfibio"
tipo9="Rana"
tipo10="Sapo"



#Nombre de la persona
nombre=input("Ingresa tu nombre: ")
print()

#Menu para elijer la opcion ya sea personas o animales a procesar
mensaje="""Menú:
Digita (1) para 'Personas'
Digita (2) para 'Animales'
Digata (3) para 'Salir'"""

#Menu de paises
menu="""Menu de paises:

1-El salvador
2-Alemania
3-Rusia
4-Belgica 
5-Español
6-Costa Rica
7-Peru
8-Paraguay
9-Mexico
10-Panama
"""

#Menu de especie de animales
menu2="""Menu de especies:

1-Mamifero 
2-Canina
3-Reptil 
4-Ave
5-Anfibio
"""

print(mensaje)

print()
op=(input(f"{nombre} toma un caso:"))
print()

if op is "1":
    
    print("*******************")
    print("Escogiste Personas")
    print("*******************")
    print()
    print(menu)
    dato=input("Escoge tu pais (por numeral o nombre): ")
    dato=dato.lower()
    print()
    
    if dato==per1 or dato=="1":
        
        print(f"{nombre} eres de {per1} y tu gentilicio es Salvadoreño/a")  #
        
    elif dato==per2 or dato=="2":
        
        print(f"{nombre} eres de {per2} y tu gentilicio es Aleman/a")
        
    elif dato==per3 or dato=="3":
        
        print(f"{nombre} eres de {per3} y tu gentilicio es Ruso/a")
        
    elif dato==per4 or dato=="4":
              
        print(f"{nombre} eres de {per4} y tu gentilicio es Belga")
        
    elif dato==per5 or dato=="5":
        
        print(f"{nombre} eres de {per5} y tu gentilicio es Español/a")
     
    elif dato==per6 or dato=="6":
        
        print(f"{nombre} eres de {per6} y tu gentilicio es Tico/a")

    elif dato==per7 or dato=="7":
        
        print(f"{nombre} eres de {per7} y tu gentilicio es Peruano/a")

    elif dato==per8 or dato=="8":
        
        print(f"{nombre} eres de {per8} y tu gentilicio es Paraguayo/a")

    elif dato==per9 or dato=="9":
        
        print(f"{nombre} eres de {per9} y tu gentilicio es Mexicano/a")

    elif dato==per10 or dato=="10":
        
        print(f"{nombre} eres de {per10} y tu gentilicio es Panameño/a")

    else:         
     print("Pais no encontrado.   \nFIN")


elif op is"2":
    
   print("*******************")
   print("Escogiste Animales")
   print("*******************")
   print()
   
   print(menu2)
   dato2=input(f"{nombre} escoge un tipo de especie (por numeral o nombre):")
   print()
   
   dato2=dato2.lower()
   
   if dato2==especie1 or dato2=="1" :
       
       print(f'Los animales de la especie "{especie1}", en el sistema solo existen: {tipo1} y {tipo2}')
   
   elif dato2==especie2 or dato2=="2" :
       
       print(f'Los animales de la especie "{especie2}", en el sistema solo existen: {tipo3} y {tipo4}')
    
   elif dato2==especie3 or dato2=="3" :
       
       print(f'Los animales de la especie "{especie3}", en el sistema solo existen: {tipo5} y {tipo6}')
   
   elif dato2==especie4 or dato2=="4" :
       
       print(f'Los animales de la especie "{especie4}", en el sistema solo existen: {tipo7} y {tipo8}')
   
   elif dato2==especie5 or dato2=="5" :
       
       print(f'Los animales de la especie "{especie5}", en el sistema solo existen: {tipo9} y {tipo10}')
   
   else:
       
       print("Especie no existente en el sistema")

elif op is "3":
    
    print("Fin programa")
    
else:
    
    print("Opcion no valida, debes digitar '1', '2' o '3' ")