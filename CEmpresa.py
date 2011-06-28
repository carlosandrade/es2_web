#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MEmpresa
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

    def salvaEmpresa(self,name,cnpj,email):
        
        empresa = MEmpresa.Empresa(name,cnpj,email)
        empresa.save()
        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2>Os dados da empresa",name,"foram cadastrados com sucesso</h2>"
        print "</body>"
        print "</html>"


def main():
    form = cgi.FieldStorage()
    cEmpresa = CEmpresa()
    if form.has_key("action"):
        if form["check"].value == "visualizar":
            cEmpresa.exibeCadastro(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value)
        if form["check"].value == "cadastrar":
            cEmpresa.salvaEmpresa(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value)

main()