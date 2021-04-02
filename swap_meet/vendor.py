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
          
    def swap_first_item(self, their_vendor):
        if len(self.inventory) == 0 or len(their_vendor.inventory) == 0:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = their_vendor.inventory[0]
            self.inventory.append(their_first_item)
            their_vendor.inventory.append(my_first_item)
            self.inventory.remove(my_first_item)
            their_vendor.inventory.remove(their_first_item)
            return True
          
    def get_best_by_category(self, category):
        category_wanted = self.get_by_category(category)
        if not category_wanted:
            return None
        else:
            best_condition = max(item.condition for item in category_wanted)
            for item in category_wanted:
                if item.condition == best_condition:
                    return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)
        
    