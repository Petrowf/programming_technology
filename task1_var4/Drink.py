from MenuPosition import MenuPosition

class Drink(MenuPosition):
    def __init__(self, menu_position:str):
        super().__init__(menu_position)
        volume = menu_position.split()[-1]
        self.volume = int(volume)

    def __str__(self):
        return f"Категория: Напитки, " + super().__str__() + f',  Объём: {self.volume} мл'
