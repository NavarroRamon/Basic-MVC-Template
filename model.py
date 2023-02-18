class Model:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        del self.items[index]

    def get_items(self):
        return self.items
