# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User():

    def __init__(self, user_name, user_id, user_access = "Basic Access"):
        self.__user_name = user_name
        self.__user_id = user_id
        self.__user_access = user_access


class Admin(User):

    def __init__(self, user_name, user_id, user_access, admin_access):
        super().__init__(user_name, user_id, user_access)
        self.__admin_access = admin_access
        self.__users = []

    def add_user(self, user_name, user_id, user_access):
        user = User(user_name, user_id, user_access)
        self.__users.append({"name" : user_name,
                             "id" : user_id,
                             "access" : user_access
                             })
        print(f"Добавлен новый пользователь - {user_name}, {user_id}, {user_access}")


    def remove_user(self, user_id):
        user_list = self.__users
        for user in user_list:
            if user["id"] == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user['name']} удален админом")
                break
            else:
                print("Пользователь с введенным ID не найден")

    def info(self):
        print("Список пользователей:")
        user_list = self.__users
        for user in user_list:
            print(f"Имя - {user['name']}, ID - {user['id']}, доступ - {user['access']}")




admin1 = Admin("Ольга", "000", "Basic Access", "Admin Access")
admin1.add_user("Женя", "001", "Basic Access")
admin1.add_user("Таня", "002", "Basic Access")
admin1.add_user("Юля", "003", "Basic Access")
admin1.remove_user("001")
admin1.info()

