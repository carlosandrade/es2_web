#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import MConsumidor, MUsuario,MSugestao
import Cookie, os
cgitb.enable()


#Cria a classe controller de oferta

class LConsumidor:
	
    def __init__(self,form=""):
        if form != "":    
            if form.has_key("action"):
                if form["action"].value == "TCadastroConsumidor":
	                self.salvaConsumidor(form["nome"].value, form["email"].value, form["ncartao"].value, form["tipoCartao"].value, form["login"].value, form["password"].value)
                if form["action"].value == "TEnviarSugestao":
	                self.salvaSugestao(form["titulo"].value, form["mensagem"].value)
	                

    def salvaSugestao(self,titulo, mensagem):
        sugestao = MSugestao.Sugestao(titulo,mensagem)
        sugestao.save()
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/TEnviarSugestao.py?update=exibeSugestaoSalva\">"
        
        

#    def exibeDadosConsumidor(self):
#         a_cookie = Cookie.Cookie( os.environ.get("HTTP_COOKIE", "") )
#         if a_cookie.has_key("login"):
#            consumidor = MConsumidor.Consumidor()
#            consumidor.open(a_cookie["login"].value)
#                         
#            print "\t\t<TR><TH>Nome: </TH><TH>",consumidor.nome,"</TH><TR>\n"

#            print "\t\t<TR><TH>Numero do cartao: </TH><TH>",consumidor.ncartao,"</TH><TR>\n"

#            print "\t\t<TR><TH>Tipo do cartao: </TH><TH>",consumidor.tipoCartao,"</TH><TR>\n"


    def salvaConsumidor(self,nome,email,ncartao,tipoCartao,login,password):
        
        consumidor = MConsumidor.Consumidor(nome,email,ncartao,tipoCartao,login,password)
        consumidor.save()
        usuario = MUsuario.Usuario("consumidor",login,password)
        usuario.save()
        print "Content-type:text/html\r\n\r\n"
        print "<html>"
        print "<head>"
        print "<title>Hello - Second CGI Program</title>"
        print "</head>"
        print "<body>"
        print "<h2>Os dados da oferta",nome,"foram cadastrados com sucesso</h2>\n"
        print "<p>O que deseja fazer agora?\n<p>"
        print " <a href=\"TCadastroConsumidor.py\">Retornar a tela de cadastro de consumidor</a>"
        print "</body>"
        print "</html>"


