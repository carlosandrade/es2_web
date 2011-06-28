#!/usr/bin/python

class Empresa:
 
    def __init__(self,nome,cnpj,email):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email

    def save(self):
        file = open("empresas.txt","w")
        file.write(self.nome+""+self.cnpj+""+self.email)
        file.close()