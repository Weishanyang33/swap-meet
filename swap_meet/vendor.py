from swap_meet.item import Item

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
    def swap_items(self, their_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in their_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            their_vendor.inventory.remove(their_item)
            their_vendor.inventory.append(my_item)
            return True 
