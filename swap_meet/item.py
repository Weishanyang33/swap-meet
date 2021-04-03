class Item:
    def __init__(self, category="", condition = 0, age = None):
        self.age = age
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"   
    
    def condition_description(self):
        if self.condition < 1:
            return "Take it home for free!"
        elif self.condition < 2:
            return "Bearable"
        elif self.condition < 3:
            return "Usable"
        elif self.condition < 4:
            return "Normal wear"
        else:
            return "Like new"
