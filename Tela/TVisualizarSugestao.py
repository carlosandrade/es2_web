#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
import FNegocio
cgitb.enable()

def main():
    #a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Visualizar Sugestao</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Sugestoes<H3>\n"
    print "\t<TABLE BORDER = 4> \n"
    print "\t\t<TR> \
    \n"
    print "<TH>Titulo</TH>\n"
    print "<TH>Mensagem</TH>\n"
    print "</TR>\n"    
   # print "\t<TABLE BORDER = 4> \n"
  #  print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
  #  \"TAvaliarOferta\">\n"
    fNegocio = FNegocio.FNegocio()
    sugestoes = fNegocio.administradorGetSugestoes()
    
    for sugestao in sugestoes:
        campoSugestao = string.split(sugestao)
        print "<TR>\n"
        for i in range(len(campoSugestao)):
            print "<TH>",campoSugestao[i],"</TH>"
    print "</TABLE>"
    print "</BODY>"
    print "</HTML>"
    
main()