#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()


class Consumidor:
 
    def __init__(self,nome="",email="",ncartao="",tipoCartao="",login="",password=""):
        self.nome = nome
        self.email = email
        self.ncartao = ncartao
        self.tipoCartao = tipoCartao 
        self.login = login
        self.password = password
      
    def save(self):
        file = open("Banco/consumidor.txt","a+")
        file.write(self.nome+" "+self.login+" "+self.password+" "+self.email+" "+self.ncartao+" "+self.tipoCartao+" \n")
        file.close()

    def open(self,login):
        consumidores = self.openAll()
        for i in range(len(consumidores)):
            campoConsumidor = string.split(consumidores[i]," ")
            if (login == campoConsumidor[1]):
                self.nome,self.login,self.password,self.email,self.ncartao,self.tipoCartao,enter = campoConsumidor
               
    def openAll(self):
        file = open("Banco/consumidor.txt","r+")
        consumidores = file.readlines()
        file.close()
        return consumidores
