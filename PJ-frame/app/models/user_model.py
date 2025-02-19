class User:
    # Simulação de um banco de dados
    users = [
        {"id": 1, "name": "Chris", "email": "chris@example.com"},
        {"id": 2, "name": "Ella", "email": "Ella@example.com"}
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