import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    cont1 = 10
    result1 = 0

    for digito1 in nove_digitos:
        result1 += int(digito1) * cont1
        cont1 -= 1

    digito1 = (result1 * 10) % 11
    digito1 = 0 if digito1 > 9 else digito1

    # Segundo dígito
    dez_digitos = nove_digitos + str(digito1)
    cont2 = 11
    result2 = 0

    for digito2 in dez_digitos:
        result2 += int(digito2) * cont2
        cont2 -= 1

    digito2 = (result2 * 10) % 11
    digito2 = 0 if digito2 > 9 else digito2

    cpf_gerado = f'{nove_digitos}{digito1}{digito2}'

    print(cpf_gerado)