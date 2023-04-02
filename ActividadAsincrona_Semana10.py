#Programa que permita al usuario procesar los montos de las compras de un cliente.
print("**********************************************")
print("               Bucle While")
print("**********************************************")
print()

#Digite el numero de compras a realizar.
valor = int(input("Digita el numero de compras que desea realizar: "))
print()
resultado = 0
x = 0
#Digite el nombre y el precio de cada producto.
while x < valor:
    x += 1
    nombre = input("Digite el nombre del producto: ")
    precio = int(input("Digite el precio del producto: "))
    print()
    resultado = resultado + precio

# En este proceso se realizara un descuento al total a pagar, si este supera sierta cantidad de dinero.
if resultado >= 0 and resultado <= 500:
    print("Total de la compra: ",resultado)
    print()
    print("No aplicaste a un descuento tu monto a pagar es: ",resultado)

elif resultado > 500 and resultado <= 1000:
    print("Total de la compra: ",resultado)
    print()
    formula = resultado * 0.05
    formula2 = resultado - formula
    print("Tienes un descuento del 5% por el total de la compra, tu nuevo monto a pagar es: ",formula2)

elif resultado > 1000:
    print("Total de la compra: ",resultado)
    print()
    formula1 = resultado * 0.10
    formula3 = resultado - formula1
    print("Tienes un descuento del 10% por el total de la compra, tu nuevo monto a pagar es: ",formula3)

else:
    resultado <= 0
    print("'*ERROR* Monto no valido'")
print()

print("Fin del programa")
