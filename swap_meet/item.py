class Item:
  def __init__(self, category="", condition=0):
    self.category = category
    self.condition = condition

  def condition_in_words(self):
    if self.condition < 1:
      return "You probably want a glove for this one..."
    elif self.condition < 2:
      return "Hopefully, its ok if this doesn't last you unto next month"
    elif self.condition < 3:
      return "It may not be pretty but its sturdy!"
    elif self.condition < 4:
      return "Its clearly used...but it could be much worse!"
    elif self.condition < 5:
      return "Almost like its brand new!"
    else:
      return "MINT: Literally hasn't left the box!"

  def __str__(self):
    return "Hello World!"