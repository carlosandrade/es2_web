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
               if form["check"].value == "aceitar":
                   self.aceitaOferta(form["dropdown"].value)
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
                    ofertas[i] += campoOferta[j]+" "
                #if i != len(ofertas)-1:
                #    ofertas[i] += "\n"
        mOferta.saveAll(ofertas)
        print "Content-type:text/html\r\n\r\n"
        print "<HTML>\n"
        print "<HEAD>\n"
        print "\t<TITLE>Redirecionando...</TITLE>\n"
        print "</HEAD>\n"
        print "<BODY>\n"
        print "\t<H3>Ofertas Pendentes<H3>\n"  
        print "</BODY>\n"
        print "</HTML>\n"
    

    
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
            print "\t\t<OPTION VALUE=\"%s\">%s</ OPTION >" % (nomeOferta[0],nomeOferta[0])
            #print "\t\t<OPTION VALUE=\"",nomeOferta[0],"\">",nomeOferta[0],"</ OPTION > "
        print "\t\t</SELECT>"