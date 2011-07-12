#!/usr/bin/python

import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")

import cgi, cgitb, string
cgitb.enable()


class Usuario:
 
    def __init__(self,login="",senha="",tipo=""):
        self.login = login
	self.senha = senha
	self.tipo = tipo


    def save(self):
        file = open("usuarios.txt","a+")
        file.write(self.login+" "+self.senha+" "+self.tipo+" \n")
        file.close()

    def openAll(self):
        file = open("usuarios.txt","r+")
        usuarios = file.readlines()
        file.close()
        return usuarios

    def saveAll(self,usuarios):
        file = open("usuarios.txt","w")
        file.close
        file = open("usuarios.txt","a+")
        for usuario in usuarios:
            file.write(usuario)
        file.close()

    def open(self,nomeUsuario):
        file = open("usuarios.txt","r+")
      	usuarios = file.readlines()
        file.close()
        for usuario in usuarios:
            campoUsuario = string.split(usuario)
            if campoUsuario[0] == nomeUsuario:
                return campoUsuario
        return "not_found"            


