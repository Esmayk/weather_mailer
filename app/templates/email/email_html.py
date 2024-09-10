from datetime import datetime

class EmailHtml:
    def __init__(self):
        self.data = None

    def gerar_html(self, data, velocidade_nos):
        self.data = data
        formatted_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        weather_icon_url = f"https://cdn2.iconfinder.com/data/icons/weather-flat-14/64/weather02-512.png"
        wind_icon_url = "https://cdn3.iconfinder.com/data/icons/scenarium-vol-20/128/020_042-256.png" 
        wind_direction_url = "https://www.example.com/icons/wind_direction.png"

        velocidade_nos = velocidade_nos
    
        html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Relatório de Clima</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 80%;
                    margin: auto;
                    overflow: hidden;
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #333;
                }}
                .weather-info {{
                    display: flex;
                    align-items: center;
                    border-bottom: 1px solid #ddd;
                    padding-bottom: 10px;
                    margin-bottom: 10px;
                }}
                .weather-info img {{
                    width: 50px;
                    height: 50px;
                    margin-right: 10px;
                }}
                .weather-info div {{
                    flex: 1;
                }}
                .weather-info p {{
                    margin: 0;
                }}
                .wind-info {{
                    display: flex;
                    align-items: center;
                    border-bottom: 1px solid #ddd;
                    padding-bottom: 10px;
                    margin-bottom: 10px;
                }}
                .wind-info img {{
                    width: 40px;
                    height: 40px;
                    margin-right: 10px;
                }}
                .footer {{
                    text-align: center;
                    font-size: 0.9em;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Relatório do Clima</h1>
                <p><strong>Local:</strong> {self.data['name']}</p>
                <p><strong>Data e Hora:</strong> {formatted_now}</p>

                <div class="weather-info">
                    <img src="{weather_icon_url}" alt="Ícone do Clima">
                    <div>
                        <p><strong>Condição:</strong> {self.data['weather'][0]['description'].capitalize()}</p>
                        <p><strong>Temperatura:</strong> {self.data['main']['temp'] - 273.15:.1f}°C</p>
                        <p><strong>Sensação Térmica:</strong> {self.data['main']['feels_like'] - 273.15:.1f}°C</p>
                    </div>
                </div>

                <div class="wind-info">
                    <img src="{wind_icon_url}" alt="Ícone do Vento">
                    <div>
                        <p><strong>Velocidade do Vento:</strong> {velocidade_nos} nós</p>
                        <p><strong>Direção do Vento:</strong> <img src="{wind_direction_url}" alt="Direção do Vento" title="Direção do Vento {self.data['wind']['deg']}°"></p>
                    </div>
                </div>

                <p><strong>Coordenadas:</strong> Latitude {self.data['coord']['lat']}, Longitude {self.data['coord']['lon']}</p>
                <p><strong>País:</strong> {self.data['sys']['country']}</p>
                <p><strong>Zona Horária:</strong> GMT{self.data['timezone'] // 3600}</p>

                <div class="footer">
                    <p>Este é um relatório automático gerado pelo sistema de previsão do tempo.</p>
                </div>
            </div>
        </body>
        </html>
        """
        return html