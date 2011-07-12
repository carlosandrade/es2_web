#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb
cgitb.enable() 

def loginPassou():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Info Form</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "Senha correta. Usuario autenticado.\n"
    print "</BODY>\n"
    print "</HTML>\n"

def loginFalhou():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Info Form</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "Senha incorreta, favor tentar novamente.\n"
    print "</BODY>\n"
    print "</HTML>\n"   

def default():
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
    NAME = \"login\"></TD><TR>\n"

    print "\t\t<TR><TH>Senha:</TH><TD><INPUT \
    TYPE = password NAME = \"password\"></TD></TR>\n"

    print "\t</TABLE>\n"
    print "\t<INPUT TYPE = hidden NAME = \"action\" VALUE = \
    \"TLogin\">\n"
    print "\t<INPUT TYPE = submit VALUE = \"Entrar\">\n"
    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

def main():
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "passed":
            loginPassou()
        elif form["update"].value == "failed":
            loginFalhou()
        else:
            default()                                            
    else:  
        default()
    
main()
