class Product:
    """A class to represent store products"""
    id_counter = 0

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.id_counter += 1  # increase id 1 for each new product
        self.prod_id = Product.id_counter
        # print(f'Created new product: {self.name}, ID: {self.prod_id}')

    def update_price(self, percent_change, is_increased):
        # Updates the product's price. If is_increased is True, the price
        # should increase by the percent_change provided. If False, the price
        # should decrease by the percent_change provided.
        print(f'{self.name.upper()} \nOld price: ${round(self.price, 2)}')
        if is_increased is True:
            self.price += self.price * (percent_change/100)
        if is_increased is False:
            self.price -= self.price * (percent_change/100)
        print(f'Adjusted price: ${round(self.price, 2)}')
        return self

    def print_info(self):
        # print the name of the product, its category, and its price.
        print(
            f'{self.name.upper()} '
            + f'\nID: {self.prod_id} '
            + f'\nPrice: ${round(self.price, 2)} '
            + f'\nCategory: {self.category}\n'
            )
        return self


##########################

# banana = Product('banana', 0.99, 'fruit')
# banana.print_info()
# banana.update_price(3, True)
# banana.update_price(3, False)

