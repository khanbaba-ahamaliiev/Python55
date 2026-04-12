class Recipe:
    def __init__(self,name: str, ingredients: list, text:str, time:int):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self) -> str:
        return f"Страва: {self._name}"

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        return self._time > other._time

    def display_info(self):
        print(f"{self._name}")

        for ingredient in self._ingredients:
            print(ingredient)

        print(f"{self._text}")

        print(f"{self._time}")

dish1 = Recipe("Піца",
 ["борошно", "вода", "дріжджі", "томат", "сир"],
 "Готуємо тісто, додаємо інгредієнти та запікаємо",
 30)

dish2 = Recipe("Салат",
 ["томат", "огірок", "зелень", "олія"],
 "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10)

dish3 = Recipe("Суп",
 ["вода", "картопля", "морква", "м'ясо"],
 "Варимо всі інгредієнти до готовності",
 45)

dishes = [dish1, dish2, dish3]

for dish in dishes:
    if dish.__contains__('томат'):
        print(dish)

min_recipe = dishes[0]

for dish in dishes:
    if min_recipe > dish:
        min_recipe = dish
min_recipe.display_info()
