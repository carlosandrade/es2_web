#!/usr/bin/python

def imprime_tabela_de_dados():
    print "\t<H3>Favor preencher os dados requisitados<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TCadastroConsumidor\">\n"


    print "\t\t<TR><TH>Nome completo:</TH><TD><INPUT type = text \
    name = \"nome\"></TD><TR>\n"

    print "\t\t<TR><TH>Email:</TH><TD><INPUT type = text \
    name = \"email\"></TD><TR>\n"

    print "\t\t<TR><TH>Numero do cartao:</TH><TD><INPUT type = text \
    name = \"ncartao\"></TD></TR>\n"

    print "<select name=\"tipoCartao\">"
    print "<option value=\"visa\" selected>Visa</option>"
    print "<option value=\"mastercard\">Mastercard</option>"
    print "<option value=\"amex\">American Express</option>"
    print "</select>"

    print "\t\t<TR><TH>Login:</TH><TD><INPUT type = text \
    name = \"login\"></TD></TR>\n"

    print "\t\t<TR><TH>Senha:</TH><TD><INPUT type = password \
    name = \"password\"></TD></TR>\n"  

    print "\t</TABLE>\n"


    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"cadastrar\">\n"
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
