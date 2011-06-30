#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MEmpresa, Cookie, os
import MOferta

cgitb.enable()

class LAdministrador:
    def __init__(self,form=""):
       if form.has_key("action"):
            if form["action"].value == "TAvaliarOferta":
                if form["check"].value == "avaliar":
                    self.avaliaOferta(form["dropdown"].value)

    def avaliaOferta(self,nomeOferta):
        mOferta = MOferta.MOferta()
        mOferta.open(nomeOferta)