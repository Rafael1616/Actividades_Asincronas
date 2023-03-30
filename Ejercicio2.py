print("TRES NUMERO DIGITADOS POR TECLADO")

num1 = int(input("Digita el primer numero: "))

num2 = int(input("Digita el segundo numero: "))

num3 = int(input("Digita el tercer numero: "))

if num1 > num2 and num2 > num3:
    print("El numero ",num1, " es el mas grande de los tres")
    print("El numero ",num2, " es el mediano de los tres")
    print("El numero ",num3, " es el mas pequeño de los tres")

elif num1 > num3 and num3 > num2: 
    print("El numero ",num1, " es el mas grande de los tres")
    print("El numero ",num3, " es el mediano de los tres")
    print("El numero ",num2, " es el mas pequeño de los tres")

elif num2 > num1 and num1 > num3:
    print("El numero ",num2, " es el mas grande de los tres")
    print("El numero ",num1, " es el mediano de los tres")
    print("El numero ",num3, " es el mas pequeño de los tres")

elif num2 > num3 and num3 > num1:
    print("El numero ",num2, " es el mas grande de los tres")
    print("El numero ",num3, " es el mediano de los tres")
    print("El numero ",num1, " es el mas pequeño de los tres")

elif num3 > num1 and num1 > num2:
    print("El numero ",num3, " es el mas grande de los tres")
    print("El numero ",num1, " es el mediano de los tres")
    print("El numero ",num2, " es el mas pequeño de los tres")

elif num3 > num2 and num2 > num1:
    print("El numero ",num3, " es el mas grande de los tres")
    print("El numero ",num2, " es el mediano de los tres")
    print("El numero ",num1, " es el mas pequeño de los tres")

else:
    print("ERROR!!!")

print("**fin del programa**")