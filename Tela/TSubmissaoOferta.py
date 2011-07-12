#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
import FNegocio
cgitb.enable()


def ofertaSubmetidaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Oferta submetida com sucesso!</title>"
    print "</head>"
    print "<body>"
    print "<h2>Oferta submetida com sucesso!</h2>\n"
    print "<p>O que deseja fazer agora?\n<p>"
    print " <a href=\"TSubmissaoOferta.py\">Retornar a tela de submissao de oferta</a>"
    print "</body>"
    print "</html>"


def default():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Submissao de ofertas</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    print "\t<H3>Favor preencher os dados da oferta:<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TSubmissaoOferta\">\n"

    print "\t\t<TR><TH>Nome :</TH><TD><INPUT type = text \
    name = \"oferta_nome\"></TD><TR>\n"

    print "\t\t<TR><TH>Cota minima:</TH><TD><INPUT type = text \
    name = \"cota_minima\"></TD><TR>\n"

    print "\t\t<TR><TH>Preco do produto:</TH><TD><INPUT type = text \
    name = \"preco\"></TD></TR>\n"

    print "\t\t<TR><TH>Desconto oferecido:</TH><TD><INPUT type = text \
    name = \"desconto\"></TD></TR>\n"
 
    print "\t\t<TR><TH>Regulamento:</TH><TD><INPUT type = text \
    name = \"regulamento\"></TD></TR>\n"

    print "\t\t<TR><TH>Validade:</TH><TD><INPUT type = text \
    name = \"validade\"></TD></TR>\n"

    print "\t\t<TR><TH>Limite de cupons por pessoa:</TH><TD><INPUT type = text \
    name = \"limite\"></TD></TR>\n"

    print "\t\t<TR><TH>Detalhes:</TH><TD><INPUT type = text \
    name = \"detalhes\"></TD></TR>\n"

    print "\t\t<TR><TH>Quantidade:</TH><TD><INPUT type = text \
    name = \"quantidade\"></TD></TR>\n"

    print "\t</TABLE>\n"

    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Submeter oferta\">\n"
    print "\t</FORM>\n"

    print "</BODY>\n"
    print "</HTML>\n"	
	
def main():
    
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "exibeOfertaSubmetidaComSucesso":
            ofertaSubmetidaComSucesso()
#        elif form["update"].value == "exibeDiaOferta":
#            ofertaDoDiaComSucesso()
        else:
            default()                                            
    else:  
        default()    
    
main()
