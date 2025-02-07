from MenuPosition import MenuPosition

class Food(MenuPosition):
    def __init__(self, menu_position:str):
        super().__init__(menu_position)
        mass = menu_position.split()[-1]
        self.mass:int = int(mass)

    def __str__(self):
        return f"Категория: Еда, " + super().__str__() + f',  Масса: {self.mass} грамм'
