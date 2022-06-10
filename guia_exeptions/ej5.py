#s

try:    

    valor = input("Indica el valor: ")
    file = open('readme.txt', 'w')
    file.write("Funciono")

    if valor.isnumeric() == True:
        file.write(int(valor))
    else: 

        file.write(valor)
    file.close()
    file = open('readme.txt', 'r')
    print(file.read())
    file.close()
except TypeError:

    
    file = open('readme.txt', 'w')
    file.write("Funciono pero con un problema")

    file.close()

    file = open('readme.txt', 'r')


    print(file.read())
    file.close()