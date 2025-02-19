from app.controllers.user_controller import get_users, get_user_by_id

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def users():
        return get_users()

    @app.route('/users/<int:user_id>', methods=['GET'])
    def user_detail(user_id):
        return get_user_by_id(user_id)
