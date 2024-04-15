"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar
Retorne se o número é par ou ímpar
"""

def multiplicacao(*args):
    total = 1
    for n in args:
        total *= n
    return total

def par_impar(n):
    par = n % 2 == 0
    if par:
        return 'É par'
    else:
        return 'É ímpar'
    

p1 = multiplicacao(1, 2)
p2 = multiplicacao(5, 5)
p3 = par_impar(2)
p4 = par_impar(5)
p5 = par_impar(12)

print(p1, p2, p3, p4, p5)