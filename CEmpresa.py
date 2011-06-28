#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 



# Create instance of FieldStorage 


#Cria a classe controller de empresas

class CEmpresa:

    #def executeOperacao(self,action):
       # if action == "display":
        #    self.exibeCadastro()
     #  print "bla"

   def exibeCadastros(self, name, cnpj, email):
       print "Content-type:text/html\r\n\r\n"
       print "<html>"
       print "<head>"
       print "<title>Hello - Second CGI Program</title>"
       print "</head>"
       print "<body>"
       print "<h2>Hello %s %s %s</h2>" % (name, cnpj,email)
       print "</body>"
       print "</html>"

def main():
    form = cgi.FieldStorage()
    cEmpresa = CEmpresa()
    if form.has_key("action"):
        if form["action"].value == "display":
            cEmpresa.exibeCadastro(form["business_name"].value, form["business_cnpj"].value, form["business_email"].value)

main()