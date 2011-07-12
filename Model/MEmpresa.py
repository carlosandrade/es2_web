#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()


class Empresa:
 
    def __init__(self,nome="",cnpj="",email="",login="",password="",reputacao="neutra"):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
	self.reputacao = reputacao
        self.login = login
        self.password = password

    def save(self):
        file = open("Banco/empresas.txt","a+")
        file.write(self.nome+" "+self.cnpj+" "+self.email+" "+self.login+" "+self.password+" "+self.reputacao+" \n")
        file.close()

    def open(self,login):
        empresas = self.openAll()
        for i in range(len(empresas)):
            campoEmpresa = string.split(empresas[i]," ")
            if (login == campoEmpresa[3]):
                self.nome,self.cnpj,self.email,self.login,self.password,self.reputacao,enter = campoEmpresa

    def openAll(self):
        file = open("Banco/empresas.txt","r+")
        empresas = file.readlines()
        file.close()
        return empresas
