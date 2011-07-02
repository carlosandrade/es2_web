#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules
import cgi, cgitb, string
import FNegocio
cgitb.enable() 


def main():
    #a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Avaliar Oferta</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Ofertas Pendentes<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"
    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    #\"TAvaliarOferta\">\n"
    fNegocio = FNegocio.FNegocio()
    fNegocio.administradorExibeDadosOfertasPendentes()
    fNegocio.administradorDropOfertasPendentes()
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"avaliar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"recusar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"modficacao\">\n"

    

    #print "\t\t<TR><TH>Usuario: ",a_cookie["user"].value,"</TH><TD>\n"
    #print "\t\t<TR><TH>CNPJ: ",a_cookie["cnpj"].value,"</TH><TD>\n"
    #print "\t\t<TR><TH>Email: ",a_cookie["email"].value,"</TH><TD>\n"

    print "\t</TABLE>\n"
    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"

main()
