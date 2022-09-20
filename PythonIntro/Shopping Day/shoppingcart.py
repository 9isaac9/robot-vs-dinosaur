class ShoppingCart:

    def __init__(self):
        self.name = "shopping cart"
        self.products = []

    def add_new_product(self,product):
        self.products.append(product)
        print(f" {product.name} was added to cart")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
