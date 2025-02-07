from MenuPosition import MenuPosition

class Food(MenuPosition):
    def __init__(self, menu_position:str):
        super().__init__(menu_position)
        self.mass:int = self.menu_position.pop(0)
        del self.menu_position

    def __str__(self):
        return f"Категория: Еда, " + super().__str__() + f',  Масса: {self.mass} грамм'
