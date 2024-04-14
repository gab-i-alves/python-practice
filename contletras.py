frase = 'aaaabbbbccccDDDDDDDDDDddddddd'

i = 0
count = 0
letra = ''

while i < len(frase):
    atual = frase[i]

    if atual == ' ':
        i += 1
        continue

    count_atual = frase.count(atual)

    if count_atual >= count:
        count = count_atual
        letra = atual

    i += 1

print(f'A letra que apareceu mais vezes foi {letra} que apareceu {count}x.')