def postfija(expresion):
    pila = []
    for elemento in expresion:
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            num2 = pila.pop()
            num1 = pila.pop()
            if elemento == '+':
                resultado = num1 + num2
            elif elemento == '-':
                resultado = num1 - num2
            elif elemento == '*':
                resultado = num1 * num2
            elif elemento == '/':
                resultado = num1 / num2
            pila.append(resultado)
    return pila.pop()

def prefija(expresion):
    pila = []
    for elemento in expresion[::-1]:
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            num1 = pila.pop()
            num2 = pila.pop()
            if elemento == '+':
                resultado = num1 + num2
            elif elemento == '-':
                resultado = num1 - num2
            elif elemento == '*':
                resultado = num1 * num2
            elif elemento == '/':
                resultado = num1 / num2
            pila.append(resultado)
    return pila.pop()

def tipo_notacion():
    while True:
        print("\nCalculadora de notaciones postfijo y prefijo")
        print("\nOpciones:")
        print("1. Notación postfija")
        print("2. Notación prefija")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            operacion = input("Ingrese la operación en notación postfija: ").strip()
            resultado = postfija(operacion)
        elif opcion == '2':
            operacion = input("Ingrese la operación en notación prefija: ").strip()
            resultado = prefija(operacion)
        elif opcion == '3':
            print("Saliendo del programa...\n")
            break
        else:
            print("Algo salió mal, intente ingresando de nuevo.")
            continue  

        print(f"El resultado de la operación es: {resultado}")

tipo_notacion()