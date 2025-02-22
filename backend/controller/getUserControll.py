from service.superUserService import UserService

def get_users_controll():
    users = UserService.get_user()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return user_list
