#s

while True:
    try:

        n1 = int(input("Escribi una n: "))

        n2 = int(input("Escribi otra n: "))

        division = n1/n2

        print(division)

    except ZeroDivisionError:

        print("No se puede dividir por 0")
    except ValueError:

        print("Ingresa un numero valido:")
