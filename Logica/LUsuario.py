#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string, Cookie, os
import MEmpresa, MUsuario, MConsumidor
cgitb.enable()

class LUsuario:

    def __init__(self,form):
        if form.has_key("action"):
            if (form["action"].value == "TLogin"):
                result = self.test(form["login"].value, form["password"].value)
                self.exibeResultadoAutenticacao(result,form["login"].value)
                    

	# Define function to test the password.
    def test(self,login, password):
        usuario = MUsuario.Usuario()
        usuarios = usuario.openAll()
        for i in range(len(usuarios)):
   	        campoUsuario = string.split(usuarios[i]," ")
   	        if (login == campoUsuario[1]) and (password == campoUsuario[2]):
   	            return "passed"
        return "failed"

    def tipoUsuario(self,login):
        usuario = MUsuario.Usuario()
        usuarios = usuario.openAll()
        for i in range(len(usuarios)):
            campoUsuario = string.split(usuarios[i]," ")
            if (login == campoUsuario[1]):
                return campoUsuario[0]

    def set_client_Cookie(self,tipo,login):
        # Create a Cookie object.
        a_cookie = Cookie.SimpleCookie()
        
        if (tipo == "consumidor"):
            consumidor = MConsumidor.Consumidor()
            consumidor.open(login)

            # Assign the cookie a value.
            a_cookie["nome"] = consumidor.nome
            a_cookie["email"] = consumidor.email
            a_cookie["ncartao"] = consumidor.ncartao
            a_cookie["tipoCartao"] = consumidor.tipoCartao
            a_cookie["login"] = consumidor.login
            a_cookie["password"] = consumidor.password
            
            # Required header that tells the browser how to render the HTML.
#            print "Content-Type: text/html"

		    # Send the cookie back to the client.
#            print a_cookie, "\n\n"

		    # Print the cookie value.
#            print "<HTML><BODY>"
#            print "Bem vinda, ",consumidor.nome, "\n"
#            print "<FORM METHOD = post ACTION = \"TMinhaConta.py\">\n"
#            print "<INPUT TYPE = \"hidden\" NAME = \
#            \"set\" VALUE =\"yes\">\n"
#            print "<INPUT TYPE = \"submit\" VALUE = \"Continuar\"></FORM>\n"
#            print "</BODY></HTML>\n"
#            print

            

        elif (tipo == "empresa"):
    	    #Load Empresa from file using id
            empresa = MEmpresa.Empresa()
            empresa.open(login)

            # Assign the cookie a value.
            a_cookie["nome"] = empresa.nome
            a_cookie["cnpj"] = empresa.cnpj
            a_cookie["email"] = empresa.email
            a_cookie["login"] = empresa.login
            a_cookie["password"] = empresa.password
            a_cookie["reputacao"] = empresa.reputacao

		    # Required header that tells the browser how to render the HTML.
            print "Content-Type: text/html"

		    # Send the cookie back to the client.
            print a_cookie, "\n\n"

		    # Print the cookie value.
            print "<HTML><BODY>"
            print "Bem vinda, ",empresa.nome, "\n"
            print "<FORM METHOD = post ACTION = \"TMinhaConta.py\">\n"
            print "<INPUT TYPE = \"hidden\" NAME = \
            \"set\" VALUE =\"yes\">\n"
            print "<INPUT TYPE = \"submit\" VALUE = \"Continuar\"></FORM>\n"
            print "</BODY></HTML>\n"
            print

    # Define function to read a cookie.
    def read_client_Cookie(self):

        # Required header that tells the browser how to render the HTML.
        print "Content-Type: text/html\n\n"

        # Create a Cookie object.
        a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )

        # Assign the variable a cookie value.
        cookie_val = a_cookie["user"].value



        # Print the cookie value.
        print "<HTML><BODY>"
        print cookie_val, "user cookie read from client.\n"
        print "</BODY></HTML>\n"


    # Define function display_page.
    def exibeResultadoAutenticacao(self,result,login):
        tipo = self.tipoUsuario(login)
        if result == "passed":
            self.set_client_Cookie(tipo,login)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TLogin.py?update=%s\">" % (result)
