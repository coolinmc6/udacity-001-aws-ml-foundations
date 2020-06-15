import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = np.array(gift_costs).astype(int)  # convert string to int

# Original Slow Version: 5+ seconds
start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

# Can I get this under 0.5 seconds

# Fast Version
start = time.time()

total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
print(total_price)

print('Duration: {} seconds'.format(time.time() - start))

"""
Using numpy makes it very easy to select all the elements in an array that meet 
a certain condition, and then perform operations on them together all at once. 
You can them find the sum of what those values end up being.
"""