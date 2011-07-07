#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb
import LEmpresa, LUsuario
import LAdministrador, LOferta
import LConsumidor
import biscoito, Cookie, os
cgitb.enable()

class FNegocio:

     def logicaEmpresa(self,form):
         lEmpresa = LEmpresa.LEmpresa(form)

     def logicaUsuario(self,form):
         lUsuario = LUsuario.LUsuario(form)

     def logicaOferta(self,form):
         lOferta = LOferta.LOferta(form)
    
     def logicaConsumidor(self,form):
        lConsumidor = LConsumidor.LConsumidor(form)

     def logicaAdministrador(self,form):
         lAdministrador = LAdministrador.LAdministrador(form)

     def administradorDropOfertasPendentes(self):
         lAdministrador = LAdministrador.LAdministrador()
         return lAdministrador.DropOfertasPendentes()

     def administradorGetDadosOfertasPendentes(self):
         lAdministrador = LAdministrador.LAdministrador()
         return lAdministrador.getDadosOfertasPendentes()
         
     def telaPrincipalExibeOfertaDia(self):
         lOferta = LOferta.LOferta()
         lOferta.exibe_oferta_do_dia()
     
     def exibeDadosCompraConsumidor(self):
        lConsumidor = LConsumidor.LConsumidor()
        lConsumidor.exibeDadosConsumidor()



def main():
    form = cgi.FieldStorage()
    fNegocio = FNegocio()
    if form.has_key("action"):
        if form["action"].value == "TCadastroEmpresa":
            fNegocio.logicaEmpresa(form)
        elif form["action"].value == "TLogin":
            fNegocio.logicaUsuario(form)
        elif form["action"].value == "TAvaliarOferta":
            fNegocio.logicaAdministrador(form)
        elif form["action"].value == "TSubmissaoOferta":
            fNegocio.logicaOferta(form)
        elif form["action"].value == "TCadastroConsumidor":
            fNegocio.logicaConsumidor(form)
        elif form["action"].value == "TPrincipal":
            print "Content-type:text/html\r\n\r\n"
            if form["check"].value == "Login":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/TLogin.py\">"
            elif form["check"].value == "Cadastrar(Cliente)":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/TCadastroConsumidor.py\">"
            elif form["check"].value == "Cadastrar(Empresa)":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/TCadastroEmpresa.py\">"
            elif form["check"].value == "Compre Agora!":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/TCompraOferta.py\">"
                            
                    
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
