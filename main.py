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


# 27. Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może
# być mniejsza niż 20 elementów) losowych liczb z zakresu 1-40.
# Wyswietl ich sumę, różnicę i część wspólną

# import random
# zbior1=set([random.randint(1,40) for _ in range(20)])
# zbior2=set([random.randint(1,40) for _ in range(20)])
# print(f'suma={zbior1.union(zbior2)}')
# print(f'część wspólna={zbior1.intersection(zbior2)}')
# print(f'z1-z2={zbior1.difference(zbior2)}')
# print(f'z2-z1={zbior2.difference(zbior1)}')
#
# import random
# zbior1= {random.randint(1,40) for _ in range(20)}
# zbior2={random.randint(1,40) for _ in range(20)}
# print(f'suma={zbior1.union(zbior2)}')
# print(f'część wspólna={zbior1.intersection(zbior2)}')
# print(f'z1-z2={zbior1.difference(zbior2)}')
# print(f'z2-z1={zbior2.difference(zbior1)}')

# przerwa do 13:04


# lista1=[1,'A']
# z1={
#     lista1,
#     [2,'B'],
#     [3,'C']
# }
# lista1[0]=10


# z1 = {
#     (1, 'A'),
#     (2, 'B'),
#     (2, 'B'),
#     (2, 'B'),
#     (3, 'C')
# }
# print(z1)

# 28. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.
#
# wynik=list(set([ tuple(linia.strip().split(';')) for linia in open('dane.csv',encoding='utf-8')]))
# for w in wynik:
#     print(w)
# print(type(wynik))

#
# for w in list(set([ tuple(linia.strip().split(';')) for linia in open('dane.csv',encoding='utf-8')])):
#     print(w)

#29.
# Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv
# dane z pliku dane.csv wzbogacone o obliczone BMI,
# bez duplikatów i rozwiązując problem  podania przecinka w miejsce kropki
# we wzroście i masie oraz problem z pustymi wierszami.


# plik=open('pliczek.txt',encoding='utf-8',mode='w')
# plik.write("1;Andrzej\n")
# plik.write("2;Czesio\n")
# plik.close()
#
# with open('pliczek.txt',encoding='utf-8',mode='w') as plik:
#     plik.write("1;Andrzej\n")
#     plik.write("2;Czesio\n")
# print('koniec')
#
# linia="1;Andrzej;Klusiewicz;1.76;80\n"
# lista=linia.strip().split(';')
# lista.append(str(25))
# print(lista)
# linia_csv=";".join(lista)
# print(linia_csv)

#
# lista=[ linia.replace(',','.').strip().split(';') for linia in open('dane.csv',encoding='utf-8') if len(linia.strip())>0]
# for e in lista:
#     e.append(str(round(float(e[4])/pow(float(e[3]),2),2)))
#
# wynik=list(set([tuple(e) for e in lista]))
#
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for w in wynik:
#         plik.write(";".join(w)+"\n")

# lista=[ linia.replace(',','.').strip().split(';') for linia in open('dane.csv',encoding='utf-8') if len(linia.strip())>0]
# for e in lista:
#     e.append(str(round(float(e[4])/pow(float(e[3]),2),2)))
#
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for w in list(set([tuple(e) for e in lista])):
#         plik.write(";".join(w)+"\n")
#
# sl=dict()
# sl['tekst']='wartość 1'
# sl['liczba']=123
# sl['lista']=[1,2,3]
# sl['krotka']=(1,2,3,4)
#
# print(sl['liczba'])
#
# print('############')
#
# # for k in sl.keys():
# #     print(k,sl[k])
#
# del sl['liczba']
# for k in sl:
#     print(k,sl[k])

# for v in sl.values():
#     print(v)

#print(conf['enconding'])

#30. Stwórz plik ustawienia.conf i umieść w nim poniższe dane
# encoding=utf-8
# timezone=-2
# color=black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

#
# sl=dict()
# for f in [e.strip().split('=') for e in open('ustawienia.conf',encoding='utf-8')]:
#     sl[f[0]]=f[1]
#
# for k in sl:
#     print(k,sl[k])
#
# print(sl['encoding'])


#przerwa do 14:24

