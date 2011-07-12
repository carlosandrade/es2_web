#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb


def empresaCadastradaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Empresa cadastrada com sucesso</title>"
    print "</head>"
    print "<body>"
    print "<h2>Empresa cadastrada com sucesso!</h2>\n"
    print "<p>O que deseja fazer agora?\n<p>"
    print " <a 	href=\"TCadastroEmpresa.py\">Retornar a tela de cadastro de empresa</a>"
    print "</body>"
    print "</html>"


def default():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Cadastro da Empresa</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

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



#    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"visualizar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"cadastrar\">\n"
    print "\t</FORM>\n"

    print "</BODY>\n"
    print "</HTML>\n"	
	
def main():
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "exibeEmpresaCadastradaComSucesso":
            empresaCadastradaComSucesso()
#        elif form["update"].value == "exibeOfertaRecusada":
#            ofertaRecusadacomSucesso()
        else:
            default()                                            
    else:  
        default()   
    
main()
