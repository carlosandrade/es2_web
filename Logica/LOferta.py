#!/usr/bin/python

# Import modules for CGI handling 
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, os, Cookie
import MOferta, MCupom
import string
cgitb.enable()


#Cria a classe controller de oferta

class LOferta:
	
    def __init__(self,form=""):
       if form != "":
           if form.has_key("action"):
               if form["action"].value == "TSubmissaoOferta":
		           self.salvaOferta(form["oferta_nome"].value, form["cota_minima"].value, form["preco"].value, form["desconto"].value,form["regulamento"].value,form["validade"].value,form["limite"].value,form["detalhes"].value,form["quantidade"].value)
               elif form["action"].value == "TCompraOferta":
                   a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
                   oferta = self.getOferta(form["nome_oferta"].value)
                   self.compraOferta(a_cookie["login"].value,form["nome_oferta"].value,oferta.validade,form["dropdown"].value)
           
    def compraOferta(self,nomeComprador,nomeOferta,validadeOferta,quantidade):
        mOferta = MOferta.Oferta()
        ofertas = mOferta.openAll()
        for i in range(len(ofertas)):
            campoOferta = string.split(ofertas[i], " ")
            if campoOferta[0] == nomeOferta:
                campoOferta[10] = str(int(campoOferta[10]) - int(quantidade)) #transforma string em inteiro, subtrai e transforma em string o resultado
                ofertas[i] =""
                for j in range(len(campoOferta)):
                    if campoOferta[j] != "\n":
		                ofertas[i] += campoOferta[j]+" "
                    else:
                       ofertas[i] += campoOferta[j]
        mOferta.saveAll(ofertas)
        self.criaCupom(nomeOferta,validadeOferta,nomeComprador)
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCompraOferta.py?update=exibeCompraRealizada\">"


    def criaCupom(self,nomeOferta,validadeOferta,nomeComprador):
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
        

    def salvaOferta(self,nome,cota_minima,preco,desconto,regulamento,validade,limite,detalhes,quantidade):

        oferta = MOferta.Oferta(nome,cota_minima,preco,desconto,regulamento,validade,limite,detalhes,quantidade)
        oferta.save()
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TSubmissaoOferta.py?update=exibeOfertaSubmetidaComSucesso\">"


    def getOferta(self,nomeOferta):
        oferta = MOferta.Oferta()
        oferta = oferta.open(nomeOferta)
        return oferta
