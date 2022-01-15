init python:

 class PLACE(object):
  def __init__(self, Name, niceName, Opening, Closing, Parent, mapIcon, Locked):
   self.Name = Name
   self.niceName = niceName
   self.Opening = Opening
   self.Closing = Closing
   self.Parent = Parent
   self.mapIcon = mapIcon
   self.Locked = Locked

  @property
  def isOpen(self):
   global timeOfDay
   if timeOfDay >= self.Opening and timeOfDay < self.Closing:
    return True
   return False
