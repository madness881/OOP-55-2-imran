def check_user(user):
    def decorator(func):
        def wrapper():

            if user == "admin":
                func()
            else:

                print('=============')
                print('Вход запрещен')
        return wrapper
    return decorator

@check_user("admin")
def delete_database():
    print('База данных удаляется\n Осталось:96%')
@check_user("quest")
def delete_logs():
    print('Логи удалены')

delete_database()
delete_logs()
