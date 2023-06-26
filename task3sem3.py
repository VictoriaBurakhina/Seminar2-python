#3 Задача. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

myThings = {'еда':3, "котелок":1, "вода":2,"палатка":3, "посуда":3,"одежда":2,"фонарик":1,"аптечка":2}
maxWeight = 10
bag = {}
for key,value in myThings.items():
    if maxWeight-value >= 0:
        bag[key] = value
        maxWeight = maxWeight-value
print(bag)