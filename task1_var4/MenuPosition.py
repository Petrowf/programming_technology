from datetime import time

class MenuPosition:

    def __init__(self, menu_position:str):
        _, name, menu_position = menu_position.split("\"")
        menu_position = menu_position.split()
        cost, time_= menu_position[0:2]
        cost = float(cost)
        hours, minutes = time_.split(':')
        hours = int(hours)
        minutes = int(minutes)
        self.name: str = name
        self.cost : float = cost
        self.time_to_complete : time = time(hours, minutes)

    def __str__(self):
        return f"Название: {self.name}, Цена: {self.cost}, Время приготовления: {self.time_to_complete.hour}:{self.time_to_complete.minute}"
