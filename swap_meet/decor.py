from swap_meet.item import Item

class Decor(Item):
    def __init__(self):
        super().__init__(category = "Decor")
    def __str__(self):
        return "Something to decorate your space."