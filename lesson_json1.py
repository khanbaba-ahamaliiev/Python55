# json
import json

data = {
    'name': 'Антон',
    'age': 23,
    'items':['bread', 'apple', 'milk'],
    'is_good': True,
    'data':None
}


# Сохранение данных в JSON файл

with open("data.json", "w", encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4) # ensure_ascii - дает разрешение использовать другие символы, а не только английские
                                                        # indent - отступы для удобства чтения

# Чтение данных из JSON файла

with open("data.json", "r", encoding='utf-8') as file:
    new_data = json.load(file)

print(type(new_data))
print(new_data)
print(new_data['name'])


# разрешенные типы данных в JSON: dict, list, str, int, float, bool, None

# json переводит данные в байты и потом их в файле сохраняет

# переводит данные в байты

raw_bites = json.dumps(new_data, ensure_ascii=False)
print(type(raw_bites))
print(raw_bites)
print(repr(raw_bites))

new_data = json.loads(raw_bites)
print(type(new_data))
print(new_data)
