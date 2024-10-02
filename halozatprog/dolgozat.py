import random
vezetek = input("Írja be a vezeték nevét!")
kereszt = input("Írja be a keresztnevét!")
print("Üdvözöllek",vezetek,kereszt)
szam = int(input("Adjon meg egy számot!"))

print(szam-1, szam+1)
if szam % 2 == 0:
    print("A szam paros")
else:
    print("A szam paratlan")
lista = []
i = 0
while 10 > i:
    i = i+1
    lista.append(random.randint(1,51))
print(sum(lista))
print(sum(lista)/2)
print(lista)
a = int(input("Adja meg a értékét!"))
b = int(input("Adja meg b értékét!"))
c = (2*a+3*b)
d = c-2*a-3*b
print(c,d)