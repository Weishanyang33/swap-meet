class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"   
    
    def condition_description(self):
        if self.condition == 0:
            return "Take it home for free!"
        elif self.condition == 1:
            return "Bearable"
        elif self.condition == 2:
            return "Usable"
        elif self.condition == 3:
            return "Normal wear"
        elif self.condition == 4:
            return "Like new"
        elif self.condition == 5:
            return "Brand-New"
