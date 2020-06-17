class Shirt:
  def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
    self.color = shirt_color
    self.size = shirt_size
    self.style = shirt_style
    self.price = shirt_price
  
  def change_price(self, new_price):
    self.price = new_price

  def discount(self, discount):
    return self.price * (1 - discount)


new_shirt = Shirt('red', 'S', 'short sleeve', 15)
print(new_shirt) # <__main__.Shirt object at 0x03BDF870>

print(new_shirt.color)  # red
print(new_shirt.size)   # S
print(new_shirt.style)  # short sleeve
print(new_shirt.price)  # 15

new_shirt.change_price(12)
print(new_shirt.price)  # 12

print(new_shirt.discount(0.2)) # 9.6