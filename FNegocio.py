#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb
import LEmpresa, LUsuario
cgitb.enable()

class FNegocio:

     def logicaEmpresa(self,form):
         lEmpresa = LEmpresa.LEmpresa(form)

     def logicaUsuario(self,form):
         lUsuario = LUsuario.LUsuario(form)

     def logicaAdministrador(self,form):
         lAdministrador = LAdministrador.LAdministrador(form)

def main():
    form = cgi.FieldStorage()
    fNegocio = FNegocio()
    if form.has_key("action"):
        if form["action"].value == "TCadastroEmpresa":
            fNegocio.logicaEmpresa(form)
        if form["action"].value == "TLogin":
            fNegocio.logicaUsuario(form)
        if form["action"].value == "TAvaliarOferta":
            fNegocio.logicaAdministrador(form)


#Call main function.
main()