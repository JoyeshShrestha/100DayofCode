class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False


def check_authentication(function):
    def wrapper_function(*args,**kwargs):
        if args[0].is_logged_in == True:
           return createUser(args[0])
    return wrapper_function        


# user = User()
@check_authentication
def createUser(user):
    print(f"This is {user.name}'s blog")


new_user = User('Joyesh')
new_user.is_logged_in = True
createUser(new_user)