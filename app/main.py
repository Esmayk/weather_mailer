import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from controllers.usuario_controller import endpoint
from services.scheduler_service import start_scheduler_email

app = Flask(__name__)
app.register_blueprint(endpoint)

if __name__ == "__main__":
    start_scheduler_email()
    app.run(debug=True, host="0.0.0.0", port=8000, load_dotenv=True)