from products import Product
from store import Store

'''Welcome to the marketplace, where we interact with stores and products!'''


# instantiate stores
grocery = Store("Monty's Grocery")
bakery = Store("Chris' Bakery")

# instantiate products
banana = Product('banana', 0.99, 'fruit')
apple = Product('apple', 0.79, 'fruit')
cheese = Product('cheese', 2.50, 'dairy')
croissant = Product('croissant', 1.00, 'pastry')
baguette = Product('baguette', 1.69, 'bread')
chocolate_cake = Product('chocolate cake', 3.75, 'cake')

# add products to stores
grocery.add_product(banana)
grocery.add_product(apple)
grocery.add_product(cheese)
bakery.add_product(croissant)
bakery.add_product(baguette)
bakery.add_product(chocolate_cake)

# sell products froms stores
grocery.sell_product(0)
bakery.sell_product(1)

# adjust product prices storewide
bakery.inflation(3)
grocery.set_clearance(category='fruit', percent_discount=20)
