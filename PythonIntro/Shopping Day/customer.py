from itertools import product
from shoppingcart import ShoppingCart

class Customer:
    def __init__(self,name):
        self.name = name
        self.shoppingcart = ShoppingCart

    def add_product_to_cart(self):
        self.shoppingcart.add_new_product(product)