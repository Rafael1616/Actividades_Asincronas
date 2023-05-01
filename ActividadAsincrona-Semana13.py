print("**************************")
print("   Inicio del Programa")
print("**************************")
print()

#Lista de datos de cada integrante del grupo.
nombres=["Anderson","Rafa","Carlos","Jonathan","Anthony","Leo"]

anderson=["Anderson Juvini","Cisneros Quijada","Masculino","18 años","Chalatenango,","Nueva concepción", "Canton Potrero Sula Centro"]

rafa=["Rafael Edmundo","Salguero Dubon","Masculino","19 años","Chalatenango,","Nueva concepción","4 av sur barrio el rosario"]

carlos=["Carlos Manuel","Salguero Dubon","Masculino","17 años","Chalatenango,","Nueva Concepción","4° Avenida sur Barrio El Rosario"]

jonathan=["Jhonatan Enrique","Hernández Pineda","Masculino","19 años","Chalatenango,","La Reina","4av norte Barrio el centro"]

leo=["Juan Leonidas","Villafranco Sibrian","Masculino","19 años","Chalatenango,","Nueva Concepcion","8° calle poniente Barrio El Calvario"]

thony=["Anthony Dialessandro","Ortiz Calderon","Masculino","18 años","Chalatenango,","Nueva Concepcion","Lotificacion Prados de San Rafael" ] 

#Es la funcion que se encarga de ejecutar el programa completo 
def ejecutar_programa():
     
     #Muestra el listado del nombre de los integrantes
     print("Menu de Integrantes:")
     print()
     for i in nombres:
         print(f"✓ {i}")
     print()
     
     #Pedir el nombre del integrante
     menu=input("Ingresa el nombre posterior de uno de los integrantes:\n➣ ").lower()
     
     #Este bucle se encargara de repetir la interacción si el usuario ingresa un nombre equivocado
     while menu!="anderson" and menu!="rafa" and menu!="carlos" and menu!="jonathan" and menu!="anthony" and menu!="leo"  :

      print("[-] Error, Ingresa un nombre compatible")
      print()
      menu=input("Ingresa el nombre de uno de los integrantes:\n➣ ").lower()
     
     #Validar el nombre y mostrar al usuario los datos de dicho nombre 
     if menu=="anderson":
         print()
         print("Nombre:", anderson[0], anderson[1])
         print("Sexo:",anderson[2])
         print("Edad:",anderson[3])
         print("Departamento:",anderson[4],anderson[5])
         print("Direccion:",anderson[6])
         print()
         
     elif menu=="carlos":
         print()
         print("Nombre:", carlos[0], carlos[1])
         print("Sexo:",carlos[2])
         print("Edad:",carlos[3])
         print("Departamento:",carlos[4],carlos[5])
         print("Direccion:",carlos[6])
         print()
         
     elif menu=="rafa":
         print()
         print("Nombre:", rafa[0], rafa[1])
         print("Sexo:",rafa[2])
         print("Edad:",rafa[3])
         print("Departamento:",rafa[4],rafa[5])
         print("Direccion:",rafa[6])
         print()
         
     elif menu=="leo":
         print()
         print("Nombre:", leo[0], leo[1])
         print("Sexo:",leo[2])
         print("Edad:",leo[3])
         print("Departamento:",leo[4],leo[5])
         print("Direccion:",leo[6])
         print()

     elif menu=="anthony":
         print()
         print("Nombre:", thony[0], thony[1])
         print("Sexo:",thony[2])
         print("Edad:",thony[3])
         print("Departamento:",thony[4],thony[5])
         print("Direccion:",thony[6])
         print()

     else:
         print()
         print("Nombre:", jonathan[0], jonathan[1])
         print("Sexo:",jonathan[2])
         print("Edad:",jonathan[3])
         print("Departamento:",jonathan[4],jonathan[5])
         print("Direccion:",jonathan[6])
         print()
    
     #Consultar al usuario si desea consultar otro integrante del menú
     preguntar=input("¿Quieres consultar otro integrante? Ingresa '1' para SI o '2' para NO:\n➣ ")
     print()
        
     #Este bucle se encargara de repetir la interacción si el usuario no ingresa un numero solicitado
     while preguntar.isdigit()!=True or int(preguntar)>2 or  int(preguntar)==0:
         
      print("[-] Error, Digita un numero entre los solicitados")
      print()
      preguntar=input("Ingresa '1' para SI o '2' para NO:\n➣ ")
      print()
    
     #Ejecutar la funcion nuevamente
     if preguntar=="1":
         ejecutar_programa()
         
     #Finalizar el programa  
     else:
    
         print("Fin del Programa. Gracias Por Utilizarlo.")


print("Bienvenido. Feliz dia.")
print()
ejecutar=input("¿Quieres ejecutar la aplicacion?\n    Digita '1' para *SI*\n    Digita '2' para *NO*\n➣ ")

#El bucle se repite si el usuario no ingresa un numero solicitado o volver a preguntar.
while ejecutar.isdigit()!=True or int(ejecutar)>2 or  int(ejecutar)==0:
    print()
    print("[-] Error, Digita un numero entre los solicitados")
    print()
    ejecutar=input("¿Realmente deseas ejecutar el programa?\n    Digita '1' para *SI*'\n    Digita '2' para *NO*\n➣ ")
    
print()

#Si digita 1, ejecuta la funcion 
if ejecutar=="1":
    
    ejecutar_programa()
 
#Si digita 2, termina el programa 
elif ejecutar=="2":
    print("Fin del Programa")
