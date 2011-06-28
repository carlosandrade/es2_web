#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
#import business_logic.CEmpresa

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
business_name = form.getvalue('business_name')
business_cnpj  = form.getvalue('business_cnpj')
business_email  = form.getvalue('business_email')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s %s</h2>" % (business_name, business_cnpj,business_email)
print "</body>"
print "</html>"
