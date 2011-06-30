#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb
import Cookie, os
cgitb.enable()


def read_client_Cookie():
    # Create a Cookie object.
    a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )

    # Assign the variable a cookie value.
    cookie_val = a_cookie["user"].value

    # Required header that tells the browser how to render the HTML.
    print "Content-Type: text/html\n\n"

    # Print the cookie value.
    #print "<HTML><BODY>"
    #print cookie_val, "user cookie read from client.\n"
    #print "Empresa:", a_cookie["user"].value,"CNPJ:",a_cookie["cnpj"].value,"Email:",a_cookie["email"].value,"\n"    
    #print "</BODY></HTML>\n"


def main():
    
    a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Cadastro da Empresa</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Minha Conta<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TMinhaConta\">\n"


    print "\t\t<TR><TH>Nome: ",a_cookie["user"].value,"</TH><TD>\n"

    #print "\t\t<TR><TH>CNPJ:</TH><TD><INPUT type = text \
    #name = \"business_cnpj\"></TD><TR>\n"

    #print "\t\t<TR><TH>Email da empresa:</TH><TD><INPUT type = text \
    #name = \"business_email\"></TD></TR>\n"

    print "\t</TABLE>\n"



    #print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"visualizar\">\n"
    #print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"cadastrar\">\n"
    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

main()

