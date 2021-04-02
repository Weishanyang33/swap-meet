from swap_meet.item import Item

class Electronics(Item):
    def __init__(self):
        super().__init__(category = "Electronics")
    def __str__(self):
        return "A gadget full of buttons and secrets."