#31. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone z nazwiskiem rozdzielone spacja,
# a pozostałe dane znalazły się w wartości
#jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość

#
# dane=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for d in dane:
#     sl[  d[1]+" "+d[2]  ]=(d[0],d[3],d[4])
#
# for k in sl:
#     print(k,sl[k])

# slownik=dict()
# slownik['klucz1']=123
# if 'klucz1' in slownik:
#     print('mamy taki klucz')
# else:
#     print('nie mamy takiego klucza')

#32. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc. i unifikację wielkości.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.
#
# Tadeusz
# Tadeusz,
# Tadeusz.
#
# Tadeusz
# tadeusz
# TADEUSZ
#
# lista=[
#     ('slowo1',5421),
#     ('slowo2',4566),
#     ('slowo',3321)
# ]
#
# tekst="siała, baba!, mak.?"
# niechciane=[',','.','!','?']
# for n in niechciane:
#     tekst=tekst.replace(n,'')
# print(tekst)
#
# plik = 'tadzio.txt'
# calosc = open(plik, encoding='utf-8').read()
#szukane = [ e.strip().split(" ") for e in calosc]
# tekst="siała baba mak"
# for l in tekst:
#     print(l)


#print(calosc[:10])
#
# import time
# poczatek=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['.',',','!','?','/',':',';','(',')','-','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# print(slowa)
# #poniżej złe rozwiązanie
# for s in slowa:
#     print(s,slowa.count(s))
# koniec=time.time()
# print(f'trwało to {koniec-poczatek} s')

#242s


# import time
# poczatek=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['.',',','!','?','/',':',';','(',')','-','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s in sl:
#         #sl[s]=sl[s]+1
#         sl[s]+=1
#     else:
#         sl[s]=1
# for k in sl:
#     print(k,sl[k])
# koniec=time.time()
# print(f'trwało to {koniec-poczatek} s')

#Przepakuj dane ze słownika do listy i posortuj (a następnie wypisz)

# import time
# poczatek=time.time()
# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# niechciane=['.',',','!','?','/',':',';','(',')','-','…']
# for n in niechciane:
#     calosc=calosc.replace(n,'')
# slowa=calosc.split()
# sl=dict()
# for s in slowa:
#     if s in sl:
#         #sl[s]=sl[s]+1
#         sl[s]+=1
#     else:
#         sl[s]=1
# wynik=[]
# for k in sl:
#     wynik.append([k,sl[k]])
# wynik.sort(key=lambda e:e[1], reverse=True)
# for w in wynik:
#     print(w)
# koniec=time.time()
# print(f'trwało to {koniec-poczatek} s')


# calosc=open('tadzio.txt',encoding='utf-8').read().lower()
# for n in ['.',',','!','?','/',':',';','(',')','-','…']:
#     calosc=calosc.replace(n,'')
# sl=dict()
# for s in calosc.split():
#     if s in sl:
#         sl[s]+=1
#     else:
#         sl[s]=1
# wynik=[]
# wynik=sorted([ [k,sl[k]] for k in sl],key=lambda e:e[1], reverse=True)
# for w in wynik:
#     print(w)
#
# import time
# def metryki(fun):
#     def wewnetrzna(*args,**kwargs):
#         p=time.time()
#         fun(*args,**kwargs)
#         k=time.time()
#         print(f"Funkcja {fun.__name__} wykonała się w {round(k-p,2)}s")
#
#     return wewnetrzna
# @metryki
# def koza():
#     time.sleep(1)
#     print('dupa')
#
# koza()

#
# f=metryki(fun)
# f()


#33. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
# for x in range(-10,11):
#     print(1/x)



# print('dupa1')
# print(1/0)
# print('dupa2')
# print(1/0)
# print('dupa3')
# print(1/0)
#
# print('przed')
# try:
#     print(1/0)
# except:
#     print('muka...')
# print('po')

# print('przed')
# try:
#     print(1/0)
#     print('po dzieleniu')
# except Exception as e:
#     print(f'muka...e={e} type(e)={type(e)}')
# print('po')

