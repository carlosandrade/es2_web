#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()


class Oferta:
 
    def __init__(self,nome="",cota_minima="",preco="",desconto="",regulamento="",validade="",limite="",detalhes="",quantidade=""):
        self.nome = nome
        self.cota_minima = cota_minima
        self.preco = preco
        self.desconto = desconto 
        self.regulamento = regulamento
        self.validade = validade
        self.limite = limite
        self.detalhes = detalhes
        self.reputacao = "neutra"
        self.avaliacao = "pendente"
        self.quantidade = quantidade


    def save(self):
        file = open("/Library/WebServer/CGI-Executables/Banco/ofertas.txt","a+")
        file.write(self.nome+" "+self.cota_minima+" "+self.preco+" "+self.desconto+" "+self.regulamento+" "+self.validade+" "+self.limite+" "+self.detalhes+" "+self.reputacao+" "+self.avaliacao+" "+self.quantidade+" \n")
        file.close()

    def openAll(self):
        file = open("/Library/WebServer/CGI-Executables/Banco/ofertas.txt","r+")
        ofertas = file.readlines()
        file.close()
        return ofertas

    def saveAll(self,ofertas):
        file = open("/Library/WebServer/CGI-Executables/Banco/ofertas.txt","w")
        file.close
        file = open("/Library/WebServer/CGI-Executables/Banco/ofertas.txt","a+")
        for oferta in ofertas:
            file.write(oferta)
        file.close()

    def open(self,nomeOferta):
        file = open("/Library/WebServer/CGI-Executables/Banco/ofertas.txt","r+")
        ofertas = file.readlines()
        file.close()
        for oferta in ofertas:
            campoOferta = string.split(oferta," ")
            if campoOferta[0] == nomeOferta:
                self.nome,self.cota_minima,self.preco,self.desconto,self.regulamento,self.validade,self.limite,self.detalhes,self.reputacao,self.avaliacao,self.quantidade,enter = campoOferta         
                return self

