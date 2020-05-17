class Store:
    """A class to represent stores"""
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        # After instantiating a product, add that product to the store
        self.products.append(new_product)
        print(f'Added {new_product.name} to {self.name}.')
        return self

    def sell_product(self, prod_id):
        # sell a product from the store, remove from products list, and print
        sold_product = self.products.pop(prod_id)
        print('\nSold Item(s):')
        sold_product.print_info()
        return self

    def inflation(self, percent_increase):
        # increases the price of each product by the percent_increase given
        # (use the method you wrote in the Product class!)
        print('\nUpdating Prices for Inflation:')
        for product in self.products:
            product.update_price(
                percent_change=percent_increase,
                is_increased=True
                )
        return self

    def set_clearance(self, category, percent_discount):
        # reduce prices within category using Products.update_price()
        print('\nUpdating Sale Item Prices:')
        for product in self.products:
            if product.category == category:
                product.update_price(
                    percent_change=percent_discount,
                    is_increased=False
                )
        return self


###############################

# # instantiate stores
# my_store = Store("Monty's Grocery")
# bakery = Store("Chris' Bakery")

# # instantiate products
# banana = Product('banana', 0.99, 'fruit')
# apple = Product('apple', 0.79, 'fruit')
# croissant = Product('croissant', 1.00, 'pastry')
# baguette = Product('baguette', 1.69, 'bread')

# # add products to stores
# my_store.add_product(banana)
# my_store.add_product(apple)
# bakery.add_product(croissant)
# bakery.add_product(baguette)

# # sell products froms stores
# # my_store.sell_product(id=0)
# # bakery.sell_product(1)

# # adjust product prices storewide
# bakery.inflation(3)
# my_store.set_clearance(category='fruit', percent_discount=20)
