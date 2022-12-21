def get_list(filename,enc='utf-8',delimeter=';'):
    return [tuple(e.strip().replace(',','.').split(delimeter)) for e in open(filename,encoding=enc) if len(e.strip())>0]

def print_list(data):
    for d in data:
        print(d)

def lokata(hajs,oprocentowanie,ilosc_miesiecy):
    poczatkowo=hajs
    for m in range(1,ilosc_miesiecy+1):
        hajs=round(hajs+(hajs*oprocentowanie/12),2)
        print(m,hajs)
    return round(hajs-poczatkowo,2)

def bmi(w,m):
    try:
        return round(m/pow(w,2),2)
    except ZeroDivisionError:
        print('Podałeś zerowy wzrost')
        return -1
    except TypeError:
        print('Jeden z podanych elementów nie jest liczbą')
        return -2


print('inicjalizacja.....')

x=None