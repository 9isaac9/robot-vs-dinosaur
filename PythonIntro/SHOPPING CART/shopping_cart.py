class Shopping_Cart:

    def __init__(self):
        self.products = []

    def calculate_cart_total(self):
        final_total = 0
        for product in self.products:
            final_total += product.price

        return final_total   
    

    def add_product_list(self,product):
        self.product.append(product)
        print(f"Your {product.name} was added ")

    def empty_products(self):
        self.products.clear = ()
        print("Your shopping cart is now empty!")



