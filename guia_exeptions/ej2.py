#s

while True:
    try:
        n1 = int(input("pone un n: "))
        n2 = int(input("pone otro n: "))
        division = n1/n2
        print(division)
    except ZeroDivisionError:
        print("no se puede dividir por 0")