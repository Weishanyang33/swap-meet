class Item:
  def __init__(self, category="", condition=0):
    self.category = category
    self.condition = condition

  def condition_in_words(self):
    if self.condition < 1:
      "You probably want a glove for this one..."
    elif self.condition < 2:
      "Hopefully, its ok if this doesn't last you unto next month"
    elif self.condition < 3:
      "It may not be pretty but its sturdy!"
    elif self.condition < 4:
      "Its clearly used...but it could be much worse!"
    elif self.condition < 5:
      "Almost like its brand new!"
    else:
      "MINT: Literally hasn't left the box!"

  def __str__(self):
    return "Hello World!"