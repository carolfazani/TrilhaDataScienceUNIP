from random import randint
def somar(a, b):
    resultado = a + b
    return resultado

n = 1
while n != 0:
    n = randint(0, 5)
    n = somar(n, n)
    print(n)