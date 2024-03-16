from src.responses.HttpResponse import HttpResponse

class UserController:
    def get_all_users():
        return HttpResponse(200, [], None).send()
    
    def create_user():
        return HttpResponse(201, None, "User created").send()

    def update_user(user_id):
        return HttpResponse(200, None, "User updated").send()
    
    def remove_user(user_id):
        return HttpResponse(200, None, "User removed").send()