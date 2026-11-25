print("=================================")
print("MI CALCULADORA DE TEMU DEL TIO")
print("=================================")

while True:
    print("")
    print("¿Que operacion sale?")
    print("1.multiplicar")
    print("2.division")
    print("3.salir")
    print("----------------------")

    opcion = input("elige una opcion")

    if opcion == "1":
        num1 = input("ingresa el primer numero:")
        num1 = int(num1)
        num2 = input("ingresa el segundo numero:")
        num2 = int(num2)
        print("el resultado de la multiplicacion:",num1*num2)

    elif opcion == "2":
        num1 = input("ingresa el primer numero: ")
        num1 = int(num1)
        num2 = input("ingresa el segundo numero: ")
        print("el resultado de la multiplicacion es",num1*num2)

    elif opcion == "3":
        print("¡graciaspor usar la calculadora¡")
        break

    else:print("opcion incorrecta")
    print("================================")

