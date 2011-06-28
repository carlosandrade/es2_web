#!/usr/bin/python
import cgi, cgitb
cgitb.enable()


class Empresa:
 
    def __init__(self,nome,cnpj,email):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email

    def save(self):
        file = open("empresas.txt","a+")
        file.write(self.nome+" "+self.cnpj+" "+self.email+"\n")
        file.close()