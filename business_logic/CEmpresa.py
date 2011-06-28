#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

#import ...test.py


# Create instance of FieldStorage 
form = cgi.FieldStorage()

#Cria a classe controller de empresas

class CEmpresa:

    def exibeCadastro(self):
        business_name = form.getvalue('business_name')
        business_cnpj = form.getvalue('business_cnpj')
        business_email = form.getvalue('business_email')