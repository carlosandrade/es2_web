#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb
import LEmpresa, LUsuario
import LAdministrador
cgitb.enable()

class FNegocio:

     def logicaEmpresa(self,form):
         lEmpresa = LEmpresa.LEmpresa(form)

     def logicaUsuario(self,form):
         lUsuario = LUsuario.LUsuario(form)

     def logicaAdministrador(self,form):
         lAdministrador = LAdministrador.LAdministrador(form)

     def administradorDropOfertasPendentes(self):
         lAdministrador = LAdministrador.LAdministrador()
         lAdministrador.DropOfertasPendentes()

     def administradorExibeDadosOfertasPendentes(self):
         lAdministrador = LAdministrador.LAdministrador()
         lAdministrador.exibeDadosOfertasPendentes()


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
        else:
            print "Content-type:text/html\r\n\r\n"
            print "<HTML>\n"
            print "<HEAD>\n"
            print "\t<TITLE>Redirecionando...</TITLE>\n"
            print "</HEAD>\n"
            print "<BODY>\n"
            print "\t<H3>Action: ",form["action"].value,"<H3>\n"
            print "</BODY>\n"
            print "</HTML>\n"

#Call main function.
main()