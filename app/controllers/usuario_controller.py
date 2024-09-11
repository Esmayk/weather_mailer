import json
from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService
from configs.config import Config

endpoint = Blueprint('usuarios', __name__)
context_api = Config.CONTEXTO_API

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
