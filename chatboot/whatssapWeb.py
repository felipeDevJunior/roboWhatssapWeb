from selenium import webdriver

class WhatssapWeb:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\WebDriver\chromedriver.exe")
        self.url = "https://web.whatsapp.com/"
        self.input = "_3zb-j"
        self.frase = "]/div/div/div/div[1]/div/span[1]/span"
        self.caminho = "//*[@id='main']/div[3]/div/div/div[3]/div["
        #              //*[@id="main"]/div[3]/div/div/div[2]/div[7]/div/div/div/div[1]/div/span[1]/span
        self.nomeConato = ""
        self.indice = "0"
        self.output = "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
        self.novaMsg = "OUeyt"
        self.dialogo = "_3j7s9"
        self.submit = "_35EW6"

        self.div0 = "vW7d1 message-in"
        self.div1 = "_3FXB1 selectable-text invisible-space copyable-text"

    def buscaUrl(self):
         self.driver.get(self.url)

    def getInput(self):
        res = self.driver.find_elements_by_class_name("vW7d1")
        indice = str(len(res))
        frase = self.driver.find_element_by_xpath(self.caminho +indice+ self.frase).text
        return frase


    def getInput2(self):
        div = self.driver.find_elements_by_class_name("vW7d1")
        indice = len(div)
        div1 = div[indice].find_element_by_class_name("_3_7SH _3DFk6 focusable-list-item")
        div2 = div1.find_element_by_class_name("MVjBr _3e2jK")
        div3 = div2.find_element_by_class_name("Tkt2p")
        div4 = div3.find_element_by_class_name("copyable-text")
        div5 = div4.find_element_by_class_name("_3zb-j")
        div6 = div5.find_element_by_class_name("_3FXB1 selectable-text invisible-space copyable-text").text
        return div6

    def getDialogo(self):
        res = self.driver.find_elements_by_class_name(self.dialogo)
        return res


    def response(self, resposta):
     self.driver.find_element_by_xpath(self.output).send_keys(resposta)


    def verifica(self):
        el = self.driver.find_elements_by_class_name(self.novaMsg)
        if(el):
            return True

    def sendMesage(self):
        self.driver.find_element_by_class_name(self.submit).click()

    def pegaNome(self,dialogo):
        div = dialogo.find_element_by_class_name("_2FBdJ")
        div1 = div.find_element_by_class_name("_25Ooe").text
        return div1


    def pegaNomaMnesagem(self,dialogo):
        #res = self.driver.find_elements_by_class_name("_3j7s9")
        div1 = dialogo.find_element_by_class_name("_1AwDx")
        div2 = div1.find_element_by_class_name("_3Bxar")
        div3 = div2.find_element_by_class_name("_15G96")
        div4 = div3.find_element_by_class_name("OUeyt")
        return div4

    def pegaInput(self,dialogo):
        div1 = dialogo.find_element_by_class_name("_1AwDx")
        div5 = div1.find_element_by_class_name("_itDl")
        div6 = div5.find_element_by_class_name("_2_LEW").text
        return div6


