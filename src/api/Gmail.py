import smtplib
import email.mime.multipart
import email.mime.base
import os
import configparser
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')

correo = config['DEFAULT']['correo']
pas = config['DEFAULT']['pas']

# Creo la conexión SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)

# Inicia sesión en la cuenta de Gmail
server.starttls()
server.login(correo, pas)

# Defino el remitente y destinatario del correo electrónico
remitente = "santiagolozman5@gmail.com"
destinatario = "santiagolozman@gmail.com"

# Creo el mensaje del correo electrónico
mensaje = email.mime.multipart.MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = "INFORMACIÓN ODONTOGRAMA"

# Añado el cuerpo del mensaje
cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n TEAM JAG[JULIETH, ANDRÉS, GONZALO]"
mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

# Convierto el mensaje a texto plano
texto = mensaje.as_string()

#Capturo los errores
try:
    # Enviar el correo electrónico
    server.sendmail(remitente, destinatario, texto)
    print("El correo electrónico se envió correctamente.")
except Exception as e:
    print("Error al enviar el correo electrónico:", str(e))

# Cerrar la conexión SMTP
server.quit()
