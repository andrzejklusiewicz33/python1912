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

# 12. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
# po     odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
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

# przerwa do 14:50
#
# lista=[]
# lista=list()
# lista=[1,'nietoperz','toperz',2]
# lista.append('dodane')
# print(lista,type(lista))
# for e in lista:
#     print(e)

# 13. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

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

# 14. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista albo +)

# import random
#
# l1 = []
# l2 = []
# for x in range(10):
#     l1.append(random.randint(1, 10))
#     l2.append(random.randint(1, 10))
#
# print(l1)
# print(l2)
# l3=l1+l2
# print(l3)
# l3=[*l1,*l2]
# print(l3)
# l1.extend(l2)
# print(l1)

# lista=[
#     [1,'A'],
#     [2,'B']
# ]
#
# for e in lista:
#     print(e)
#
# print(lista)

# lista=[]
# for x in range(1,11):
#     podlista=[x,x*1000]
#     lista.append(podlista)
#
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     lista.append(  [x,x*1000] )
#
# for e in lista:
#     print(e)

# 15. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# lista=[]
# for p in range(1,11):
#     lista.append(  [p,pow(2,p)] )
#
# print(lista)
# for l in lista:
#     print(l)
#
# lista=[]
# for e in range(1,11):
#     lista.append(e)
# print(lista)
#
# lista=[e for e in range(1,11)]
# print(lista)
#
# lista=[e*1000 for e in range(1,11)]
# print(lista)
#
# import random
# losowe=[random.randint(1,10) for e in range(10)]
# print(losowe)
#
#
# parzyste=[]
# for e in range(1,11):
#     if e%2==0:
#         parzyste.append(e)
# print(parzyste)
#
# parzyste=[e for e in range(1,11) if e%2==0]
# print(parzyste)
#
# parzyste=[e*1000 for e in range(1,11) if e%2==0]
# print(parzyste)
#
# lista=[e for e in range(1,11)]
# print(lista)
# druga=[e for e in lista if e%2==0]
# print(druga)
#
# print( [e for e in lista if e%2==0] )

# 16. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
#
# lista=[pow(2,e) for e in range(1,11)]
# print(lista)
#
# print([pow(2,e) for e in range(1,11)])
#
# for l in lista:
#     print(l)
#
# for l in [pow(2,e) for e in range(1,11)]:
#     print(l)
#
# print(list(range(10)))
# print(list(range(0,10)))
# print(list(range(1,11)))

# 17. Korzystając z list składanych wygeneruj listę 10 elementow której
# każdy element również będzie listą. Pierwszy element tej podlisty to numer potegi,
# a drugi to wartosc tej potegi dla liczby 2
#
# lista=[ [e,pow(2,e)] for e in range(1,11)]
# print(lista)
#
# linia='1;Andrzej;Klusiewicz;1.76;80'
# lista=linia.split(';')
# print(lista)
# print(lista[1])
# print(lista[1].upper())
# wzrost=float(lista[3])
# print(wzrost,type(wzrost))

# 18. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     #lista = linia.split(';').strip() #fuuuuu
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

# 19. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv
# w taki sposób   by linie oczyścic z bialych znaków i rozbić na listy.
# Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.

# wynik=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     wynik.append(lista)
#
# for w in wynik:
#     print(w)
#
# wynik=[ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# for w in wynik:
#     print(w)
#
# for w in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     print(w[4]*2)
#
# print("kotek "*10)
# get_data('dane.csv',';')


# for w in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     print(float(w[4])*2,type(w[4]),type(float(w[4])))

# 20. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika
# masa/power(wzrost,2)
#
# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     masa=float(e[4])
#     wzrost=float(e[3])
#     bmi=round(masa/pow(wzrost,2),2)
#     print(*e,bmi)

#
# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     bmi=round(float(e[4])/pow(float(e[3]),2),2)
#     print(*e,bmi)

#
# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     print(*e,round(float(e[4])/pow(float(e[3]),2),2))

#
# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     e.append(round(float(e[4])/pow(float(e[3]),2),2))
#     print(*e)
#
# lista=[1,6,2,9,3,2,6,5,1]
# lista.sort()
# print(lista)

#
# lista=[1,6,2,9,3,2,6,5,1]
# lista.sort(reverse=True)
# print(lista)


