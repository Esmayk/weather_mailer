from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from util.util import Util
from templates.email.email_html import EmailHtml
from .destinatario_service import DestinatarioService
from .integracoes.email.email_service import EmailService
from .integracoes.openweathemap.open_weathe_map_service import OpenWeatheMapService

scheduler = None

def scheduled_email_job():
    print(f"Início do scheduled de envido de e-mail at {datetime.now()}")
    data = OpenWeatheMapService("-3,7028", "-38,573").get()
    velocidade_nos = Util().convert_metros_nos(data['wind']['speed'])
    if velocidade_nos >= 15: 
        html = EmailHtml().gerar_html(data, velocidade_nos)
        destinatarios = DestinatarioService.get_emails()
        EmailService().send_email(destinatarios, html)
    print(f"Fim do scheduled de envido de e-mail at {datetime.now()}")

def start_scheduler_email():
    global scheduler
    if not scheduler:
        scheduler = BackgroundScheduler()
        scheduler.add_job(scheduled_email_job, 'interval', minutes=60)
        scheduler.start()