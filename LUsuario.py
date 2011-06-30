#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb, string, Cookie, os
import MEmpresa
cgitb.enable()

class LUsuario:

    def __init__(self,form):
        if form.has_key("action"):
            if (form["action"].value == "TLogin"):
                result = self.test(form["username"].value, form["password"].value)
                self.display_page(result)
                if  result == "passed":    
                    self.set_client_Cookie(form["username"].value)

	# Define function to test the password.
    def test(self,pident, ppasswd):
        passwd_file = open('passwords.txt', 'r')
        line = passwd_file.readline()
        passwd_file.close()
        ident,senha = string.split(line, " ")
        if (pident == ident) and (ppasswd == senha):
            return "passed"
        else:
            return "failed"

    def set_client_Cookie(self,ident):
        # Create a Cookie object.
        a_cookie = Cookie.Cookie()

        #Load Empresa from file using id
        empresa = MEmpresa.Empresa()
        empresa.open(ident)

        # Assign the cookie a value.
        a_cookie["user"] = empresa.nome
        a_cookie["cnpj"] = empresa.cnpj
        a_cookie["email"] = empresa.email

        # Required header that tells the browser how to render the HTML.
        #print "Content-Type: text/html"

        # Send the cookie back to the client.
        print a_cookie, "\n\n"

        # Print the cookie value.
        print "<HTML><BODY>"
        print "Bem vinda, ",a_cookie["user"].value, "\n"
        print "<FORM METHOD = post ACTION = \"TMinhaConta.py\">\n"
        print "<INPUT TYPE = \"hidden\" NAME = \
        \"set\" VALUE =\"yes\">\n"
        print "<INPUT TYPE = \"submit\" VALUE = \"Go\"></FORM>\n"
        print "</BODY></HTML>\n"

    # Define function to read a cookie.
    def read_client_Cookie(self):
        # Create a Cookie object.
        a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )

        # Assign the variable a cookie value.
        cookie_val = a_cookie["user"].value

        # Required header that tells the browser how to render the HTML.
        print "Content-Type: text/html\n\n"

        # Print the cookie value.
        print "<HTML><BODY>"
        print cookie_val, "user cookie read from client.\n"
        print "</BODY></HTML>\n"


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