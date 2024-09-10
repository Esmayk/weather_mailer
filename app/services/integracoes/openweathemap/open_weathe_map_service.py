import requests
from configs.config import Config

class OpenWeatheMapService:
    def __init__(self, latitude, longitude):
        self.api_url = Config.OPEN_WEATHER_MAP_API_URL
        self.api_key = Config.OPEN_WEATHER_MAP_API_KEY
        self.latitude = latitude
        self.longitude = longitude
        self.lang = "pt_br"
        
    def get(self):
        open_wheathe_map_url = f"{self.api_url}?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&lang={self.lang}"
        try:
            response = requests.get(open_wheathe_map_url)
            response.raise_for_status()  # Vai lancar um erro para códigos de status 4xx/5xx
            return response.json()  # Retorna a resposta em formato JSON
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")