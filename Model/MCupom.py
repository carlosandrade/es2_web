#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()


class Cupom:
 
    def __init__(self,nomeConsumidor="",nomeOferta="",validade=""):
        self.nomeConsumidor = nomeConsumidor
        self.nomeOferta = nomeOferta
        self.validade = validade


    def save(self):
        file = open("/Library/WebServer/CGI-Executables/Banco/cupoms.txt","a+")
        file.write(self.nomeConsumidor+" "+self.nomeOferta+" "+self.validade+" \n")
        file.close()

    def openAll(self):
        file = open("/Library/WebServer/CGI-Executables.Banco/cupoms.txt","r+")
        cupoms = file.readlines()
        file.close()
        return cupoms

    def saveAll(self,cupoms):
        file = open("/Library/WebServer/CGI-Executables/Banco/cupoms.txt","w")
        file.close
        file = open("/Library/WebServer/CGI-Executables/Banco/cupoms.txt","a+")
        for cupom in cupoms:
            file.write(cupom)
        file.close()

