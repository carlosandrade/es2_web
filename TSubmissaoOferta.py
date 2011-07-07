#!/usr/bin/python

def imprime_tabela_de_dados():
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



    print "\t</TABLE>\n"

    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Submeter oferta\">\n"
    print "\t</FORM>\n"


def main():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Submissao de ofertas</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    imprime_tabela_de_dados()

    print "</BODY>\n"
    print "</HTML>\n"	
	
main()
