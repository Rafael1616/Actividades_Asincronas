print()
print("Programa capturando datos desde el teclado")
print()

#Recolectar informacion con el tipo de dato Int
print("Multiplicacion con tipo de dato INT") 
print("------------------------------")
print()
var1=int(input("Ingresa un numero entero para multiplicar:"))
var2=int(input("Ingresa un segundo numero entero para multiplicar:"))
var3=int(input("Ingresa un tercer numero entero para multiplicar:"))

#Multiplicar las 3 variables
m=(var1*var2*var3)
print()
print(f"El resultado de la multplicacion de los 3 numeros ingresado es de: {m}")
print()

#Para la division
print()
print("Division con tipo de dato INT") 
print("------------------------------")
print()
div1=int(input("Ingresa un numero para divir:"))
div2=int(input("Ingresa un segundo numero para dividir:"))

#Dividir las variables ingresadas
d=(div1//div2)
print()
print(f"El resultado de la division de los 2 numeros ingresado es de: {d}")
print()

#sumar el resultado de la multiplicacion + la division
resultados=(m+d)
print(f"La sumatoria del resultado de la multiplicacion y division es: {resultados}")
print()


#Recolectar informacion con el tipo de dato Float

#Recolectar informacion con el tipo de dato Float, Exponencial
print()
print("Exponencial con tipo de dato FLOAT")
print("------------------------------")
print()
valor1=float(input("Ingresa un valor decimal o entero:"))
valor2=float(input(f"Ingresa ahora el valor por el ser elevado el numero {valor1}:"))
print()
#Formula
resul=(valor1**valor2)
print(f"El resultado de {valor1} elevado a la {valor2} es: {resul} ")
print()

#Modulo
print()
print("Modulo con tipo de dato FLOAT")
print("------------------------------")
print()
mod=float(input("Ingresa un numero para modular: "))
mod2=float(input("Ingresa un segundo numero para modular: "))


#Formula
dato=(mod%mod2)
print()
print(f"El resultado de {mod} modulado con {mod2} es: {dato} ")
print()

#Restar del resultado del metodo exponencial con el resultado del modulo
#Formula
resta=(resul-dato)
print(f"El resultado de la resta entre {resul} y {dato} = {resta}")
print()

#Division entre el resultado de la resta y la suma 
div=(resultados/resta)
print(f"La division de {resultados} entre {resta} = {div}")
print()

#Numeros complejos
print("Numeros complejos")
print()
cumple= 2 + 2j
cumple2= 10 - 3j
cumple3= 20 / 5j
cumple4= 10 * 5j

print(cumple)
print(cumple2)
print(cumple3)
print(cumple4)
print()


#Varibles con tipo de dato String

rafa="Papaya"
carlos="Durazno"
anderson="Banana"
leo="Manzana"
Jhonatan="Uva"
Anthony="Melon"

#Varible Boolean

fruta=input("Digita un nombre de una fruta (La primera letra mayuscula): ")

if fruta == rafa:
    
    print(f"{rafa} es la fruta que le gusta a Rafa")

else:
       if fruta==carlos:
         print(f"{carlos} es la fruta que le gusta a Carlos")
         
       else:
           
        if fruta==anderson:
            print(f"{anderson} es la fruta que le gusta a Anderson")
        
        else:  
                
            if fruta==leo:
              print(f"{leo} es la fruta que le gusta a Leo")
              
            else:
              if fruta==Jhonatan:
               print(f"{Jhonatan} es la fruta que le gusta a Jhonatan")
              
              else:
                
                if fruta==Anthony:
                 print(f"{Anthony} es la fruta que le gusta a Anthony")
                      
                else:           
                 print(f"Nadie del grupo le gusta la {fruta}")
        
 
