def nearest_square(num):
  root = 0
  while (root + 1) ** 2 <= num:
    root += 1
  return root ** 2