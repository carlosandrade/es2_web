#!/usr/bin/python
import cgi, cgitb, string
cgitb.enable()


class Empresa:

    #def __init__(self):
     #   self.nome = default

#    def __init__(self,nome,cnpj,email):
 #       self.nome = nome
  #      self.cnpj = cnpj
   #      self.email = email

    def save(self):
        file = open("empresas.txt","a+")
        file.write(self.nome+" "+self.cnpj+" "+self.email+"\n")
        file.close()

    def open(self,username):
        file = open("empresas.txt","r")
        line = file.readline()
        file.close()
        self.nome,self.cnpj,self.email = string.split(line, " ")