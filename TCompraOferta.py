#!/usr/bin/python

import cgi, cgitb
import Cookie, os
import FNegocio
cgitb.enable()


def imprime_tabela_de_dados():
    
    fNegocio = FNegocio.FNegocio()
    

    print "\t<H3>Comprar oferta:<H3>\n"
    print "\t<TABLE BORDER = 0> \n"

    fNegocio.telaPrincipalExibeOfertaDia()
    fNegocio.exibeDadosCompraConsumidor()



    print "\t</TABLE>\n"

    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Comprar oferta\">\n"
    print "\t</FORM>\n"


def main(): 
    
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Compra de ofertas</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    imprime_tabela_de_dados()

    print "</BODY>\n"
    print "</HTML>\n"	
	
main()
