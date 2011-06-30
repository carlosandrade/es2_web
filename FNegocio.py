#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb
import LEmpresa
cgitb.enable()

class FNegocio:

     def logicaEmpresa(self,form):
         lEmpresa = LEmpresa.LEmpresa(form)

def main():
    form = cgi.FieldStorage()
    fNegocio = FNegocio()
    if form.has_key("action"):
        if form["action"].value == "TCadastroEmpresa":
            fNegocio.logicaEmpresa(form)
        else:
            print "Content-type:text/html\r\n\r\n"
            print "<HTML>\n"
            print "<HEAD>\n"
            print "\t<TITLE>Info Form</TITLE>\n"
            print "</HEAD>\n"
            print "<BODY BGCOLOR = white>\n"
            print "Senha incorreta, favor tentar novamente.\n"
            print "</BODY>\n"
            print "</HTML>\n"

#Call main function.
main()