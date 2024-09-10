import json
from db.conexao import Database
from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository
from flask import jsonify
class UsuarioService: 
    def buscar_usuarios():
        try:
            db = Database() 
            usuarios_data = UsuarioRepository(db).buscar_usuarios()
            usuarios = []
            if usuarios_data is not None:
                for data in usuarios_data:
                    usuario = Usuario(*data).to_dict()
                    usuarios.append(usuario)
            return  usuarios
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            db.rollback()
        finally:
            db.close()
    
    def inserir_usuario(nome, apelido, email):
        if not nome:
            return jsonify({"error": "Nome é obrigatório"}), 400
        if not apelido:
            return jsonify({"error": "Apelido é obrigatório"}), 400
        if not email:
            return jsonify({"error": "Email é obrigatório"}), 400 
        
        db = Database()
        
        try:
            usuarioExiste = UsuarioRepository(db).buscar_usuario_email(email)
            if usuarioExiste:
                return jsonify({"error": "Usuário já está cadastrado na base de dados!"}), 400
            else:
                usuario_novo = UsuarioRepository(db).inserir_usuario(nome, apelido, email)
                usuario_novo = Usuario(*usuario_novo).to_dict()
                return json.dumps(usuario_novo, indent=4), 201
        except Exception as e:
            db.rollback()
            print(f"Erro ao inserir usuário: {e}")
        finally:
            db.close()