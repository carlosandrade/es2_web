#!/usr/bin/python
import cgi, cgitb, string
cgitb.enable()


class Sugestao:
 
    def __init__(self,titulo="",mensagem=""):
        self.titulo = titulo
        self.mensagem = mensagem

    def save(self):
        file = open("sugestoes.txt","a+")
        file.write(self.titulo+" "+self.mensagem+" \n")
        file.close()

    def openAll(self):
        file = open("sugestoes.txt","r+")
        sugestoes = file.readlines()
        file.close()
        return sugestoes

    def saveAll(self,sugestoes):
        file = open("sugestoes.txt","w")
        file.close
        file = open("sugestoes.txt","a+")
        for sugestao in sugestoes:
            file.write(sugestao)
        file.close()
