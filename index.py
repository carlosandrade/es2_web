#!/usr/bin/python

#import CEmpresa

def imprime_tabela_de_dados():
    print "\t<H3>Favor digitar Nome da empresa, cnpj e e-mail<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/CEmpresa.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"display\">\n"


    print "\t\t<TR><TH>Nome da Empresa:</TH><TD><INPUT type = text \
    name = \"business_name\"></TD><TR>\n"

    print "\t\t<TR><TH>CNPJ:</TH><TD><INPUT type = text \
    name = \"business_cnpj\"></TD><TR>\n"

    print "\t\t<TR><TH>Email da empresa:</TH><TD><INPUT type = text \
    name = \"business_email\"></TD></TR>\n"

    print "\t</TABLE>\n"



    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"visualizar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"cadastrar\">\n"
    print "\t</FORM>\n"


def main():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Cadastro da Empresa</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    imprime_tabela_de_dados()

    print "</BODY>\n"
    print "</HTML>\n"	
	
main()