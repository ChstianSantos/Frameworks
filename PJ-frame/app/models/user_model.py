class User:
    # Simulação de um banco de dados
    users = [
        
        {"id": 1, "name": "Merc1", "cnpj":"11222333000166", "email": "Merc1@example.com" ,"celular": "99999999", "senha": "senha", "status": "activo"},
        
        ]

    @classmethod
    def get_users(cls):
        return cls.users

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users:
            if user["id"] == user_id:
                return user
        return None

    @classmethod
    def create_user(cls, data):
        new_id = max(user["id"] for user in cls.users) + 1 if cls.users else 1
        new_user = {"id": new_id, "name": data["name"], "cnpj": data["cnpj"], "email": data["email"], "celular": data["celular"], "senha": data["senha"], "status": data["status"]}
        cls.users.append(new_user)
        return new_user

    @classmethod
    def update_user(cls, user_id, data):
        for user in cls.users:
            if user["id"] == user_id:
                user.update(data)
                return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        cls.users = [user for user in cls.users if user["id"] != user_id]
