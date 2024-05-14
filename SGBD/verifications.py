import os, random, sqlite3
import SGBD.base_datos as BD
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
def send_mail(email, subject):

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    remitente = "Soporte HEALTHSYNC"
    destinatarios = email



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
                    <h1 style="color: #0066ff; font-weight: bold;">{subject}</h1>
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
    msg["Subject"] = subject

    # Adjunta el mensaje HTML al correo electrónico
    msg.attach(MIMEText(mensaje_html, "html"))

    # Crear conexión y enviar correo
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("USER_MAIL"), os.getenv("PASSWORD"))
        server.sendmail(remitente, destinatarios, msg.as_string())
        print("Correo enviado.")
    
    return codigo_verificacion

def code_verification(email, subject):
    code = send_mail(email, subject)
    user_code = input("Código: ")
    if user_code == code:
        print("Código correcto")
        return True
    else:
        print("Código incorrecto")
        return False


def email_verification(email):

    if code_verification(email, subject = "VERIFICACIÓN EMAIL"):
        BD.update_email_status(user= BD.saber_user_con_email(email), future_status=1)
        print(f"El correo {email} ha sido verificado correctamente")
    else:
        #SE MANTIENE EL ESTADO FALSE
        print("No se ha podido verificar el correo")


