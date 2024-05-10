import os, random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Creamos el código de verificación o cambio de contraseña
def crear_codigo():
    codigo = ""
    for i in range(6):
        numero = random.randint(0, 9)
        codigo += str(numero)
    
    return codigo


# Función que manda un correo con el código de verificación
def send_mail():

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    remitente = "Soporte HEALTHSYNC"
    destinatarios = ["pabgarcia2005@gmail.com"]



    codigo_verificacion = crear_codigo()
    # Mensaje en formato HTML
    mensaje_html = f"""
    <html>
    <body>
        <table style="width: 100%; background-color: #f2f2f2;">
        <tr>
            <td align="center">
            <table style="width: 80%; border: 2px solid #0066ff; border-radius: 10px; padding: 20px; background-color: #ffffff;">
                <tr>
                <td style="text-align: center;">
                    <h1 style="color: #0066ff; font-weight: bold;">CAMBIO DE CONTRASEÑA</h1>
                    <p style="font-size: 18px; color: #000000;">El código es:</p>
                    <p style="font-size: 75px; color: #000000; font-weight: bold;">{codigo_verificacion}</p>
                    <p style="font-size: 10px; color: #0066ff; margin-top: 20px;">HealthSync™ - Todos los derechos reservados © 2024</p>
                </td>
                </tr>
            </table>
            </td>
        </tr>
        </table>
    </body>
    </html>
    """

    # Crea la instancia del mensaje
    msg = MIMEMultipart()
    msg["From"] = remitente
    msg["To"] = ", ".join(destinatarios)
    msg["Subject"] = "Cambio de contraseña"

    # Adjunta el mensaje HTML al correo electrónico
    msg.attach(MIMEText(mensaje_html, "html"))

    # Crear conexión y enviar correo
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("USER_MAIL"), os.getenv("PASSWORD"))
        server.sendmail(remitente, destinatarios, msg.as_string())
        print("Correo enviado.")
    
    return codigo_verificacion


send_mail()