import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
import ssl
import smtplib

import os
#COE_JEMOP10**
# sxgpfagbgxkqtxrz

# comando para buscar los archivos
# python -c "import sys; print(sys.executable)"
# C:\Users\Nicolas.Valbuena\AppData\Local\Programs\Python\Python310\python.exe

#blica-jemop@blica-426315.iam.gserviceaccount.com

def enviar_correo(destinatarios, archivo, nombre_archivo):
    print(destinatarios)
    # Iniciamos los parámetros del script
    ruta_archivos = archivo

    remitente = 'coejemop@gmail.com'
    contrasena = 'sxgpfagbgxkqtxrz'
    
    asunto = '[RPI] resultados estadisticos del ECJ'
    cuerpo = 'RESULTADOS DEL CENTRO DE OPERACIONES DEL EJC.'
    ruta_adjunto = ruta_archivos
    nombre_adjunto = nombre_archivo


    # em = EmailMessage()
    # em['From'] = remitente
    # em['To'] = destinatarios
    # em['Subject'] = cuerpo
    # em.set_content(cuerpo)


    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
    
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login(remitente,contrasena)

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)


    # contexto = ssl.create_default_context()

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    #     smtp.login(remitente, contrasena)
    #     smtp.sendmail(remitente,destinatarios, em.as_string())

    # Cerramos la conexión
    print("correos envaidos")
    sesion_smtp.quit()