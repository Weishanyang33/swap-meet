class Vendor:
  def __init__(self, inventory=[]) -> None:
    self.inventory = inventory

  def add(self, item):
    self.inventory.append(item)
    return item

  def remove(self, item):
    matched = False
    for candidate in self.inventory:
      if item == candidate:
        self.inventory.remove(candidate)
        matched = candidate
    return matched

  def get_by_category(self, category):
    return list(filter(lambda item : item.category == category, self.inventory))

  def swap_items(self, other, my_item, their_item):
    try:
      self.inventory.remove(my_item)
      other.inventory.remove(their_item)
    except ValueError:
      return False
    self.inventory.append(their_item)
    other.inventory.append(my_item)
    return True

  def swap_first_item(self, other):
    if len(self.inventory) == 0 or len(other.inventory) == 0:
      return False
    return self.swap_items(other, self.inventory[0], other.inventory[0])

  def get_best_by_category(self, category):
    items_in_category = self.get_by_category(category)
    return max(items_in_category, key = lambda item: item.condition) if len(items_in_category) > 0 else None

  def swap_best_by_category(self, other, my_priority, their_priority):
    my_best = self.get_best_by_category(their_priority)
    their_best = other.get_best_by_category(my_priority)
    return self.swap_items(other, my_best, their_best)

