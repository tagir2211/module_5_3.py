class House:
  def __init__(self, name, number_of_floors):
    self.name = name
    self.number_of_floors = number_of_floors
    if  not(isinstance(self.number_of_floors, int)):
        print(f'Количество этажей в доме: "{self.name}" указана не корректно.')

  def go_to(self, new_floor):
    if new_floor < 1 or new_floor > self.number_of_floors:
      print(f'В доме "{self.name}" нет этажа {new_floor}')
    else:
      for i in range(0, new_floor):
          print(i+1)
  def __len__(self):
    return self.number_of_floors

  def __eq__(self, other):
      if isinstance(other, House):
        if isinstance(other.number_of_floors, int):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        else:
            return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __ne__(self, other):
      if isinstance(other, House):
          if isinstance(other.number_of_floors, int):
              if self.number_of_floors != other.number_of_floors:
                  return True
              else:
                  return False
          else:
              return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __ge__(self, other):
      if isinstance(other, House):
          if isinstance(other.number_of_floors, int):
              if self.number_of_floors >= other.number_of_floors:
                  return True
              else:
                  return False
          else:
              return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __gt__(self, other):
      if isinstance(other, House):
          if isinstance(other.number_of_floors, int):
              if self.number_of_floors > other.number_of_floors:
                  return True
              else:
                  return False
          else:
              return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __le__(self, other):
      if isinstance(other, House):
          if isinstance(other.number_of_floors, int):
              if self.number_of_floors <= other.number_of_floors:
                  return True
              else:
                  return False
          else:
              return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __lt__(self, other):
      if isinstance(other, House):
          if isinstance(other.number_of_floors, int):
              if self.number_of_floors < other.number_of_floors:
                  return True
              else:
                  return False
          else:
              return f'Количество этажей в доме: "{other.name}" указана не корректно.'
      else:
          return f'Объект "{other}" не является обеъктом типа {type(self)}'

  def __add__(self, value):
    if isinstance(value, int):
        self.number_of_floors = self.number_of_floors + value
        return self
    else:
        return f'{value} - не является числом'

  def __iadd__(self, value):
    return self.__add__(value)
  def __radd__(self, value):
    return self.__add__(value)

  def __str__(self):
    return f'Название: "{self.name}", количество этажей:  {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)


print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__