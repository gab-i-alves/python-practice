"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

teste1 = duplicar(2)
teste2 = triplicar(2)
teste3 = quadruplicar(2)

print(teste1, teste2, teste3)