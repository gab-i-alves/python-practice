# Calculadora

while (True):

    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    n_valido = None
    op_valido = "+-/*"

    try:
        n1 = float(n1)
        n2 = float(n2)
        n_valido = True
    except:
        n_valido = None

    if n_valido is None:
        print("Digite números válidos")
        continue

    op = input("Digite um operador: ")

    if op not in op_valido:
        print("Digite um operador válido")
        continue

    if len(op) > 1:
        print("Digite apenas um operador")
        continue

    if op == '+':
        print(f'{n1}+{n2}=', n1+n2)
    if op == '-':
        print(f'{n1}-{n2}=', n1-n2)
    if op == '*':
        print(f'{n1}*{n2}=', n1*n2)
    if op == '/':
        print(f'{n1}/{n2}=', n1/n2)

    sair = input("Deseja sair? [s]im ou Enter para continuar").lower().startswith("s")
    if sair is True:
        break