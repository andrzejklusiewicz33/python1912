# test
# przerwa do 10:16
#
# print('hello world!')
# print("hello world!")
# print("hello Mc'Donalds")
# #print 'dupa' #wersja 2, juz nie dziala #fuuuuuuu
# imie='Andrzej'
# print(imie)
# print(type(imie))
# imie=123
# print(imie)
# print('')

# imie="Andrzej"
# print('Siema, jestem '+imie+"!")
# x=10.5
# print(type(x))
# print("Siema, x wynosi "+x+"!")
#
# x=10.5
# y=2400
# #print("x="+str(x)+'!')
# print("x={} a y={}!".format(x,y))
# print(x,y)
# print(type(x))
# print(type(y))
# print(type(x),type(y))
# print("type(x)={} type(y)={}".format(type(x),type(y)))

#
# x=10.5
# y=2400
# print(f"x={x}, y={y}!")
# print(f"x={x} y={y}")

# x=input("Dej iksa:\n")
# print(x,type(x))
# #print(x/10)
# y=float(x)
# print(y,type(y))
# print(y/10)
# print(float(x)/10)
#
# x=1
# if x>0:
#     print('tak iks jezd wiekży od zera')
# else:
#     print('igz nie jezd wiekży od zera')
# print('koniec')

# print('whatever...')

# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
# imie=input('podaj imię:\n')
# print(f"imie={imie}")

# x=10
# x,y=10,20
#
# imie, nazwisko = input("Podaj swoje imie: "), input("Podaj swoje nazwisko: ")
# print(f"Witaj, twoje imie i nazwisko to: {imie} {nazwisko}")
# print(f'Witaj, Twoje imię i nazwisko to: '+imie+" "+nazwisko+"!")
#
# print(pow(1.76, 2))
# x = 1.5
# y = 100
# print(x / y)
# z=x/y
# print(z)


# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę w kilogramach
# i wzrost w metrach, wyliczy i wypisze BMI.
#
# x=float(  input('dej iksa:')  )
# print(x,type(x))

# wzrost = float(input('Podaj wzrost w metrach:\n'))
# masa = float(input('Podaj masę w kilogramach:\n'))
# bmi = round(masa / pow(wzrost, 2), 2)
# print(f'bmi={bmi}')

# x = -20
# if x > 10:
#     print('x>10')
#     print('...')
#     print('...')
#     print('...')
# else:
#     print('x<=10')
#     print('...')
#     print('...')
#     print('...')
# print('koniec')
#
# x=3
# if x==1:
#    print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# elif x==4:
#     print('cztery')
# else:
#     print('poza zakresem')

# 3. Niech użytkownik poda jakąś liczbę.
# Jeśli poda dodatnią to chcemy wyświetlić tę wartość z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero", jeśli ujemna to wyświetlamy "wartość ujemna".
#
# x=float(input('podaj x:'))
# if x>0:
#     print(f'{x} to wartość dodatnia')
# elif x==0:
#     print(f'{x} to zero')
# else:
#     print(f'{x} to wartość ujemna')


# przerwa do 11:40

# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.
#
# wzrost = float(input('Podaj wzrost w metrach:\n'))
# masa = float(input('Podaj masę w kilogramach:\n'))
# bmi = round(masa / pow(wzrost, 2), 2)
# print(f'bmi={bmi}')
#
# tekst=input('dej tekst:').replace(",",".")
# print(tekst)

# x=20
# y=20
# if x>10 and y>10:
#     print('oba wieksze od 10')
#
#
# if x>10 or y>10:
#     print('co najmniej jeden wiekszy od 10')

# wzrost = float(input('Podaj wzrost w metrach:\n'))
# masa = float(input('Podaj masę w kilogramach:\n'))
# bmi = round(masa / pow(wzrost, 2), 2)
# print(f'bmi={bmi}')
# if bmi<16:
#     print('wygłodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa prawidłowa')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('1 stopnień przypakowania')
# elif bmi<40:
#     print('2 stopień przypakowania')
# else:
#     print('3 stopień przypakowania')
#
# for x in range(10):
#     print('boom z bazuki')
#     print('dziura w podłodze')
#
#

# for x in range(10):
#     print(f'boom z bazuki x={x}')
#     print('dziura w podłodze')

# for x in range(1,11):
#     print(f'boom z bazuki x={x}')
#
# for x in range(1,11,2):
#     print(f'boom z bazuki x={x}')
# print(f'x po pętli: {x}')
#
# for x in range(1,11):
#     print(x*1000)

# 5. Wyświetl 20 kolejnych potęg liczby 2

# for p in range(1,21):
#     print(p,pow(2,p))


# for p in range(1,21): print(p,pow(2,p))

# for x in range(-10,11):
#     if x<0:
#         print(f'{x} jest ujemny')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest dodatni')

# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta

# print(11%2)
#
# for i in range(1,101):
#     if i%2==0:
#         print(f'{i} jest parzyste')
#     else:
#         print(f'{i} jest nieparzyste')

# import this

# 7.Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna

# hajs=100000

