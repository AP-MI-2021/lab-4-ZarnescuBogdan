def gasesteSirDeCaractere(l, sirCautat):
    '''
    Determina daca un sir de caractere se gaseste in lista.
    :param l: lista[str]
    :param sirCautat: str, sirul pe care il cautam in lista.
    :return: True, daca sirul cautat se gaseste in lista, respectiv False, in caz contrar.
    '''
    ok = 0
    for x in l:
        if x == sirCautat:
            return 'DA'
    return 'NU'

def testGasesteSirDeCaractere():
    assert gasesteSirDeCaractere(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'drd') == 'DA'

def siruriRepetate(l):
    '''
    Creeaza o lista cu toate sirurile de caractere care se repeta in lista data.
    :param l: lista[str]
    :return: O lista noua cu toate sirurile de caractere care se repeta in lista data.
    '''
    rezultat = []
    for x in l:
        nrAp = 0
        for y in l:
            if x == y:
                nrAp = nrAp + 1
        if nrAp > 1 and rezultat.count(x) == 0:
            rezultat.append(x)
    if len(rezultat) > 0:
        return rezultat
    else:
        return 'UNIC'

def testSiruriRepetate():
    assert siruriRepetate(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa']
    assert siruriRepetate(['aaa', 'bbb', 'ccc']) == 'UNIC'

def listaPalindroame(l):
    '''
    Determina sirurile de caractere din lista care sunt palindroame.
    :param l: lista[str]
    :return: O lista cu sirurile de caractere care sunt palindroame.
    '''
    rezultat = []
    for x in l:
        xInversat = x[::-1]
        if x == xInversat:
            rezultat.append(x)
    return rezultat

def testListaPalindroame():
    assert listaPalindroame(['ada', 'abc', 'cmtc', 'drd', 'aaa']) == ['ada', 'drd', 'aaa']
    assert listaPalindroame(['ada', 'abc', 'cmtc', 'drd', 'aaa', 'ada']) == ['ada', 'drd', 'aaa', 'ada']

def procesareLista(l):
    '''
    Determina lista obținută prin înlocuirea șirurilor care conțin caracterul care apare de cele mai
     multe ori în toată lista cu numărul de apariții ale acestui caracter.
    :param l: lista[str]
    :return: lista obținută prin înlocuirea șirurilor care conțin caracterul care apare de cele mai
             multe ori în toată lista cu numărul de apariții ale acestui caracter.
    '''
    caractere = []
    if len(l) > 0:
        for i in range(len(l)):
            for j in range(len(l[i])):
                caractere.append(l[i][j])
    caractere.sort()
    nrApMax = 1
    nrAp = 1
    indexCaracter = 0
    caracter = caractere[0]
    for i in range(len(caractere) - 1):
        if caractere[i] != caractere[i + 1]:
            if nrAp > nrApMax:
                nrApMax = nrAp
                indexCaracter = i
                caracter = caractere[i]
            nrAp = 1
        else:
            nrAp = nrAp + 1
    if caractere[len(caractere) - 2] == caractere[len(caractere) - 1]:
        if nrAp > nrApMax:
            nrApMax = nrAp
            indexCaracter = len(caractere) - 1
            caracter = caractere[len(caractere) - 1]
    for i in range(len(l)):
        ok = 0
        for j in range(len(l[i])):
            if l[i][j] == caracter:
                ok = 1
                break
        if ok == 1:
            l[i] = nrApMax
    return l

def testProcesareLista():
    assert procesareLista(['aaa', 'bbab', 'caamtc', 'drd', 'aaa']) == [9, 9, 9, 'drd', 9]

def readList():
    givenStr = input('Dati elementele listei, separate printr-o virgula: ')
    numbersAsStr = givenStr.split(',')
    return numbersAsStr


def testAll():
    testGasesteSirDeCaractere()
    testSiruriRepetate()
    testListaPalindroame()
    testProcesareLista()


def printMenu():
    print('1. Citirea unei liste de numere intregi.')
    print('2. Afișați dacă un șir de caractere citit de la tastatură se găsește în listă. Dacă se găsește șirul, se'
          'va afisa DA, dacă nu se găsește șirul atunci se va afișa NU.')
    print('3. Afișați o listă cu toate șirurile de caractere care se repetă în listă (apar de cel puțin două ori).'
          'Dacă nu exista niciun șir de acest gen, afișați UNIC.')
    print('4. Afișați toate șirurile de caractere din lista care sunt un palindrom.')
    print('5. Afișați lista obținută prin înlocuirea șirurilor care conțin caracterul care apare de cele mai'
          'multe ori în toată lista cu numărul de apariții ale acestui caracter.')
    print('a. Afisarea listei.')
    print('x. Iesire.')


def main():
    l = []
    while True:
        printMenu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            l = readList()
        elif optiune == '2':
            sirCautat = input('Dati sirul: ')
            print(gasesteSirDeCaractere(l, sirCautat))
        elif optiune == '3':
            print(siruriRepetate(l))
        elif optiune == '4':
            print(listaPalindroame(l))
        elif optiune == '5':
            print(procesareLista(l))
        elif optiune == 'a':
            print(l)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida! Reincercati: ')

testAll()
main()
