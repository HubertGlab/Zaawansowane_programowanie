def czy_parzysta(num: int):
    if num % 2 == 0:
        return True
    else:
        return False


liczba = czy_parzysta(2)

if liczba:
    print("Liczba parzysta")
else:
    print("liczba nieparzysta")
