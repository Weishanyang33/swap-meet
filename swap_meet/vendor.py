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
            self.remove(their_vendor.add(my_item))
            their_vendor.remove(self.add(their_item))
            return True 
          
    def swap_first_item(self, their_vendor):
        if not self.inventory or not their_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = their_vendor.inventory[0]
            return self.swap_items(their_vendor, my_first_item, their_first_item)
          
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
        
    