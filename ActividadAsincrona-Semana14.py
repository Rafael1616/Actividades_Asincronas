#Programa de busqueda de municipios por departamento 
 
 #Creamos este array para que almacene los departamentos 
depa = ["Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán", "La Libertad", "La Paz", "La Unión", "Morazán", "San Miguel", "San Salvador", "Santa Ana", "Sonsonate", "San Vicente", "Usulután"]

#Creamos este array para almacenar los municipios
array1=["Ahuachapán", "Atiquizaya", "Apaneca", "Turín", "Tacuba"]
array2=["Sensuntepeque", "Ilobasco", "Victoria", "San Isidro", "Dolores"]
array3=["Chalatenango", "La Palma", "La Reina", "San Rafael", "Nueva Concepcion"]
array4=["Cojutepeque", "Suchitoto", "San Rafael Cedros", "Candelaria", "San Ramón"]
array5=["Santa Tecla", "La Libertad", "Antiguo Cuscatlán", "Zaragoza", "Colón"]
array6=["Santiago Nonualco", "San Luis Talpa", "San Juan Nonualco", "Olocuilta"]
array7=["La Unión", "Intipucá", "Pasaquina", "San Alejo", "Conchagua"]
array8=["San Francisco Gotera", "Perquín", "Arambala", "Meanguera", "Jocoaitique"]
array9=["San Miguel", "Ciudad Barrios", "Chinameca", "Chapeltique", "Moncagua"]
array10=["San Salvador", "Soyapango", "Mejicanos", "Santa Tecla", "Delgado"]
array11=["Santa Ana", "Chalchuapa", "Metapán", "Coatepeque", "Texistepeque"]
array12=["Sonsonate", "Izalco", "Nahuizalco", "Acajutla", "Juayúa"]
array13=["San Vicente", "Tecoluca", "Zacatecoluca", "Verapaz", "Apastepeque"]
array14=["Usulután", "Santiago de María", "Jiquilisco", "Mercedes Umaña", "Nueva Granada"]

#Esta funcion ejecuta el programa 
def ejecutar_pogra():
     print("Departamentos a elegir: ")
     print()
#Imprime los departamentos
     for i in depa:
            print(f"✓ {i}")
     print()
     menu=input("Ingresa un departamento-> ").lower()
        
     while menu!="ahuachapan" and menu!="cabañas" and menu!="chalatenango" and menu!="cuscatlán" and menu!="la liberta" and menu!="la paz" and menu!="la unión" and menu!="morazán" and menu!="san miguel" and menu!="san salvador" and menu!="santa ana" and menu!="sonsonate" and menu!="san vicente" and menu!="usulutan":

      print("[-] Error, Ingresa un departamento compatible")
      print()
      menu=input("Ingresa un departamento de los que se encuentran en pantalla-> ").lower()
#Esta funcion valida el departamento ingresado
     if menu == "ahuachapan":
         for i in array1:
              print("Los municipios de Ahuchapan son: ", i)
     elif menu == "cabañas":
          for i in array2:
              print("Los municipios de Cabañas son: ", i)
     elif menu == "chalatenango":
          for i in array3:
              print("Los municipios de Chalatenango son: ", i)
     elif menu == "cuscatlan":
          for i in array4:
              print("Los municipios de Cuscatlan son: ", i)
     elif menu == "la libertad":
          for i in array5:
              print("Los municipios de La Libertad son: ", i)
     elif menu == "la paz":
          for i in array6:
              print("Los municipios de La Paz son: ", i)
     elif menu == "la union":
          for i in array7:
              print("Los municipios de La Union son: ", i)
     elif menu == "morazan":
          for i in array8:
              print("Los municipios de Morazan son: ", i)
     elif menu == "san miguel":
          for i in array9:
              print("Los municipios de San Miguel son: ", i)
     elif menu == "san salvador":
          for i in array10:
              print("Los municipios San Salvador son: ", i)
     elif menu == "santa ana":
         for i in array11:
              print("Los municipios de Santa Ana son: ", i)
     elif menu == "sonsonate":
          for i in array12:
              print("Los municipios de Sonsonate son: ", i)
     elif menu == "san vicente":
          for i in array13:
              print("Los municipios de San Vicente son: ", i)
     elif menu == "usulutan":
          for i in array14:
              print("Los municipios de Usulutan son: ", i)
#Esta funcion es por si deseas consultar otro departamento o finalizarlo
     Preguntar= input("Digita ¨1¨ para consultar otro departamento o ¨2¨ para finalizar: ")
     while Preguntar!="1" and Preguntar!="2":

      print("Error ingresa ¨1¨ o ¨2¨")
      Preguntar= input("Ingresa ¨1¨ si desea ejecutar el programa o ¨2¨ si deseas finalizar: ").lower()
     if Preguntar=="1":
      ejecutar_pogra()
     else : 
      print("Fin del programa")
#Esta funcion pregunta si deseas ejecutar el programa
Contenedor= input("Ingresa ¨SI¨ si desea ejecutar el programa o ¨NO¨ si deseas salir: ").lower()

while Contenedor!="si" and Contenedor!="no":
    
    print("Error ingresa ¨si¨ o ¨no¨")
    Contenedor= input("Ingresa ¨SI¨ si desea ejecutar el programa o ¨NO¨ si deseas salir: ").lower()
#Si el usuario Ingresa "Si" el programa se ejecutara
if Contenedor=="si":
    ejecutar_pogra()
#Si el usuario ingresa "No" el programa se finaliza
else : 
    print("Fin del programa")

