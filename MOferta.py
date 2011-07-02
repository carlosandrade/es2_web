#!/usr/bin/python
import cgi, cgitb, string
cgitb.enable()


class Oferta:
 
    def __init__(self,nomeOferta="", cotaMinima="", descontoOferecido="", preco="", regulamento="", validade="", limiteCompraPorPessoa="", detalhes="", avaliacao=""):
        self.nomeOferta = nomeOferta

  #  def update(self,username):

#    def save(self):
#        file = open("empresas.txt","a+")
#        file.write(self.nome+" "+self.cnpj+" "+self.email+"\n")
#        file.close()

    def openAll(self):
        file = open("ofertas.txt","r+")
        ofertas = file.readlines()
        file.close()
        return ofertas

    def saveAll(self,ofertas):
        file = open("ofertas.txt","w")
        file.close
        file = open("ofertas.txt","a+")
        for oferta in ofertas:
            file.write(oferta)
        file.close()

    def open(self,nomeOferta):
        file = open("ofertas.txt","r+")
        ofertas = file.readlines()
        file.close()
        for oferta in ofertas:
            campoOferta = string.split(oferta)
            if campoOferta[0] == nomeOferta:
                return campoOferta
        return "not_found"            


