# a

lista_a = ['Tomek', 'Grzegorz', 'Jacek', 'Krystyna', 'Magdalena']


def wysw_imion(lista):
    if len(lista) == 5:
        for name in lista:
            print(name)


# wysw_imion(lista_a)

# b)

lista_b = [1, 2, 3, 4, 5]


def mnoz_liczb(lista):
    liczby2 = []
    if len(lista) == 5:
        for liczba in lista:
            liczba = liczba * 2
            liczby2.append(liczba)
    return liczby2


# print(mnoz_liczb(lista_b))


def mnoz_liczb2(lista):
    if len(lista) == 5:
        lista_mnoz = [i * 2 for i in lista]
    return lista_mnoz


# print(mnoz_liczb2(lista_b))

# c)

lista_c = [*range(0, 10)]


def parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)


# parzyste(lista_c)

# d)

lista_d = [*range(0, 10)]


def co_drugie(lista):
    for liczba in range(0, len(lista), 2):
        print(lista[liczba])

# co_drugie(lista_d)
