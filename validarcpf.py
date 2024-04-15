"""
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:                              70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10:                301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11:      3010 % 11 = 7
Se o resultado anterior for maior que 9:                resultado é 0
Caso contrário disso:                                   resultado é o valor da conta

Cálculo do segundo dígito do CPF
Colete a soma ds 9 primeiros dígitos do CPF + O PRIMEIRO DÍGITO multiplicando cada um dos valores por uma contagem
regressiva começando de 11

"""
import re # regular expressions
import sys

cpf_input = input('Digite um CPF: ')
cpf_input = re.sub(
    r'[^0-9]',
    '',
    cpf_input
)

cpf_sequencial = cpf_input == cpf_input[0] * len(cpf_input)
if cpf_sequencial:
    print("CPF sequencial não é válido")
    sys.exit()

# Primeiro dígito
nove_digitos = cpf_input[:9]
cont1 = 10
result1 = 0

for digito1 in nove_digitos:
    result1 += int(digito1) * cont1
    cont1 -= 1

digito1 = (result1 * 10) % 11
digito1 = 0 if digito1 > 9 else digito1
print(f'O primeiro dígito é {digito1}')

# Segundo dígito
dez_digitos = nove_digitos + str(digito1)
cont2 = 11
result2 = 0

for digito2 in dez_digitos:
    result2 += int(digito2) * cont2
    cont2 -= 1

digito2 = (result2 * 10) % 11
digito2 = 0 if digito2 > 9 else digito2
print(f'O segundo dígito é {digito2}')

# Validação CPF
cpf_gerado = f'{nove_digitos}{digito1}{digito2}'

if cpf_gerado == cpf_input:
    print(f'{cpf_input} é válido.')
else:
    print('CPF inválido.')