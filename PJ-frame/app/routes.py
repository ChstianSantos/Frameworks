from app.controllers.user_controller import delete_user_by_id, get_users, get_user_by_id, store, update_user_by_id

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def users():
        return get_users()

    @app.route('/users/<int:user_id>', methods=['GET'])
    def user_detail(user_id):
        return get_user_by_id(user_id)
    
    @app.route('/users/', methods=['POST'])
    def store_user():
        return store()

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        return delete_user_by_id(user_id)
    
    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        return update_user_by_id(user_id)
