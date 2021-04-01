from item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
          return False
    def get_by_category(self, category):
      category_wanted = []
      for item in self.inventory:
          if item.category == category:
              category_wanted.append(item)
      return category_wanted
    
