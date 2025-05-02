from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidget, QTableWidgetItem
from functions import *

def read_file(window):
    filename = open_file(window)
    objects = parse_objects_from_file_to_list(filename)
    add_objects_to_table(objects, window.menu_table)

# def save_file(list_widget: QTableWidget, filename: str):
#
#     with open(filename, mode="w") as file:
#
# def add_item()

