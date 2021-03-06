#!/usr/bin/python

# Import modules for CGI handling 
import sys
sys.path.append("/Library/WebServer/CGI-Executables/")
sys.path.append("/Library/WebServer/CGI-Executables/Logica")
sys.path.append("/Library/WebServer/CGI-Executables/Model")
sys.path.append("/Library/WebServer/CGI-Executables/Tela")
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
                if form["action"].value == "TIndicarAmigo":
	                self.enviarEmail(form["email"].value, form["mensagem"].value)
	                

    def salvaSugestao(self,titulo, mensagem):
        sugestao = MSugestao.Sugestao(titulo,mensagem)
        sugestao.save()
        print "Content-type:text/html\r\n\r\n"
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TEnviarSugestao.py?update=exibeSugestaoSalva\">"
        
#    def enviarEmail(self,email, mensagem):
        
#        import smtplib
#        import getpass

#        SMTP_SERVER = 'smtp.gmail.com'
#        SMTP_PORT = 587

#        sender = 'compron.python@gmail.com'

#        #HERE'S THE PASSWORD, IN PLAIN TEXT
#        password = 'padawan22'
#        recipient = email
#        subject = 'Um amigo seu lhe indicou ao nosso site!'
#        body = "Mensagem do seu amigo: "+mensagem+"\n Atenciosamente, \n A equipe do Compron\n"

#        "Sends an e-mail to the specified recipient."

#        body = "" + body + ""

#        headers = ["From: " + sender,
#                   "Subject: " + subject,
#                   "To: " + recipient,
#                   "MIME-Version: 1.0",
#                   "Content-Type: text/html"]
#        headers = "\r\n".join(headers)

#        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

#        session.ehlo()
#        session.starttls()
#        session.ehlo

        #THIS IS WHERE THE PASSWORD IS USED
#        session.login(sender, password)

#        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
#        session.quit()
                
#        print "Content-type:text/html\r\n\r\n"
#        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TIndicarAmigo.py?update=exibeEmailEnviadoComSucesso\">"



        

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
        print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TCadastroConsumidor.py?update=exibeConsumidorCadastradoComSucesso\">"


