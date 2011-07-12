#!/usr/bin/python
import cgi, cgitb, string
cgitb.enable()

def default():

    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Enviar Sugestoes</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

    print "\t<H3>Favor preencher os dados requisitados<H3>\n"
    print "\t<TABLE BORDER = 0> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"

    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TEnviarSugestao\">\n"

    print "\t\tTitulo:</TH><TD><INPUT type = text \
    name = \"titulo\"> <br />\n"

    print "\t\tSugestao: <br /><textarea rows=\"30\" name=\"mensagem\" cols=\"40\">"
    print "</textarea>\n"


    print "\t</TABLE>\n"


    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"submeter\">\n"
    print "\t</FORM>\n"


    print "</BODY>\n"
    print "</HTML>\n"
    
def sugestaoEnviadaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Sugestao enviada com sucesso!</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Sugestao enviada com sucesso. Obrigado!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"

def main():
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "exibeSugestaoSalva":
            sugestaoEnviadaComSucesso()
        #elif form["update"].value == "exibeOfertaRecusada":
        #    ofertaRecusadacomSucesso()
        else:
            default()                                            
    else:  
        default()


    
main()