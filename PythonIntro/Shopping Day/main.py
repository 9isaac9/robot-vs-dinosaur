from product import Product
from customer import Customer


customer_one = Customer("James")
product_one = Product("Banana", 1.5,"produce")
product_two = Product("Donut",2,"Bakery")
product_three =Product("Cheese",3,"Dairy")

customer_one.add_product_to_cart(product_one)
customer_one.add_product_to_cart(product_two)
customer_one.add_product_to_cart(product_three)

shopping_cart_total_price = customer_one.shoppingcart.calculate_total()
print(shopping_cart_total_price)