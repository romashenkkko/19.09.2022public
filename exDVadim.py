import math

a=int(input('Introdu primul  numar: '))
b=int(input('Introdu al doilea numar:  '))

def Suma():
    return (a + b)

print('a) Suma: ', Suma())

def Produs():
    return (a * b)

print('b) Produs: ', Produs())

def Media():
    return (a + b)/2

print('c) Media aritmetica:', Media())


def Divizor(a, b):
    return math.gcd(a, b)

print('d) Cel mai mare divizor comun ', Divizor(a, b))



def Minim(a, b):
    return min(a, b)

print('f) Minim ', Minim(a, b))

def Maxim(a, b):
    return max(a, b)
print('g) Maximum ', Maxim(a, b))


def SumNmCitite():
    
    a = int(input('a '))
    b = int(input('b '))
    c = a + b
    return c

print('h) a', '+', 'b', '=', SumNmCitite())

def ProdusNmCitite():
    a = int(input('a '))
    b = int(input('b '))
    c = a + b
    return c
print('i) a', '*', 'b', '=', ProdusNmCitite())

def DivizorComun(a, b):
    divizor = 0
    print("j) Divizorii comuni pentru ", a, " si ", b, " sunt ")
    for i in range(1,min(a, b)+1):
        if (a % i == 0) and (b % i == 0):
            divizor = i
        print(divizor)
    return i
print(DivizorComun(a, b))


def MultipliComuni(a, b):
    multiplii =[]
    for i in range(1, b ** 5):
        for j in range(1, a ** 5):
            if b * i == a * j:
                multiplii.append(b * i)
            if len(multiplii) == 5:
                return multiplii
                
print('k) 5 Multipli comuni ', MultipliComuni(a, b))

def CifreComune(a, b):
    while a > 0:
        d = a % 10
        a//=10
        c = b
        while c > 0:
            if c % 10 == d:
                print("l) Cifra comuna in ambele ", d)
            c//=10
  
print(CifreComune(a, b))


def CifreUnice(a, b):
    listaA = [x for x in str(a)]
    listaB = [y for y in str(b)]
    cifre_unicale = []
    for i in str(a):
        if (i in listaA) and (i not in listaB):
            cifre_unicale.append(i)
    return cifre_unicale

# print(CifreUnice(a, b))
print ('m) Sunt in primul, dar nu in al 2 lea ', CifreUnice(a, b))


def VerifyDivisors(a, b):
    divA = len([i for i in range(1, a + 1) if not a % i])
    divB = len([j for j in range(1, b + 1) if not b % j])
    if divA == divB:
        return "Prietene"
    else:
        return "Nu sunt prietene"
        
print("n) ", VerifyDivisors(a, b))