# lista=[1,6,2,9,3,2,6,5,1]
# lista.sort()
# lista.reverse()
# print(lista)
#
# lista=['6','22','11','2','1','koza']
# lista.sort()
# print(lista)

# lista=[1,6,2,9,3,2,6,5,1]
# druga=sorted(lista,reverse=True)
# print(druga)
#
# krotka=(1,6,2,9,3,2,6,5,1)
# print(krotka,type(krotka))
# #krotka.sort()
# #druga=sorted(krotka)
# druga=tuple(sorted(krotka))
# print(druga,type(druga))
# #druga=sorted(lista,reverse=True)
# #print(druga)

#
# lista=[1,6,2,9,3,2,6,5,1]
# wynik=[str(e) for e in lista]
# print(wynik)
#
# lista=[1,6,2,9,'nietoperz',3,2,6,5,1]
# wynik=[e for e in lista if type(e)==int]
# print(wynik)

# 21. ! Wygeneruj listę 10 elementów o losowej wartości liczbowej,
# posortuj listę i wyświetl jej zawartość linia po linii

# import random
# lista=[random.randint(1,1000) for _ in range(10)]
# print(lista)
# lista.sort()
# for e in lista:
#     print(e)
#
# import random
# lista=[random.randint(1,1000) for _ in range(10)]
# print(lista)
# for e in sorted(lista):
#     print(e)
#
# import random
# for e in sorted([random.randint(1,1000) for _ in range(10)]):
#     print(e)
#
# lista=[
#     [2,'A'],
#     [1,'B'],
#     [3,'D'],
#     [0,'C']
# ]
#
# lista.sort(reverse=True)
#
# for e in lista:
#     print(e)


# from operator import itemgetter
#
# lista=[
#     [2,'A'],
#     [1,'B'],
#     [3,'D'],
#     [0,'C']
# ]
#
# lista.sort(key=itemgetter(1))
#
# for e in lista:
#     print(e)

#
# lista=[
#     [2,'A'],
#     [1,'B'],
#     [3,'D'],
#     [0,'C']
# ]
#
# lista.sort(key=lambda e:e[1])
#
# for e in lista:
#     print(e)

#
# lista=[
#     [2,'A'],
#     [1,'B'],
#     [3,'D'],
#     [0,'C']
# ]
# kopia=sorted(lista,key=lambda e:e[1])
# for e in kopia:
#     print(e)

#
# lista=[
#     [2,'A'],
#     [1,'B'],
#     [3,'D'],
#     [0,'C']
# ]
# for e in sorted(lista,key=lambda e:e[1]):
#     print(e)

# SQLAlchemy
# Django ORM
#
# class Person:
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return str(self.__dict__)
#
# data=[Person("Eustachy","Enterman"),Person("Benek","Burczymucha"),Person("Stefan","Szymczyk")]
# data.sort(key=lambda p:p.last_name, reverse=True)
# for d in data:
#     print(d)

#
# class Person:
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return str(self.__dict__)
#
# data=[Person("Eustachy","Enterman"),Person("Benek","Burczymucha"),Person("Stefan","Szymczyk")]
# for d in sorted(data,key=lambda p:p.last_name, reverse=True):
#     print(d)
#
#
#
#
# class Person:
#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
#
# data = [Person("Eustachy", "Enterman"), Person("Benek", "Burczymucha"), Person("Stefan", "Szymczyk")]
#
# def sortowanie_person(p):
#     p.last_name=p.last_name.upper()
#     return p.last_name
#
# for d in sorted(data, key=lambda p:sortowanie_person(p), reverse=True):
#     print(d)
#


# 22.  Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po nazwiskach i wyswietl linia po linii na konsoli.
#
# lista=[linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8')]
# for e in sorted(lista,key=lambda e:e[2]):
#     print(e)

# przerwa do 10:28

# 23.Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi

#
# dane= [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]
# for d in dane:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
#
# dane.sort(key=lambda e:e[5],reverse=True)
# for d in dane:
#     print(d)


# tekst="siała baba mak"
# if "bab".lower() in tekst.lower():
#     print('jest baba w tekście')
# else:
#     print('nie ma baby w tekście')
# lista=tekst.split()
# print(lista)
#
# if "bab" in lista:
#     print('jest baba w liście')
# else:
#     print('nie ma baby w liście')
#
# for e in lista:
#     if 'bab' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')

