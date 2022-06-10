#s

while True:

    try:

        n1 = int(input("Escribe numero: "))

        n2 = int(input("Escribe otro numero numero: "))
        suma = n1+n2
        print(suma)

    except ValueError:
        
        print("Porfavor podes poner un numero")