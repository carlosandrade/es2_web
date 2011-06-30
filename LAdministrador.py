#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MEmpresa, Cookie, os
import MOferta

cgitb.enable()

class LAdministrador:
    def __init__(self,form=""):
	
       if form != "":
            if form["action"].value == "TAvaliarOferta":
                if form["check"].value == "avaliar":
                    self.avaliaOferta(form["dropdown"].value)

    #def avaliaOferta(self,nomeOferta):
        #mOferta = MOferta.MOferta()
        #ofertas = mOferta.openAll(nomeOferta)
        

    def exibeOfertas(self):
          mOferta = MOferta.Oferta()
          ofertas = mOferta.openAll()
          return ofertas

#        for oferta in ofertas:
#            ofertaID = string.split(oferta, "")
#            if oferta[0] == ident: #Localizou a oferta do dropdown
#                oferta[9] = "aceita" #Modificou a oferta para aceita

#        file.write(ofertas)