#
# import os
# for e in os.walk("e:\\"):
#     print(e)

# 24.
# Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną
# frazę - wraz ze ścieżkami. Wyszukiwarka ma być nieczuła na wielkość liter
#
# import os
# katalog="e:\\"
# plik="oracle.jar"
# print( os.path.join(katalog,plik) )
# print( os.path.join(e[0],plik) )
#
# import os
# katalog_startowy=input('podaj katalog startowy:\n')
# szukane=input('podaj szukaną frazę:\n').lower()
# for e in os.walk(katalog_startowy):
#     for k in e[1]:
#         if szukane in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane in p.lower():
#             print(os.path.join(e[0],p))
#

#
# if "dupa".__contains__("d"):
#     print(1)
# else:
#     print(2)


# przerwa do 11:35

#
# krotka=(1,2,3,4,'koza',[1,4,'coś'])
#
# for k in krotka:
#     print(k)
#
# if 'koza' in krotka:
#     print('jest koza')

#
# krotka=(5,9,1,4,2,3,7)
# druga=sorted(krotka)
# print(druga)


# krotka=(5,9,1,4,2,3,7)
# druga=tuple(sorted(krotka))
# print(druga)
#
# krotka=(5,9,1,4,2,3,7)
# print(krotka)
# lista=list(krotka)
# print(lista)
# krotka2=tuple(lista)
# print(krotka2)

# 25. Stwórz dwie krotki.
# Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli
# import random
# krotka1=tuple([random.randint(1,10) for _ in range(10)])
#
# print(krotka1,type(krotka1))
#
# import random
# krotka1=tuple([random.randint(1,10) for _ in range(10)])
# krotka2=tuple([random.randint(11,20) for _ in range(10)])
# print(krotka1)
# print(krotka2)
# #krotka3=(*krotka1,*krotka2)
# krotka3=krotka1+krotka2
# print(krotka3)

# import random
# krotka1=(random.randint(1,10) for _ in range(10))
# print(*krotka1,type(krotka1))


# import random
# gen=(random.randint(1,10) for _ in range(10))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# for g in (random.randint(1,10) for _ in range(10)):
#     print(g)
# #
# import time
# def funkcja():
#     wynik=[]
#     for x in range(1,11):
#         time.sleep(1)
#         wynik.append(x)
#     return wynik
#
# for e in funkcja():
#     print(e)
# #

#
# import time
# def funkcja():
#     for x in range(1,11):
#         time.sleep(1)
#         yield f'element numer {x}'
#
# for e in funkcja():
#     print(e)

#
# def funkcja():
#     x=0
#     while True:
#         x+=1
#         yield x
#
# for f in funkcja():
#     print(f)

#
# tab=[]
# while True:
#     tab.append("terefere kuku")
#
# import random
# losowe=[random.randint(1,1000) for _ in range(1000)]
# print(losowe)
# print(f'suma={sum(losowe)}')
# print(f'max={max(losowe)}')
# print(f'min={min(losowe)}')
# print(f'max={sum(losowe)/len(losowe)}')

# 26. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv
#
# wynik= [ tuple(linia.strip().split(';')) for linia in open('dane.csv',encoding='utf-8')]
# print(wynik)

# zbior1={1,7,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4}
# zbior1.add(10)
# print(zbior1)


# lista=[1,7,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]
# print(lista)
# zbior=set(lista)
# print(zbior)
# lista=list(zbior)
# print(lista)
#
# lista=[1,7,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]
# lista=list(set(lista))
# print(lista)

# zbior1 = {1, 2, 3, 4, 5}
# zbior2 = {4, 5, 6, 7, 8}
# print(f'suma={zbior1.union(zbior2)}')
# print(f'część wspólna={zbior1.intersection(zbior2)}')
# print(f'z1-z2={zbior1.difference(zbior2)}')
# print(f'z2-z1={zbior2.difference(zbior1)}')


#27. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może
# być mniejsza niż 20 elementów) losowych liczb z zakresu 1-40.
# Wyswietl ich sumę, różnicę i część wspólną
