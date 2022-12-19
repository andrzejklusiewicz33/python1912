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

#3. Niech użytkownik poda jakąś liczbę.
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


#przerwa do 11:40

#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.

wzrost = float(input('Podaj wzrost w metrach:\n'))
masa = float(input('Podaj masę w kilogramach:\n'))
bmi = round(masa / pow(wzrost, 2), 2)
print(f'bmi={bmi}')