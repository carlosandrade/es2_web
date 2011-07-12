#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()

def default(form):

    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Recomendar Oferta</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    print "\t<H3>Favor preencher os dados requisitados<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TRecomendarOferta\">\n"

    print "\t\tEmail do seu amigo:</TH><TD><INPUT type = text \
    name = \"email\"> <br />\n"

    if form.has_key("mensagem"):
        print "\t\tMensagem: <br /><textarea rows=\"30\" name=\"mensagem\" cols=\"40\" >%s" % (form["mensagem"].value)
    else:
        print "\t\tMensagem: <br /><textarea rows=\"30\" name=\"mensagem\" cols=\"40\" >"
    print "</textarea>\n"


    print "\t</TABLE>\n"


    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"submeter\">\n"
    print "\t</FORM>\n"


    print "</BODY>\n"
    print "</HTML>\n"
    
def emailEnviadoComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Email enviado com sucesso!</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Email enviado com sucesso. Obrigado!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"

def main():
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "exibeEmailEnviadoComSucesso":
            emailEnviadoComSucesso()
        #elif form["update"].value == "exibeOfertaRecusada":
        #    ofertaRecusadacomSucesso()
        else:
            default(form)                                            
    else:  
        default(form)


    
main()