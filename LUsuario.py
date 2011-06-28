#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import cgi, cgitb, string, Cookie, os
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

    def set_client_Cookie(self):
        # Create a Cookie object.
        a_cookie = Cookie.Cookie()

        # Assign the cookie a value.
        a_cookie["user"] = "Python"

        # Required header that tells the browser how to render the HTML.
        #print "Content-Type: text/html" informado na verificacao de senha

        # Send the cookie back to the client.
        print a_cookie, "\n\n"

        # Print the cookie value.
        print "<HTML><BODY>"
        print a_cookie["user"].value, "user cookie set.\n"
        print "<FORM METHOD = post ACTION = \"example_7.4.cgi\">\n"
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

def main():
    form = cgi.FieldStorage()
    lUsuario = LUsuario()
    if form.has_key("action"):
        if (form["action"].value == "login"):
            result = lUsuario.test(form["username"].value, form["password"].value)
            lUsuario.display_page(result)

            #if (form.has_key("set")):
             #   if (form["set"].value == "yes"):
                     #lUsuario.read_client_Cookie()
                #else:
            lUsuario.set_client_Cookie() 
    


#Call main function.
main()