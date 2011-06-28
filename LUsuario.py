#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb, string
cgitb.enable()

class LUsuario:
	# Define function to test the password.
    def test(self,pident, ppasswd):
        passwd_file = open('passwords.txt', 'r')
        line = passwd_file.readline()
        passwd_file.close()
        ident,senha = string.split(line, " ")
        #ident = "abc"
        #senha = "1234"
        if (pident == ident) and (ppasswd == senha):
            return "passed"
        else:
            return "failed"
     # Define function display_page.
    def display_page(self,result):
        print "Content-type:text/html\r\n\r\n"
        print "<HTML>\n"
        print "<HEAD>\n"
        print "\t<TITLE>Info Form</TITLE>\n"
        print "</HEAD>\n"
        print "<BODY BGCOLOR = white>\n"
        if result == "passed":
            print "Senha correta.\n"
        else:
            print "Senha incorreta, favor tentar novamente.\n"
        print "</BODY>\n"
        print "</HTML>\n"

def main():
    form = cgi.FieldStorage()
    lUsuario = LUsuario()
    if form.has_key("action"):
        if (form["action"].value == "login"):
            result = lUsuario.test(form["username"].value, form["password"].value)
            lUsuario.display_page(result)
#Call main function.
main()