from Food import Food
from Drink import Drink
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem

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

def open_file(window: QMainWindow):
    filename, _ = QFileDialog.getOpenFileName(window.centralwidget, "Открыть файл", "/", "Text Files (*.txt)")
    return filename

def add_objects_to_table(objects_list: list, table_widget: QTableWidget):
    for object_ in objects_list:
        table_widget.insertRow(table_widget.rowCount())
        for i, column in enumerate(object_.to_list()):
            table_widget.setItem(table_widget.rowCount()-1, i, QTableWidgetItem(str(column)))

def get_save_filename(window):
    filename, _ = QFileDialog.getSaveFileName(window, "Save File", "", "All Files(*);;Text Files(*.txt)")
    return filename

# def table_to_list(table: QTableWidget):
#     objects = []
#     for i in range(table.rowCount()):
#         object_ = ''
#         for j in range(table.columnCount()):
#             object_ +=