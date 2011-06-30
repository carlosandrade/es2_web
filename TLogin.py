#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules
import cgi, cgitb
cgitb.enable() 

# Define function to generate HTML form.
def main():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Tela de login</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Digite usuario e senha</H3>\n"
    print "\t<TABLE BORDER = 0>\n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"
    print "\t\t<TR><TH>Usuario:</TH><TD><INPUT TYPE = text \
    NAME = \"username\"></TD><TR>\n"
    print "\t\t<TR><TH>Senha:</TH><TD><INPUT \
    TYPE = password NAME = \"password\"></TD></TR>\n"
    print "\t</TABLE>\n"
    print "\t<INPUT TYPE = hidden NAME = \"action\" VALUE = \
    \"TLogin\">\n"
    print "\t<INPUT TYPE = submit VALUE = \"Entrar\">\n"
    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

main()