#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb, string, Cookie, os
import MEmpresa
cgitb.enable()

class FModel:
    
    def salvaEmpresa(self,nome,cnpj,email):
        empresa = MEmpresa.MEmpresa(nome,cnpj,email)
        empresa.save()

    def carregaEmpresa(self,username):
        empresa = MEmpresa.MEmpresa()
        empresa.open(self,username)