import json
from flask_cors import CORS
from configs.config import Config
from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

context_api = Config.CONTEXTO_API

endpoint = Blueprint('usuarios', __name__)
CORS(endpoint, resources={r"/*": {"origins": "*"}})

@endpoint.route(f"{context_api}/usuarios", methods=['GET'])
def buscar_usuarios():
    usuarios = UsuarioService.buscar_usuarios()
    if usuarios == []:
        return jsonify({"error": "Nenhum resultado encontrado!"}), 400
    else:
        return json.dumps(usuarios, indent=4)

@endpoint.route(f"{context_api}/usuarios", methods=['POST'])
def create_usuario():
    data = request.get_json()
    return UsuarioService.inserir_usuario(data.get('nome'), data.get('apelido'), data.get('email'))

@endpoint.route("/")
def index():
    return jsonify({"status":"UP"})
