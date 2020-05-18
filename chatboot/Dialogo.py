class Dialogo:
    def __init__(self):
        self.opcoes = """        Olá, faça seu pedido.
        Digite [0]  para cancelar 
        Digite [1]  X-salada Valor : 7.50
        Digite [2]  X-bacon Valor : 10.00
        Digite [3]  x-mortadela Valor : 15.00
        Digite [4]  para prosseguir com o Pedido
        Digite [5]  para finalizar o Pedido"""

        self.solicitaNome = """Ola, digite seu nome e digite [0] para comfirmar."""


    def mostra(self):
        return  str(self.opcoes)




