#1. feladat

szamok = []
import random
def beker(inputIdx):

    szam = int(input(f"Kérem az {inputIdx}. páros számot:"))

    while not (szam % 2 == 0):
        szam = int(input("Ez nem páros! PÁROS számot kérek: "))

    return szam

def harom_paros_szam():
    inputIdx = 1

    while inputIdx <= 3:
        szam = beker(inputIdx)
        szamok.append(szam)
        inputIdx += 1

def legkisebb():
    i = 0
    minIdx = 0
    min = szamok[minIdx]

    while i < len(szamok):
        if szamok[i] < min:
            min = szamok[i]
            minIdx = i
        i += 1

    print(f"A legkisebb szám {min}, ami a {minIdx + 1}. helyen található.")


#2 feladat
import random
def veletlen_szamok():
    i = 1
    lista = []
    while i <= 13:
        vel = int(random.random() * 190) - 40
        lista.append(vel)
        i += 1
    print(lista)
    return lista

def ketjegyuek_szama(lista):
    i = 0
    ketjegyuDb = 0
    while i < len(lista):
        if lista[i] >= 10 and lista[i] < 100:
            ketjegyuDb += 1
        i += 1

    print(f"A kétjegyüek száma: {ketjegyuDb} db")
    return ketjegyuDb

def paros_osszege(lista):
    i = 0
    osszeg = 0

    while i < len(lista):
        if lista[i] % 2 == 0:
            osszeg += lista[i]
        i += 1

    print(f"A páros szűmok összege: {osszeg}")
    return osszeg

def paratlan_osszege(lista):
    i = 0
    osszeg = 0

    while i < len(lista):
        if not (lista[i] % 2 == 0):
            osszeg += lista[i]
        i += 1

    print(f"A páratlan számok összege: {osszeg}")
    return osszeg

lista = veletlen_szamok()
ketjegyuek_szama(lista)
parosOsszeg = paros_osszege(lista)
paratlanOsszeg = paratlan_osszege(lista)

#e
if parosOsszeg > paratlanOsszeg:
    print(f"A páros számok öszege nagyobb mint a páratlan számok összege! ({parosOsszeg} > {paratlanOsszeg})")
else:
    print(f"A páratlan számok öszege nagyobb mint a páros számok összege! ({paratlanOsszeg} > {parosOsszeg})")

#3.feladat
stadion_nev = []
varos = []
csapat = []
elso_indulas = []
utolso_indulas = []

def beolvas(fajlnev):
    fajl = open(fajlnev,'r', encoding='utf-8')
    print(fajl)










