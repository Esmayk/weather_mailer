from flask import Flask
from controllers.usuario_controller import endpoint
from services.scheduler_service import start_scheduler_email
from services.destinatario_service import DestinatarioService

app = Flask(__name__)
app.register_blueprint(endpoint)
#app.config.from_object('app.config.Config')

if __name__ == "__main__":
    start_scheduler_email()
    #dest = DestinatarioService.get_emails()
    #print(f"Destinatario:{dest}")
    app.run(debug=True, host="0.0.0.0", port=8000, load_dotenv=True)