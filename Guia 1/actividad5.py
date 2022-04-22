def palindromo() -> bool:
    word = str(input("Ingresa una palabra : "))

    if word == word[::-1]:
        return True
    else:
        return False
