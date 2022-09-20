from shopping_cart import Shopping_Cart


class Customer:

    def __init__(self,name_passed):
        self.name = name_passed 
        self.cart = Shopping_Cart

    def add_new_prod(self,product):
        self.add_new_prod = (product)
        print(f" {self.name} added {product.name}to their  cart! ")
        
    def view_all_product(self):
        for product in self.cart.products:
            print(product.name)
    
