"""
Faça uma lista de compras com listas
O usuário deve ter a posibilidade de inserir, apagar e listas valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista = []

while True:
    print("Selecione uma opção")
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == 'a':
        indice = input("Digite o índice que deseja apagar: ")
        try:
            indice = int(indice)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(lista) == 0:
            print("A lista está vazia")
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print("Por favor digite i, a ou l.")