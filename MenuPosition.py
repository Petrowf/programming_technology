from datetime import time

class MenuPosition:

    def __init__(self, menu_position:str):
        _, self.name, menu_position = menu_position.split("\"")
        self.menu_position = menu_position.split()
        self.cost: float = float(self.menu_position.pop(0))
        time_= self.menu_position.pop(0)
        hours, minutes = time_.split(':')
        hours = int(hours)
        minutes = int(minutes)
        self.time_to_complete:time = time(hours, minutes)

    def __str__(self):
        return f"Название: {self.name}, Цена: {self.cost}, Время приготовления: {self.time_to_complete.hour}:{self.time_to_complete.minute}"
