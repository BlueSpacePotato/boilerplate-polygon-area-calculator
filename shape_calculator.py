class Rectangle:
  
  name = 'Rectangle'

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'

    cube = ''
    for h in range(self.height):
      cube += '*'*self.width + '\n'
    return cube
    
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return f'{self.name}(width={self.width}, height={self.height})'

class Square(Rectangle):

  name = 'Square'

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side
    
  def __str__(self):
    return f'{self.name}(side={self.width})'