# print('przed')
# try:
#     print(1/0)
#     raise IndexError
#     print('po dzieleniu')
# except IndexError:
#     print('to się nie ma prawa zdarzyć')
# except ZeroDivisionError:
#     print('nie dziel przez zero...')
# except Exception as e:
#     print(f'muka...e={e} type(e)={type(e)}')
# print('po')

#34. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10 w taki
# sposob by w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic
# na konsoli informację o błędzie i przejsc do dalszego przetwarzania

# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'muka na wartości {x}')

#35. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie.
# W przypadku pojawienia się wyjątku na obliczaniu bmi dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;IOERROR


# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     try:
#         bmi=round(float(e[4])/pow(float(e[3]),2),2)
#         print(e,bmi)
#     except ValueError:
#         print(f'ValueError na {e}')
#         linia=";".join(e)+f";ValueError\n"
#         with open('bledy.csv',encoding='utf-8',mode='w') as plik:
#             plik.write(linia)

#
# for e in [ linia.strip().split(';') for linia in open('dane.csv',encoding='utf-8')]:
#     try:
#         print(e,round(float(e[4])/pow(float(e[3]),2),2))
#     except ValueError:
#         with open('bledy.csv',encoding='utf-8',mode='w') as plik:
#             plik.write(";".join(e)+f";ValueError\n")


#przerwa do 10:10

#
# def funkcja():
#     print('hello')
#
# funkcja()
#
# def dodawanie(x,y):
#     print(x+y)
#
# def dodawanie(x,y,z):
#     pass
#
# dodawanie(10,30)
#
# def oddaj_koze():
#     return 'koza'
#
# print(oddaj_koze())
# dane=oddaj_koze()
# print(dane)
#
# def pomnoz(x,y):
#     return x*y
#
#
# def pomnoz(x,y):
#     wynik=x*y
#     return wynik
#
# print(pomnoz(3,3))
#
# def wtf():
#     return 'omg'
#     print('lol')
#
# wtf()

# def bmi_opis(b):
#     if b<18.5:
#         return 'za chudy'
#     elif b<25:
#         return 'masa ok'
#     else:
#         return 'za niski'
#
# print(bmi_opis(30))


# def omg():
#     return 1,3
#
# x,y=omg()
# print(x,y)
# print(omg()[0])

#36. Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

# x=1.5
# if type(x)==float:
#     print('to je float')
# else:
#     print(f'to je typ {type(x)}')

# def bmi(w,m):
#     try:
#         return round(m/pow(w,2),2)
#     except ZeroDivisionError:
#         print('Podałeś zerowy wzrost')
#         return -1
#     except TypeError:
#         print('Jeden z podanych elementów nie jest liczbą')
#         return -2
#
# print(bmi(0,100))
# print(bmi('dupa',100))

#
# from faker import Faker
# f=Faker("PL_pl")
# for x in range(100):
#     print(f.first_name(),f.last_name(),f.email(),f.company(),f.phone_number(),f.paragraph())
#
#
# def funkcja(a,b):
#     print(f'a={a}')
#     print(f'b={b}')
#
# funkcja(1,2)
# funkcja(1)



# def funkcja(a,b="wartość domyślna"):
#     print(f'a={a}')
#     print(f'b={b}')
#
# funkcja(1,2)
# funkcja(1)


# def funkcja(b="wartość domyślna",a): #fuuuuuuu
#     print(f'a={a}')
#     print(f'b={b}')
#
# funkcja(1,2)
# funkcja(1)
#
# def funkcja(a,b='wartość domyślna dla b',c="wartość domyślna dla c",d="wartość domyślna dla d"):
#     print(f'a={a}')
#     print(f'b={b}')
#     print(f'c={c}')
#     print(f'd={d}')
#
# funkcja(10,c="whatever")

#37. Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
  # którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
  # podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie pdane ma przyjac utf-8.
  #Rozdzielacz kolumn ma być podawany jako trzeci argument funkcji, a jesli nie zostanie podany to ma przyjac ;

#
# def get_list(filename,enc='utf-8',delimeter=';'):
#     return [e.strip().replace(',','.').split(delimeter) for e in open(filename,encoding=enc) if len(e.strip())>0]
#
# for e in get_list('dane.csv'):
#     print(e)

#38. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.
