#!/usr/bin/python

import cgi, cgitb, string
import FNegocio
cgitb.enable() 

def imprime_tabela_de_dados():

    fNegocio = FNegocio.FNegocio()
        
    print "\t<H1>ComprOn<H1>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/TCompraOferta.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TPrincipal\">\n"
    
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Cadastrar(Cliente)\">\n"

    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Cadastrar(Empresa)\">\n"    
    
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Login\">\n"
    
    print "\t</TABLE>\n"
    

    fNegocio.telaPrincipalExibeOfertaDia()



    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Compre Agora!\">\n"
    print "\t\n<H3>Outras Ofertas<H3>\n"

    ofertasDropdown = fNegocio.administradorDropOfertasPendentes()

    print "\t\t<SELECT NAME = \"dropdown\">"
    for oferta in ofertasDropdown:
        nomeOferta = string.split(oferta, " ")
        print "\t\t<OPTION VALUE=\"%s\">%s</ OPTION >" % (nomeOferta[0],nomeOferta[0])
    print "\t\t</SELECT>"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Compre Tambem!\">\n"
	
    print "\t</FORM>\n"    


        


def main():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Cadastro de Usuario</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    imprime_tabela_de_dados()

    print "</BODY>\n"
    print "</HTML>\n"	
	
main()
