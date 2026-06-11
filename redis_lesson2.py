# Завдання 1
# Створіть додаток «Соціальна мережа», який зберігає
# інформацію про користувача, його друзів, публікації користувача.
# Можливості додатку:
# ■ вхід за логіном і паролем;
# ■ додати користувача;
# ■ видалити користувача;
# ■ редагувати інформацію про користувача;
# ■ пошук користувача за ПІБ;
# ■ перегляд інформації про користувача;
# ■ перегляд усіх друзів користувача;
# ■ перегляд усіх публікацій користувача.


# як зберігатимемо дані
# інформацію про користувача -- ім'я вік місто
# personal_info:{user_name} -- {"name": "anton", "age":31}

# хто кому друг
# friends:{user_name} -- множина

# публікації
# story:{user_name}:{story_name} -- str

# логіни та паролі
# credential:{user_name} -- str(пароль)

from redis import Redis

#
# class SocialApp:
#     def __init__(self):
#         self.server = Redis(
#             host="localhost",
#             port=6379,
#             db=0, # індекс бази даних
#             decode_responses=True,
#         )
#
#         # користувач який зараз зараєстрований
#         self.current_user = None
#
#     # отримання ключів для бази даних
#     def _get_cred_key(self, user_name):
#         return f"credential:{user_name}"
#
#     def _get_info_key(self, user_name):
#         return f"personal_info:{user_name}"
#
#     def _get_friends_key(self, user_name):
#         return f"friends:{user_name}"
#
#     def _get_story_key(self, user_name, story_name):
#         return f"story:{user_name}:{story_name}"
#
# # ■ вхід за логіном і паролем;
#     def login(self, user_name, password):
#         key = self._get_cred_key(user_name)
#
#         # перевірка чи існує логін
#         if not self.server.exists(key):
#             print("користувача з таким логіном не існує")
#             return
#
#         # отримуємо справжній пароль з бази даних
#         true_password = self.server.get(key)
#
#         if true_password != password:
#             print("ви ввели не правильний пароль")
#             return
#
#         self.current_user = user_name
#         print("ви ввійшли")
#
#
#     def signup(self, user_name, password):
#         key = self._get_cred_key(user_name)
#
#         # перевірка чи такий користувач існує
#         if self.server.exists(key):
#             print("Користувач з таким логіном уже існує")
#             return
#
#         # реєструємо користувача
#         # добавити його логін та пароль в базу даних
#
#         self.server.set(key, password)
#         print("Користувача зареєстровано")
#
#     def add_info(self, name, age, city):
#         # перевірка чи користувач залогінився
#         if self.current_user is None:
#             print("ви не залогінилися")
#             return
#
#         # отримуємо ключ для користувача чкий попередньо залогінився
#         key = self._get_info_key(self.current_user)
#
#         data = {
#             "name": name,
#             "age": age,
#             "city": city
#         }
#
#         self.server.hmset(key, data)
#         print("дані оновлено")
#
# # ■ перегляд інформації про користувача;
#     def get_info(self):
#         # перевірка чи користувач залогінився
#         if self.current_user is None:
#             print("ви не залогінилися")
#             return
#
#         key = self._get_info_key(self.current_user)
#         data = self.server.hgetall(key)
#
#         print(f"Ваші дані: {data}")
#
# # ■ перегляд усіх друзів користувача;
#     def add_friend(self, friend):
#         # перевірка чи користувач залогінився
#         if self.current_user is None:
#             print("ви не залогінилися")
#             return
#
#         # перевірка чи друг є серед користувачів(чи існує його пароль в базі даних)
#         friend_key = self._get_cred_key(friend)
#         if not self.server.exists(friend_key):
#             print("невідомий друг")
#             return
#
#         # добавляємо друга
#         key = self._get_friends_key(self.current_user)
#         self.server.sadd(key, friend)
#
#         # добавити нас в друзі до friend
#         friend_key = self._get_friends_key(friend)
#         self.server.sadd(friend_key, self.current_user)
#
#         print("друга додано")
#
#     def get_friends(self):
#         if self.current_user is None:
#             print("ви не залогінилися")
#             return
#
#         # отримуємо всіх друзів
#         key = self._get_friends_key(self.current_user)
#         friends = self.server.smembers(key)
#
#         print(f"Ваші друзі: {friends}")
#
# # ■ перегляд усіх публікацій користувача.
#     def add_story(self, story_name, content):
#         if self.current_user is None:
#             print("ви не залогінилися")
#             return
#
#         key = self._get_story_key(self.current_user, story_name)
#         # перевірка чи немає піблікації з такою ж назвою
#         if self.server.exists(key):
#             print("У вас уже є піблікація з такою назвою")
#             return
#
#         self.server.set(key, content)
#
#
# app = SocialApp()
#
#
# # app.signup("John", "qwerty21")
#
# app.login("Mary", "qwerty21")
# #app.add_info(name="Anton Halysh", age=24, city="Kyiv")
# # app.get_info()
# # app.add_friend("Mary")
# # app.get_friends()
# app.add_story("python", "це мова програмування")
# app.add_story("exam", "екзамен у вівторок")
# app.add_story("ai", "це штучний інтелект")





# Завдання 2
# Створіть додаток «Музей літератури». Додаток має зберігати
# інформацію про експонати та людей, які мають відношення
# до експонатів. Можливості додатку:

class MuseumApp:
    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True
        )

        self.current_user = None
        self.is_login = False

# password:{name} password
# exponat:{exp_name} description
# people:{name} description
# exponat:exp_name:people

    def _get_cred_key(self, name):
        return f"password:{name}"

    def _get_exp_key(self,exp_name):
        return f"exponat:{exp_name}"

    def _get_people_key(self,name):
        return f"people:{name}"

    def _related_key(self,exp_name,people):
        return f"exponat:{exp_name}:{people}"


# ■ вхід за логіном і паролем;
    def login(self,name, password):
        key = self._get_cred_key(name)

        if not self.server.exists(key):
            print("user doesnt exist")
            return

        true_password = self.server.get(key)
        if true_password != password:
            print("incorect password")
            return

        self.is_login = True
        self.server.set(key, password)

    def signup(self, name, password):

        key = self._get_cred_key(name)

        if self.server.exists(key):
            print("Користувач з таким логіном уже існує")
            return

        self.server.set(key, password)
        print("Користувача зареєстровано")

# ■ додати експонат;
    def add_exponat_info(self, exp_name, description):
        if not self.is_login:
            return

        key = self._get_exp_key(exp_name)

        if self.server.exists(key):
            print("exponat already exists")
            return

        self.server.set(key, description)
        print("exponat added")
# ■ видалити експонат;

# ■ редагування інформації про експонат;

# ■ перегляд повної інформації про експонат;

# ■ виведення інформації про всі експонати;

# ■ перегляд інформації про людей, які мають відношення
# до певного експонату;
# ■ перегляд інформації про експонати, що мають відношення
# до певної людини;
# ■ перегляд набору експонатів на основі певного критерію.
# Наприклад, показати всі книжкові експонати.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи.

app = MuseumApp()
