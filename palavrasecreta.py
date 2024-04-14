"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário
"""
import os

palavra_secreta = "Bala"
tentativas = 0
acertos = ''

while True:
    letra_input = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_input) > 1:
        print("Digite apenas uma letra!")
        continue

    if letra_input in palavra_secreta:
        acertos += letra_input
    
    palavra_formada = ''
    for letra_certa in palavra_secreta:
        if letra_certa in acertos:
            palavra_formada += letra_certa
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("Acertou!")
        print(f'A palavra era {palavra_secreta}')
        print(f'{tentativas} tentativas')
        acertos = ''
        tentativas = 0
