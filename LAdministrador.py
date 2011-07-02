#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MEmpresa, Cookie, os, string
import MOferta

cgitb.enable()

class LAdministrador:
    def __init__(self,form=""):
	
       if form != "":
            if form["action"].value == "TAvaliarOferta":
                if form["check"].value == "avaliar":
                    self.avaliaOferta(form["dropdown"].value)


    #def avaliaOferta(self,nomeOferta):
        #mOferta = MOferta.MOferta()
        #ofertas = mOferta.openAll(nomeOferta)
        
    def exibeDadosOfertasPendentes(self):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        print "\t<TABLE BORDER = 4> \n"
        print "\t\t<TR> \
        <TH>Titulo</TH>\n"
        print "<TH>Cota Minima</TH>\n"
        print "<TH>Desconto Oferecido</TH>\n"
        print "<TH>Preco</TH>\n"
        print "<TH>Regulamento</TH>\n"
        print "<TH>Validade</TH>\n"
        print "<TH>Limite de Compras por pessoa</TH>\n"
        print "<TH>Detalhes</TH>\n"
        print "</TR>\n"
        for oferta in ofertas:
            campoOferta = string.split(oferta)
            print "<TR>\n"
            for i in range(8):
                print "<TD>",campoOferta[i],"</TD>"
        print "</TABLE>"

    def DropOfertasPendentes(self):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        print "\t\t<SELECT NAME = \"dropdown\">"
        for oferta in ofertas:
            nomeOferta = string.split(oferta, " ")
            print "\t\t<OPTION VALUE = \"",nomeOferta[0],"\">",nomeOferta[0],"</ OPTION > "
        print "\t\t</SELECT>"