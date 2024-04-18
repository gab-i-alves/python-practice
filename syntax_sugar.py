# Essa é uma função decoradora que recebe outra função:
def minha_decoradora(func):
    # Essa é a função que vai ser decorar a funcao_original(q estou recebendo como params) e ser executada em seu lugar.
    def funcao_decorada():  
        print(f'Antes da função {func.__name__} ser executada')
        func()  # chamando a função recebida nos params
        print(f'Depois da função {func.__name__} ser executada')
    return funcao_decorada  # retornando a função decorada 
     
# Agora criei a função_original que é a função que vai ser decorada pela função decoradora:
     
@minha_decoradora  # syntax sugar para dizer que a função a seguir será a função que minha decoradora irá receber como params
def funcao_original():
    print('Minha função original')
     
funcao_original()
