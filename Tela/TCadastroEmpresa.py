#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")

def imprime_tabela_de_dados():
    print "\t<H3>Favor digitar Nome da empresa, cnpj e e-mail<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TCadastroEmpresa\">\n"


    print "\t\t<TR><TH>Nome da Empresa:</TH><TD><INPUT type = text \
    name = \"business_name\"></TD><TR>\n"

    print "\t\t<TR><TH>CNPJ:</TH><TD><INPUT type = text \
    name = \"business_cnpj\"></TD><TR>\n"

    print "\t\t<TR><TH>Email da empresa:</TH><TD><INPUT type = text \
    name = \"business_email\"></TD></TR>\n"

    print "\t\t<TR><TH>Login da empresa:</TH><TD><INPUT type = text \
    name = \"business_login\"></TD></TR>\n"

    print "\t\t<TR><TH>Senha da empresa:</TH><TD><INPUT type = password \
    name = \"business_password\"></TD></TR>\n"

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
