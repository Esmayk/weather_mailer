import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    #Contexto da aplicacao
    CONTEXTO_API  = os.getenv("CONTEXTO_API")
    #Banco de dados.
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    #Api OpenWeatherMap
    OPEN_WEATHER_MAP_API_URL = os.getenv("OPEN_WEATHER_MAP_API_URL")
    OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
    #envio de email
    EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
    EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
    EMAIL_SMTP_PORT = os.getenv("EMAIL_SMTP_PORT")