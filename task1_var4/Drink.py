from MenuPosition import MenuPosition

class Drink(MenuPosition):
    def __init__(self, menu_position:str):
        super().__init__(menu_position)
        self.volume:int = self.menu_position.pop(0)
        del self.menu_position

    def __str__(self):
        return f"Категория: Напитки, " + super().__str__() + f',  Объём: {self.volume} мл'
