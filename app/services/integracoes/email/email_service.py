import smtplib
from configs.config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self):
        self.smtp_server = Config.EMAIL_SMTP_SERVER
        self.smtp_port = Config.EMAIL_SMTP_PORT
        self.username = Config.EMAIL_LOGIN
        self.password = Config.EMAIL_PASSWORD

    def send_email(self, to_address, html):
        to_address = to_address
        msg = MIMEMultipart()
        msg['Subject'] = "Atualização Importante: Informações sobre a Velocidade e Direção do Vento"
        msg['From'] = self.username
        msg['To'] = to_address
        
        msg.attach(MIMEText(html, 'html'))
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, to_address, msg.as_string())
                print("E-mail enviado com sucesso!")
        except Exception as e: 
                print(f"Erro ao enviar e-mail: {e}")