import yagmail

email= 'santiagolozman5@gmail.com'
contraseña = 'msdmjlrzzcquqvhz'

yag = yagmail.SMTP(user=email, password=contraseña)

destinatarios = ['santiagolozman@gmail.com']
asunto = 'Prueba de envio de correo'
mensaje = 'Mensaje de prueba dentro del correo'
html = '<h1>Hola soy un titulo</h1>'
archivo = './main.py'

yag.send(destinatarios, asunto, mensaje [mensaje, html], attachments=[archivo, 'texto.txt'])