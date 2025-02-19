from flask import make_response, jsonify, request
from app.models.user_model import User

def get_users():
    
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuarios = User.get_users()
        )
    ) 

def get_user_by_id(user_id):
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuarios = User.get_user_by_id(user_id)
        )
    ) 