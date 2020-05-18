from whatssapWeb import WhatssapWeb
from Dialogo import Dialogo
from cardapio import Cardapio
from Pedido import Pedido
import PalavrasChaves
import time

opcao1 = Cardapio("X-salada", 7.50)
opcao2 = Cardapio("X-bacon", 10.00)
opcao3 = Cardapio("X-mortadela", 15.00)

arrayPedidos = []
whats = WhatssapWeb()
dir = Dialogo()
whats.buscaUrl()
time.sleep(10)

#dialogos = whats.getDialogo()

def buscaPedido(nome):
    pedidoCliente = "null"
    if len(arrayPedidos) > 0 :
        for pedido in arrayPedidos:
            if pedido.nomePedido == nome:
                pedidoCliente = pedido

    return pedidoCliente

def criaPedido(nome):
    pedido = Pedido()
    pedido.setNome(nome)
    arrayPedidos.append(pedido)


def iniciaDialogo(entrada,nome):
        pedido = "null"
        entendi = False

        res = buscaPedido(nome)
        if res != "null":
           pedido = res
        else:
           criaPedido(nome)
           pedido = buscaPedido(nome)

        for palavra in PalavrasChaves.inputs:  # PALAVRAS DE QUE INICIAM O PEDIDO

            if (entrada == palavra):
                entendi = True
                res = dir.mostra()
                print(res)
                whats.response(res)
                whats.sendMesage()

        if entrada == "0":
            whats.response("OK! Obrigado pelo contato.")
            whats.sendMesage()

        if entrada == "1":
                 pedido.setCardapios(opcao1)
                 #arrayPedidos.append(opcao1)
                 whats.response("Você escolheu :" + opcao1.nome + ", valor : " + str(format(opcao1.valor,'.2f')))
                 whats.sendMesage()


        if entrada == "2":
                #arrayPedidos.append(opcao2)
                pedido.setCardapios(opcao2)
                whats.response("Você escolheu :" + opcao2.nome + ", valor : " + str(format(opcao2.valor,'.2f')))
                whats.sendMesage()


        if entrada == "3":
                pedido.setCardapios(opcao3)
                #arrayPedidos.append(opcao3)
                whats.response("Você escolheu :" + opcao3.nome + ", valor : " + str(format(opcao3.valor,'.2f')))
                whats.sendMesage()


        if entrada == "4":
            whats.response("Desculpe! função ainda esta em desenvolvimento ")
            whats.sendMesage()


        if entrada == "5":
            nome = pedido.nomePedido
            car = ""
            total = 0
            cardapios = pedido.cardapios
            for cardapio in cardapios:
                car = car + cardapio.nome + " , " + str(format(cardapio.valor,".2f")) + "\n"
                total = total + cardapio.valor

            whats.response("Segue abaixo seu Pedido \n Cliente : " + nome)
            whats.sendMesage()
            whats.response(car + "\n Valor total do pedido: " + str(format(total,".2f")) + "\n Tempo estimando para entrega depende da quantidade de itens no Pedido e a distância do endereço,peço a compreenção e obrigado pela preferência.")
            whats.sendMesage()

        if entendi != True and \
           entrada != "0" and \
           entrada != "1" and \
           entrada != "2" and \
           entrada != "3" and \
           entrada != "4" and \
           entrada != "5" and \
           entrada != "6" and \
           entrada != "7":
            whats.response("Desculpe! Não entendi.")
            whats.sendMesage()




sair = ""
while sair != "0":
    dialogos = whats.getDialogo()
    for dialogo in dialogos:

            try:

                div4 = whats.pegaNomaMnesagem(dialogo)
                if (div4):
                    dialogo.find_element_by_class_name("_1wjpf").click()

                    div6 = whats.pegaInput(dialogo)
                    name = whats.pegaNome(dialogo)
                    entrada = div6
                    print(entrada)
                    iniciaDialogo(entrada,name)

            except:
                print("nao tem mensagem.")

            name = whats.pegaNome(dialogo)
            if name and name == "Felipe":
                dialogo.find_element_by_class_name("_1wjpf").click()
