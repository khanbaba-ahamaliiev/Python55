# упаковывание данных

# у json есть ограничения потому что он должен быть совместим с другими языками

# только для python есть pickle
import pickle
import json


data = {
    "name": "John",
    'age':45,
    "items": {1,7,3,4}
}

# кодирование информации

# encoded = json.dumps(data) # json переводит данные в байты
# print(encoded)
# print(type(encoded))

# в pickle можно сохранять любые объекты, а не только те, которые поддерживает json
encoded = pickle.dumps(data)
print(encoded)
print(type(encoded))


# для pickle файлы нужно открывать для записи байтов
with open("data.pkl","wb") as file:
    pickle.dump(data, file)

with open("data.pkl","rb") as file:
    new_data = pickle.load(file)


print(new_data)
print(type(new_data))
print(new_data["name"])


class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def info(self):
        print(self._name)
        print(self._age)

person = Person("Mary",23)

with open("person.pkl","wb") as file:
    pickle.dump(person, file)

with open("person.pkl","rb") as file:
    new_person = pickle.load(file)


new_person.info()
