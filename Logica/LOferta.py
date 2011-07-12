#!/usr/bin/python

# Import modules for CGI handling 
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, os, Cookie
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
               elif form["action"].value == "TCompraOferta":
                   a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
                   oferta = self.getOferta(form["nome_oferta"].value)
                   self.compraOferta(a_cookie["login"].value,form["nome_oferta"].value,oferta.validade)
           
    def compraOferta(self,nomeComprador,nomeOferta,validadeOferta,quantidade):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i], " ")
            if campoOferta[0] == nomeOferta:
                campoOferta[10] = campoOferta[10] - quantidade
        mOferta.saveAll(ofertas)
        criaCupom(nomeOferta,validadeOferta,nomeComprador)


    def criaCupom(nomeOferta,validadeOferta,nomeComprador):
        mCupom = MCupom.Cupom(nomeOferta,validadeOferta,nomeComprador)
        mCupom.save()
        

    def ofertaDoDia(self):
         oferta = MOferta.Oferta()
         ofertas = oferta.openAll()
 
         for i in range(len(ofertas)):
             campoOfertas = string.split(ofertas[i]," ")
             if (campoOfertas[9] == "oferta_do_dia"):
                 ofertaDoDia = oferta.open(campoOfertas[0])
                 
         return ofertaDoDia
        

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

    def getOferta(self,nomeOferta):
        oferta = MOferta.Oferta()
        oferta = oferta.open(nomeOferta)
        return oferta
