from app.controllers.user_controller import (
    get_users, get_user_by_id, create_user, update_user, delete_user
)

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def users():
        return get_users()

    @app.route('/users/<int:user_id>', methods=['GET'])
    def user_detail(user_id):
        return get_user_by_id(user_id)

    @app.route('/users/criar', methods=['POST'])
    def add_user():
        return create_user()

    @app.route('/users/editar/<int:user_id>', methods=['PUT'])
    def edit_user(user_id):
        return update_user(user_id)

    @app.route('/users/del/<int:user_id>', methods=['DELETE'])
    def remove_user(user_id):
        return delete_user(user_id)
