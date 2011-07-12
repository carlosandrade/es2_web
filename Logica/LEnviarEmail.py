#!/usr/bin/python
import cgi, cgitb


def enviarEmail(email, titulo, mensagem):
    
    import smtplib
    import getpass

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    sender = 'compron.python@gmail.com'

    #HERE'S THE PASSWORD, IN PLAIN TEXT
    password = 'padawan22'
    recipient = email
    subject = titulo
    body = "Mensagem do seu amigo: "+mensagem+"\n Atenciosamente, \n A equipe do Compron\n"

    "Sends an e-mail to the specified recipient."

    body = "" + body + ""

    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo

    #THIS IS WHERE THE PASSWORD IS USED
    session.login(sender, password)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()
    
def main(form=""):
    #form = cgi.FieldStorage()
    if form!="":
        if form.has_key("action"):
            if form["action"].value == "TRecomendarOferta":
                enviarEmail(form["email"].value,"Um amigo lhe recomendou uma oferta do Compron!",form["mensagem"].value)
                print "Content-type:text/html\r\n\r\n"
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TRecomendarOferta.py?update=exibeEmailEnviadoComSucesso\">"
            elif form["action"].value == "TIndicarAmigo":
                enviarEmail(form["email"].value,"Um amigo lhe indicou ao site do Compron!",form["mensagem"].value)
                print "Content-type:text/html\r\n\r\n"
                print "<meta HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=/cgi-bin/Tela/TIndicarAmigo.py?update=exibeEmailEnviadoComSucesso\">"
    #elif form.has_key("update"):
     #   if form["update"].value == "exibeEmailEnviadoComSucesso":
      #      emailEnviadoComSucesso()
        #elif form["update"].value == "exibeOfertaRecusada":
        #    ofertaRecusadacomSucesso()
       # else:
                #default(form)                                            
    #else:  
     #   default(form)
main()
