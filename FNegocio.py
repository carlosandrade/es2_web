#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb
import Cookie, os


import LEmpresa, LUsuario, LAdministrador, LOferta,  LConsumidor

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
         
     def administradorGetSugestoes(self):
         lAdministrador = LAdministrador.LAdministrador()
         return lAdministrador.getSugestoes()
         
     def getOferta(self,nomeOferta):
         lOferta = LOferta.LOferta()
         return lOferta.getOferta(nomeOferta)
         
     def getOfertaDoDia(self):
         lOferta = LOferta.LOferta()
         return lOferta.ofertaDoDia()

     
     #def exibeDadosCompraConsumidor(self):
     #   lConsumidor = LConsumidor.LConsumidor()
     #   lConsumidor.exibeDadosConsumidor()



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
        elif (form["action"].value == "TSubmissaoOferta") or (form["action"].value == "TCompraOferta"):
            fNegocio.logicaOferta(form)
        elif form["action"].value == "TCadastroConsumidor" or (form["action"].value == "TEnviarSugestao") or (form["action"].value == "TIndicarAmigo"):
            fNegocio.logicaConsumidor(form)
        elif form["action"].value == "TPrincipal":
            print "Content-type:text/html\r\n\r\n"
            if form["check"].value == "Login":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TLogin.py\">"
            elif form["check"].value == "Cadastrar(Cliente)":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCadastroConsumidor.py\">"
            elif form["check"].value == "Cadastrar(Empresa)":
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCadastroEmpresa.py\">"
            #elif form["check"].value == "Compre Agora!":
                #print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCompraOferta.py\">"
                #print "wohoo"
                            
                    
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
