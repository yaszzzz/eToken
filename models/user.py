class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_user_info(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"