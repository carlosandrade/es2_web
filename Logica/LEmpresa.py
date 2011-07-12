#!/usr/bin/python

# Import modules for CGI handling 
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb
import MEmpresa, MUsuario, Cookie, os
cgitb.enable()

# Create instance of FieldStorage 


#Cria a classe controller de empresas

class LEmpresa:
	
    def __init__(self,form=""):
       if form.has_key("action"):
            if form["action"].value == "TCadastroEmpresa":
                if form["check"].value == "cadastrar":
	                self.salvaEmpresa(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value,form["business_login"].value, form["business_password"].value)

#    def exibeCadastro(self, name, cnpj, email):
#        print "Content-type:text/html\r\n\r\n"
#        print "<html>"
#        print "<head>"
#        print "<title>Hello - Second CGI Program</title>"
#        print "</head>"
 #       print "<body>"
 #       print "<h2>Hello %s %s %s</h2>" % (name, cnpj,email)
 #       print "</body>"
 #       print "</html>"

    def salvaEmpresa(self,name,cnpj,email,login,password):
        
        empresa = MEmpresa.Empresa(name,cnpj,email,login,password)
        empresa.save()
	usuario = MUsuario.Usuario("empresa",login,password)
	usuario.save()
    print "Content-type:text/html\r\n\r\n"
    print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCadastroEmpresa.py?update=exibeEmpresaCadastradaComSucesso\">"

def read_client_Cookie():
    # Create a Cookie object.
    a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )

    # Assign the variable a cookie value.
    cookie_val = a_cookie["user"].value

    # Required header that tells the browser how to render the HTML.
    print "Content-Type: text/html\n\n"

    # Print the cookie value.
    print "<HTML><BODY>"
    print cookie_val, "user cookie read from client.\n"
    print "Empresa:", a_cookie["user"].value,"CNPJ:",a_cookie["cnpj"].value,"Email:",a_cookie["email"].value,"\n"    
    print "</BODY></HTML>\n"
