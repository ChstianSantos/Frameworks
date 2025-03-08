from flask import make_response, jsonify, request
from app.models.user_model import User


def get_users():
    return make_response(
        jsonify(
            mensagem="Listagem de usuários",
            usuarios=User.get_users()
        )
    )

def get_user_by_id(user_id):
    return make_response(
        jsonify(
            mensagem="Detalhes do usuário",
            usuario=User.get_user_by_id(user_id)
        )
    )

def create_user():
    data = request.get_json()
    novo_usuario = User.create_user(data)
    return make_response(
        jsonify(
            mensagem="Usuário criado com sucesso",
            usuario=novo_usuario
        ), 201
    )

def update_user(user_id):
    data = request.get_json()
    usuario_atualizado = User.update_user(user_id, data)
    return make_response(
        jsonify(
            mensagem="Usuário atualizado com sucesso",
            usuario=usuario_atualizado
        )
    )

def delete_user(user_id):
    User.delete_user(user_id)
    return make_response(
        jsonify(
            mensagem="Usuário deletado com sucesso"
        ), 200
    )
