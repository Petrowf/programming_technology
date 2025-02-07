"""
В рамках работы студенту необходимо разработать программу,
формирующую программный объект на основании его описания в виде
текстовой строки.
В строке задается тип объекта и его свойства. Свойства могут иметь
различные типы данных (целый, дробный, строковый, дата, время).
Строковые свойства выделяются кавычками. Дата описывается в формате
гггг.мм.дд и записывается без кавычек. Время описывается в формате чч:мм.
Друг от друга свойства отделяются группой из одного или более
пробелов.
Разработанная программа должна корректно обрабатывать различные
варианты корректных входных данных (обработку ошибок можно не
выполнять).

Вариант 4:
Меню: название (строка), цена (дробное), время приготовления
"""
from Food import Food
from Drink import Drink

def parse_objects_from_file_to_list(filename):
    objects_list = []

    with open(filename) as file:
        objects_ = file.readlines()

    for menu_position in objects_:
        object_class = menu_position[0:menu_position.find(' ')]

        if object_class == 'Food':
            objects_list.append(Food(menu_position))
        elif object_class == 'Drink':
            objects_list.append(Drink(menu_position))

    return objects_list

if __name__ == "__main__":
    objects = parse_objects_from_file_to_list('menu')
    for object_ in objects:
        print(str(object_))