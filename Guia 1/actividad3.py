print("ingrese el ancho del rectangulo")
ancho = int(input())
print("ingrese el alto del rectangulo")
alto = int(input())
print("ingrese el caractear que va a usar el rectangulo")
caracter = str(input())


def rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(ancho * caracter)


rectangulo(ancho, alto, caracter)

# s#
