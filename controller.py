from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view.add_button.clicked.connect(self.add_item)
        self.view.remove_button.clicked.connect(self.remove_item)
        self.update_view()

    def show(self):
        self.view.show()

    def add_item(self):
        item = self.view.item_text.text()
        self.model.add_item(item)
        self.update_view()

    def remove_item(self):
        indexes = [i.row() for i in self.view.items_list.selectedIndexes()]
        for i in indexes:
            self.model.remove_item(i)
        self.update_view()

    def update_view(self):
        items = self.model.get_items()
        self.view.items_list.clear()
        self.view.items_list.addItems(items)
        self.view.item_text.setText("")