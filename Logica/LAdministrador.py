#!/usr/bin/python

# Import modules for CGI handling 
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb
import Cookie, os, string
import MOferta, MSugestao, MEmpresa

cgitb.enable()

class LAdministrador:
    def __init__(self,form=""):
	
       if form != "":
           if form["action"].value == "TAvaliarOferta":
               if form["check"].value == "aceitar":
                   self.aceitaOferta(form["dropdown"].value)
               elif form["check"].value == "recusar":
                   self.recusaOferta(form["dropdown"].value)
               elif form["check"].value == "modificacao":
                   self.modificaOferta(form["dropdown"].value)
               elif form["check"].value == "oferta do dia":
                   self.diaOferta(form["dropdown"].value)
            

       #else:
       #    a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
       #    print "Content-type:text/html\r\n\r\n"
       #    print "<HTML>\n"
       #    print "<HEAD>\n"
       #    print "\t<TITLE>Cadastro da Empresa</TITLE>\n"
       #    print "</HEAD>\n"
       #    print "<BODY BGCOLOR = white>\n"
       #    print "\t<H3>Minha Conta<H3>\n"
       #    print "\t<TABLE BORDER = 0> \n"
       #    print "\t\t<FORM METHOD = post ACTION = \
       #    \"/cgi-bin/FNegocio.py\">\n"

       #   print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
       #    \"TMinhaConta\">\n"

       #    print "\t\t<TR><TH>Usuario: ",a_cookie["user"].value,"</TH><TD>\n"
       #    print "\t\t<TR><TH>CNPJ: ",a_cookie["cnpj"].value,"</TH><TD>\n"
       #    print "\t\t<TR><TH>Email: ",a_cookie["email"].value,"</TH><TD>\n"

       #    print "\t</TABLE>\n"
       #    print "\t</FORM>\n"
       #    print "</BODY>\n"
       #    print "</HTML>\n"


    def aceitaOferta(self,nomeOferta):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i]," ")
            if  campoOferta[0] == nomeOferta:
                campoOferta[9] = "aceita"
                ofertas[i] =""
                for j in range(len(campoOferta)):
                    if campoOferta[j] != "\n":
                        ofertas[i] += campoOferta[j]+" "
                    else:
                        ofertas[i] += campoOferta[j] 
                #if i != len(ofertas)-1:
                #    ofertas[i] += "\n"
        mOferta.saveAll(ofertas)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TAvaliarOferta.py?update=exibeOfertaAceita\">"  

                	
    def recusaOferta(self,nomeOferta):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i]," ")
            if  campoOferta[0] == nomeOferta:
                ofertas[i] =""
        mOferta.saveAll(ofertas)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TAvaliarOferta.py?update=exibeOfertaRecusada\">"    

    def modificaOferta(self,nomeOferta):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i]," ")
            if  campoOferta[0] == nomeOferta:
                campoOferta[9] = "modifica"
                ofertas[i] =""
                for j in range(len(campoOferta)):
                    if campoOferta[j] != "\n":
                        ofertas[i] += campoOferta[j]+" "
                    else:
                        ofertas[i] += campoOferta[j] 
        mOferta.saveAll(ofertas)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TAvaliarOferta.py?update=exibeOfertaRecusada\">" 

    def diaOferta(self,nomeOferta):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i]," ")
            if  campoOferta[0] == nomeOferta:
                campoOferta[9] = "oferta_do_dia"
                ofertas[i] =""
                for j in range(len(campoOferta)):
                    if campoOferta[j] != "\n":
		                ofertas[i] += campoOferta[j]+" "
                    else:
                       ofertas[i] += campoOferta[j] 
        mOferta.saveAll(ofertas)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TAvaliarOferta.py?update=exibeDiaOferta\">" 
   
 
    def getDadosOfertasPendentes(self):
        mOferta = MOferta.Oferta()
        return mOferta.openAll()
        
    def getSugestoes(self):
        mSugestoes = MSugestao.Sugestao()
        return mSugestoes.openAll()        

    def DropOfertasPendentes(self):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        return ofertas
