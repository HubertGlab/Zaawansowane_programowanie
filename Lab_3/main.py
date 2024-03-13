import Classes.Library as Lb
import Classes.Property as Pr
import Classes.Student as St

l1 = Lb.Library('Warszawa', 'Mikolaja Kopernika', '38-290', '8-20', 322421567)
l2 = Lb.Library('Buenos Aires', 'Gruszki', '21-410', '12-18', 533424883)

e1 = Lb.Employee('Juan', 'Espanol', '18.07.1960', '18.05.1940',
              'Katowice', 'Wadowicka', '18-190', 554344675)
e2 = Lb.Employee('Michal', 'Banan', '21.02.1970', '13.06.1940',
              'Gorzow', 'Michalska', '30-300', 123456789)
e3 = Lb.Employee('John', 'Gorlicki', '23.08.2000', '18.05.1980',
              'Michalice', 'Michalicka', '10-120', 332244189)

b1 = Lb.Book(l1, '07.07.1990', 'Michał', 'Gdanski', '120')
b2 = Lb.Book(l1, '02.03.2001', 'Henryk', 'Walski', '310')
b3 = Lb.Book(l2, '04.05.2002', 'Paweł', 'Szklarski', '400')
b4 = Lb.Book(l2, '04.02.2003', 'Patryk', 'Wolski', '800')
b5 = Lb.Book(l2, '08.09.2001', 'Henryk', 'Malobadzki', '112')

o1 = Lb.Order(e1, 'Andrzej Hubert', [b1, b2, b3], '07.07.2017')
o2 = Lb.Order(e2, 'Julia Juliowska', [b2], '07.07.2016')

print(o1)
print(o2)

house = Pr.House(1000, '60x40', 7, 20000, 'Juana 103')
flat = Pr.Flat(2, '20x30', 4, 10000, 'Dzulsa 200')

print(house)
print(flat)

s1 = St.Student("Madzia", [30, 60, 80, 90])

print(s1.is_passed())