# x++ #het!
# x=x+1
# x+=1
#
# hajs=100000
# oprocentowanie=0.08
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     hajs=round(hajs+(hajs*oprocentowanie/12),2)
#     print(m,hajs)

#
# hajs=100000
# oprocentowanie=-0.2
# ilosc_miesiecy=60
# for m in range(1,ilosc_miesiecy+1):
#     hajs=round(hajs+(hajs*oprocentowanie/12),2)
#     print(m,hajs)

# przerwa obiadowa do 13:20

#
# while 1==1:
#     pass
#
# while True:
#     pass

# suma=0
# while suma<=1000:
#     print(suma)
#     suma=suma+100


# 8. Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej
# od wartosci podanej przez uzytkownika

# import random
# x=random.randint(1,100)
# y=random.random()
# print(x,y)

# import random
# suma=0
# max=int(input('podaj max zakres:'))
# while suma<max:
#     suma+=random.randint(1,10)
#     print(suma)

# import random
# suma=0
# max=int(input('podaj max zakres:'))
# while suma<max:
#     suma+=random.randint(1,10)
#     print(suma)

# import random
# suma=0
# max=int(input('podaj max zakres:'))
# while suma<max:
#     print(suma)
#     suma+=random.randint(1,10)
# tekst='siała BABA mak, nie wiedziała jak, dostała 10 lat bo nie płaciła VAT'
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(len(tekst))
# lista=[1,2,3,4]
# print(len(lista))
# print(tekst.replace('a','X'))
# print(tekst.lower().replace('a','X').replace('e','Y'))
# print(tekst.count('a'))
# print(tekst.lower().count('a'))
# if 'baba' in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')
# print("hajs "*10)
# print(tekst[0:11])
# print(tekst[10:21])
# print(tekst[10:21:2])
# if "Java">"Python":
#     print('chyba Cię gnie')
# else:
#     print('jasne że Python>Java')


# 9. Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z
# niego znaki ,.!? i wyświetli powiększony do dużych liter na konsoli
#
# tekst=input('podaj tekst:\n')
# tekst=tekst.replace(',','').replace('.','').replace('!','').replace('?','').upper()
# print(tekst)


# tekst=input('podaj tekst:\n').replace(',','').replace('.','').replace('!','').replace('?','').upper()
# print(tekst)

# print(input('podaj tekst:\n').replace(',','').replace('.','').replace('!','').replace('?','').upper())


#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)


#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())


# 10. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego
# nazwę poda użytkownik
#
# nazwa_pliku=input('podaj nazwę pliku:\n')
# for linia in open(nazwa_pliku,encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(len(linia.strip()),linia.strip())

# calosc=open('tadzio.txt',encoding='utf-8').read()
# print(calosc.replace('a','X'))

# 11. Napisz program który zliczy ilość wystąpień małej
# lub dużej wersji ciagu tekstowego podanego przez użytkownika
# w pliku którego nazwę również poda użytkownik.
#
# szukane = 'TADEUSZ'
# plik = 'tadzio.txt'
# calosc = open(plik, encoding='utf-8').read()
# x = calosc.lower().count(szukane.lower())
# print(x)

#
# szukane = input('podaj szukaną frazę:\n')
# plik = input('podaj nazwę pliku:\n')
# calosc = open(plik, encoding='utf-8').read()
# x = calosc.lower().count(szukane.lower())
# print(f'Jest {x} wystąpień słowa "{szukane}" w pliku "{plik}"')

#
# linia='siała BABA mak'
# if 'BAba'.lower() in linia.lower():
#     print('jest')
# else:
#     print('nie ma')

#12. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
 # poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
 #  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
 #po     odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
 #  i w jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.

# szukane='Tadeusz'
# plik='tadzio.txt'
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower():
#         print(x,linia.strip())

# szukane='TADEUSZ'
# plik='tadzio.txt'
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower():
#         print(x,linia.strip())

# szukane=input('podaj szukaną frazę:\n')
# plik=input('podaj plik do wyszukiwania:\n')
# x=0
# for linia in open(plik,encoding='utf-8'):
#     x+=1
#     if szukane.lower() in linia.lower():
#         print(x,linia.strip())

#przerwa do 14:50
#
# lista=[]
# lista=list()
# lista=[1,'nietoperz','toperz',2]
# lista.append('dodane')
# print(lista,type(lista))
# for e in lista:
#     print(e)

#13. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
#Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

#
# lista=[]
# for p in range(1,11):
#     lista.append(  pow(2,p)  )
#
# for e in lista:
#     print(e)
#
# print(lista)

# lista1=[1,2,3,4]
# lista2=lista1
# lista1.clear()
# print(lista1)
# print(lista2)

# lista1=[1,2,3,4]
# lista2=lista1.copy()
# lista1.clear()
# print(lista1)
# print(lista2)
#
# lista=[1,2,3,4]
# print(lista)
# print(*lista)

# def funkcja(*args):
#     pass

#
# lista=[1,2,3,4]
# print(lista)
# lista2=[*lista]
# print(lista2)


# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)
#
# l1=[1,2,3]
# l2=[4,5,6]
# l3=[*l1,*l2]
# print(l3)

# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)

#14. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista albo +)

