from cardapio import Cardapio


class Pedido:
    nomePedido = ""
    cardapios = []
    endereco = ""
    total = 0

    def setNome(self, nome):
        self.nomePedido = nome

    def setValor(self,endereco):
        self.endereco = endereco

    def setCardapios(self,cardapio):
        self.cardapios.append(cardapio)

    def somaPedido(self):

        for item in self.cardapios:
            self.total = self.total + item.valor

        return str(self.total)


#cardapio1 = Cardapio("xsalada", 10.00)
#cardapio2 = Cardapio("xbacon",15.00)
#cardapio3 = Cardapio("xmortadela",20.00)
#pedido = Pedido()
#pedido.setNome("felipe")

#pedido.cardapios.append(cardapio1)
#pedido.cardapios.append(cardapio2)
#pedido.cardapios.append(cardapio3)

#total = pedido.somaPedido()
#tipo = type(total)
#print(tipo)
