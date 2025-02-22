from extensions  import db
from model.superUserModel import SuperUser 

class UserService:
    @staticmethod
    def get_user():
        return SuperUser.query.all()
    
    @staticmethod
    def create_user(data):
        new_user = SuperUser(username=data["username"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()
        return new_user
