#!/usr/bin/python
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb
import Cookie, os
#import FNegocio
cgitb.enable()


def compraRealizadaComSucesso():
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Compra realizada com sucesso</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY>\n"
    print "\t<H3>Sua compra foi realizada com sucesso!<H3>\n"  
    print "</BODY>\n"
    print "</HTML>\n"

def default(form): 
        
    print "Content-type:text/html\r\n\r\n"
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Compra de ofertas</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"

   # fNegocio = FNegocio.FNegocio()
    

    print "\t<H3>Comprar oferta:<H3>\n"
    print "\t<TABLE BORDER = 0> \n"

    print "\t\t<FORM METHOD = post ACTION = \
    \"/cgi-bin/FNegocio.py\">\n"
    
    print form["action"].value
    
    print "\t<INPUT TYPE=HIDDEN NAME = \"nome_oferta\" VALUE = \
    \"%s\">\n" % (form["dropdown"].value)
    
    print "\t<INPUT TYPE=HIDDEN NAME = \"action\" VALUE = \
    \"TCompraOferta\">\n"

    #fNegocio.telaPrincipalExibeOfertaDia()
    #fNegocio.exibeDadosCompraConsumidor()
    import FNegocio
    fNegocio = FNegocio.FNegocio()
    oferta = fNegocio.getOferta(form["dropdown"].value)
    
    #print "\t<H3>Oferta do dia:<H3>\n"
    #print "\t<TABLE BORDER = 0> \n"
    
    

    print "\t\t<TR><TH>Nome da oferta: </TH><TH>",oferta.nome,"</TH><TR>\n"

    print "\t\t<TR><TH>Cota minima: </TH><TH>",oferta.cota_minima,"</TH><TR>\n"

    print "\t\t<TR><TH>Preco: </TH><TH>",oferta.preco,"</TH></TR>\n"

    print "\t\t<TR><TH>Desconto oferecido: </TH><TH>",oferta.desconto,"</TH></TR>\n"

    print "\t\t<TR><TH>Regulamento: </TH><TH>",oferta.regulamento,"</TH></TR>\n"
            
    print "\t\t<TR><TH>Validade: </TH><TH>",oferta.validade,"</TH></TR>\n"
            
    print "\t\t<TR><TH>Limite de cupons por pessoa: </TH><TH>",oferta.limite,"</TH></TR>\n"
            
    print "\t\t<TR><TH>Detalhes:</TH><TH>",oferta.detalhes,"</TH></TR>\n"
            
    print "\t</TABLE>\n"


    quantidade_compra = min(int(oferta.quantidade),int(oferta.limite))
    #print "\t</TABLE>\n"
    
    if quantidade_compra == 0 :
        print "Sentimos muito, mas a oferta esta esgotada!! Verifique em breve!"
    else:
        print "\t\t<SELECT NAME = \"dropdown\">"

        for i in range(1,int(quantidade_compra)+1):
            print "\t\t<OPTION VALUE=\"%s\">%s</ OPTION >" % (i,i)                
            print "\t\t</SELECT>"
            print "\t<INPUT TYPE = submit NAME = \"check\" VALUE = \"Comprar oferta\">\n"
    print "\t</FORM>\n"
  
    print "</BODY>\n"
    print "</HTML>\n"	
	
def main():
    form = cgi.FieldStorage()
    if form.has_key("action"):
        if form["action"].value == "TPrincipal":
            default(form)
    elif form.has_key("update"):
        if form["update"].value == "exibeCompraRealizada":
            compraRealizadaComSucesso()

main()