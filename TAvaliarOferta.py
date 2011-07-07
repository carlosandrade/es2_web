#!/usr/bin/python

# Import the CGI, string, sys, and md5crypt modules
import cgi, cgitb, string
import FNegocio
cgitb.enable() 

def ofertaDoDiaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Oferta do dia definida com sucesso...</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Oferta do dia definida com sucesso!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"


def ofertaAceitaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Oferta aceita com sucesso...</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Oferta aceita com sucesso!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"
    
def ofertaRecusadacomSucesso():

    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Oferta recusada com sucesso...</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Oferta recusada com sucesso!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"

def ofertaRecusadaModificacaoComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Oferta recusada exigindo modificacoes...</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Oferta recusada exigindo modificacoes com sucesso<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"

def default():
    #a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Avaliar Oferta</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print "\t<H3>Ofertas Pendentes<H3>\n"
    print "\t<TABLE BORDER = 4> \n"
    print "\t\t<TR> \
    <TH>Titulo</TH>\n"
    print "<TH>Cota Minima</TH>\n"
    print "<TH>Preco</TH>\n"
    print "<TH>Desconto Oferecido</TH>\n"
    print "<TH>Regulamento</TH>\n"
    print "<TH>Validade</TH>\n"
    print "<TH>Limite de Compras por pessoa</TH>\n"
    print "<TH>Detalhes</TH>\n"
    print "<TH>Reputacao</TH>\n"
    print "<TH>Status</TH>\n"
    print "</TR>\n"    
   # print "\t<TABLE BORDER = 4> \n"
    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"
    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TAvaliarOferta\">\n"
    fNegocio = FNegocio.FNegocio()
    ofertasPendentes = fNegocio.administradorGetDadosOfertasPendentes()
    
    for oferta in ofertasPendentes:
        campoOferta = string.split(oferta)
        print "<TR>\n"
        for i in range(10):
            print "<TH>",campoOferta[i],"</TH>"
    print "</TABLE>" 
    
    ofertasDropdown = fNegocio.administradorDropOfertasPendentes()
    
    print "\t\t<SELECT NAME = \"dropdown\">"
    for oferta in ofertasDropdown:
        nomeOferta = string.split(oferta, " ")
        print "\t\t<OPTION VALUE=\"%s\">%s</ OPTION >" % (nomeOferta[0],nomeOferta[0])
    print "\t\t</SELECT>"
        
        
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"aceitar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"recusar\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"modificacao\">\n"
    print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"oferta do dia\">\n"

    print "\t</FORM>\n"
    print "</BODY>\n"
    print "</HTML>\n"


def main():
    form = cgi.FieldStorage()
    if form.has_key("update"):
        if form["update"].value == "exibeOfertaAceita":
            ofertaAceitaComSucesso()
        elif form["update"].value == "exibeOfertaRecusada":
            ofertaRecusadacomSucesso()
        elif form["update"].value == "exibeDiaOferta":
            ofertaDoDiaComSucesso()
        else:
            default()                                            
    else:  
        default()





main()
