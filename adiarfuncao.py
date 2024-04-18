# Exercício - Adiando execução de funções -> Closure

"""
    A função criar_funcao retorna uma função interna (interna) que utiliza a variável funcao e x da função externa. 
    Essa função interna é uma closure porque "lembra" do ambiente em que foi definida, ou seja, ela retém uma referência
    à função funcao e ao valor x mesmo após a função externa ter concluído sua execução.

    Quando você chama criar_funcao(soma, 5) ou criar_funcao(multiplica, 10), você está criando closures específicas que
    retêm as referências para as funções soma ou multiplica, juntamente com os valores 5 ou 10.

    As variáveis soma_com_cinco e multiplica_por_dez são essas closures especializadas, que podem ser chamadas 
    posteriormente com um argumento adicional (y), e elas usarão os valores x e a função funcao retidos para executar a operação desejada.

    Portanto, este código faz uso do conceito de closure para criar funções que encapsulam comportamentos específicos, 
    permitindo uma reutilização conveniente dessas funcionalidades especializadas.
"""

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))