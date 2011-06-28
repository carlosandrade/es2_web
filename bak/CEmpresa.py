#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MEmpresa, Cookie, os
cgitb.enable()




# Create instance of FieldStorage 


#Cria a classe controller de empresas

class CEmpresa:

    def exibeCadastro(self, name, cnpj, email):
        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2>Hello %s %s %s</h2>" % (name, cnpj,email)
        print "</body>"
        print "</html>"

    def exibeConta(self):
	    print "Location: VTelaMinhaConta"

    def salvaEmpresa(self,name,cnpj,email):
        
        empresa = MEmpresa.Empresa(name,cnpj,email)
        empresa.save()
        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2>Os dados da empresa",name,"foram cadastrados com sucesso</h2>\n"
        print "<p>O que deseja fazer agora?\n<p>"
        print " <a href=\"VTelaDeCadastro.py\">Retornar a tela de cadastro de empresa</a>"
        print "</body>"
        print "</html>"

def read_client_Cookie():
    # Create a Cookie object.
    a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )

    # Assign the variable a cookie value.
    cookie_val = a_cookie["user"].value

    # Required header that tells the browser how to render the HTML.
    print "Content-Type: text/html\n\n"

    # Print the cookie value.
    print "<HTML><BODY>"
    print a_cookie["user"].value, a_cookie["cnpj"].value,a_cookie["email"].value, "user cookie set.\n"
    print "</BODY></HTML>\n"

def main():
    form = cgi.FieldStorage()
    cEmpresa = CEmpresa()
    if form.has_key("action") and form.has_key("check"):
        if form["check"].value == "visualizar":
            cEmpresa.exibeCadastro(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value)
        if form["check"].value == "cadastrar":
            cEmpresa.salvaEmpresa(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value)
        #if form["check"].value == "Ir para minha conta":
         #   cEmpresa.exibeConta()
    #else:
        #read_client_Cookie();    
main()