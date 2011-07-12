#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
import cgi, cgitb, string
cgitb.enable()


class Sugestao:
 
    def __init__(self,titulo="",mensagem=""):
        self.titulo = titulo
        self.mensagem = mensagem

    def save(self):
        file = open("/Library/WebServer/CGI-Executables/Banco/sugestoes.txt","a+")
        file.write(self.titulo+" "+self.mensagem+" \n")
        file.close()

    def openAll(self):
        file = open("/Library/WebServer/CGI-Executables/Banco/sugestoes.txt","r+")
        sugestoes = file.readlines()
        file.close()
        return sugestoes

    def saveAll(self,sugestoes):
        file = open("/Library/WebServer/CGI-Executables/Banco/sugestoes.txt","w")
        file.close
        file = open("/Library/WebServer/CGI-Executables/Banco/sugestoes.txt","a+")
        for sugestao in sugestoes:
            file.write(sugestao)
        file.close()

