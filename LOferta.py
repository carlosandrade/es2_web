#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MOferta
import string
cgitb.enable()


#Cria a classe controller de oferta

class LOferta:
	
    def __init__(self,form=""):
       if form != "":
           if form.has_key("action"):
               if form["action"].value == "TSubmissaoOferta":
		           self.salvaOferta(form["oferta_nome"].value, form["cota_minima"].value, form["preco"].value, form["desconto"].value,form["regulamento"].value,form["validade"].value,form["limite"].value,form["detalhes"].value)

    def salvaOferta(self,nome,cota_minima,preco,desconto,regulamento,validade,limite,detalhes):
        
        oferta = MOferta.Oferta(nome,cota_minima,preco,desconto,regulamento,validade,limite,detalhes)
        oferta.save()
        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2>Os dados da oferta",nome,"foram cadastrados com sucesso</h2>\n"
        print "<p>O que deseja fazer agora?\n<p>"
        print " <a href=\"TSubmissaoOferta.py\">Retornar a tela de submissao de oferta</a>"
        print "</body>"
        print "</html>"

    def exibe_oferta_do_dia(self):
        oferta = MOferta.Oferta()
        ofertas = oferta.openAll()
        for i in range(len(ofertas)):
            campoOfertas = string.split(ofertas[i]," ")
            if (campoOfertas[9] == "oferta_do_dia"):
                oferta.open(campoOfertas[0])
                print "\t<H3>Oferta do dia:<H3>\n"
                print "\t<TABLE BORDER = 0> \n"

                print "\t\t<TR><TH>Nome da oferta: </TH><TH>",oferta.nome,"</TH><TR>\n"

                print "\t\t<TR><TH>Cota minima: </TH><TH>",oferta.cota_minima,"</TH><TR>\n"

                print "\t\t<TR><TH>Preco: </TH><TH>",oferta.preco,"</TH></TR>\n"

                print "\t\t<TR><TH>Desconto oferecido: </TH><TH>",oferta.desconto,"</TH></TR>\n"

                print "\t\t<TR><TH>Regulamento: </TH><TH>",oferta.regulamento,"</TH></TR>\n"
                
                print "\t\t<TR><TH>Validade: </TH><TH>",oferta.validade,"</TH></TR>\n"
                
                print "\t\t<TR><TH>Limite de cupons por pessoa: </TH><TH>",oferta.limite,"</TH></TR>\n"
                
                print "\t\t<TR><TH>Detalhes:</TH><TH>",oferta.detalhes,"</TH></TR>\n"
                
                print "\t</TABLE>\n"

