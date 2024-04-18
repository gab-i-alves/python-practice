# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)

"""
As funções decoradoras em Python são um recurso avançado da linguagem que permitem adicionar comportamento adicional a uma função existente sem modificar o código original. Basicamente, uma função decoradora é uma função que recebe uma outra função como argumento e retorna uma nova função que contém o comportamento adicional.

Para entender melhor, imagine que você tem uma função que faz uma operação matemática simples, como somar dois números. Você pode querer adicionar uma verificação adicional para garantir que os números de entrada sejam do tipo correto antes de executar a soma. Em vez de modificar a função original, você pode criar uma função decoradora que realiza a verificação e depois chama a função original.

O exemplo de aplicação das funções decoradoras pode ser confuso no começo, mas é uma forma poderosa de estender e modificar o comportamento de funções em Python. É importante ter um bom entendimento de funções e closures em Python antes de tentar trabalhar com funções decoradoras, já que elas utilizam conceitos avançados da linguagem. Com prática e estudo, é possível entender e aproveitar bem esse recurso.
"""