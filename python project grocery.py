class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store product:quantity

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.stock -= quantity
            print(f"Added {quantity} {product.name}(s) to cart")
        else:
            print(f"Not enough stock! Only {product.stock} available")

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] <= quantity:
                del self.items[product]
            else:
                self.items[product] -= quantity
            product.stock += quantity
            print(f"Removed {quantity} {product.name}(s) from cart")
        else:
            print("Item not in cart")

    def get_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display(self):
        if not self.items:
            print("Cart is empty")
            return
        print("\nShopping Cart:")
        for product, quantity in self.items.items():
            print(f"{product.name}: {quantity} x ${product.price:.2f} = ${(product.price * quantity):.2f}")
        print(f"Total: ${self.get_total():.2f}")


class GroceryStore:
    def __init__(self):
        self.inventory = []
        self.cart = ShoppingCart()
        self.setup_initial_inventory()

    def setup_initial_inventory(self):
        # Sample products
        self.inventory.extend([
            Product("Apple", 0.50, 100),
            Product("Bread", 2.99, 50),
            Product("Milk", 3.49, 30),
            Product("Eggs", 4.99, 20),
            Product("Cheese", 6.99, 15)
        ])

    def display_inventory(self):
        print("\nAvailable Products:")
        for i, product in enumerate(self.inventory, 1):
            print(f"{i}. {product}")

    def run(self):
        while True:
            print("\n=== Grocery Store Application ===")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.display_inventory()

            elif choice == "2":
                self.display_inventory()
                try:
                    item_num = int(input("Enter product number: ")) - 1
                    if 0 <= item_num < len(self.inventory):
                        quantity = int(input("Enter quantity: "))
                        self.cart.add_item(self.inventory[item_num], quantity)
                    else:
                        print("Invalid product number")
                except ValueError:
                    print("Please enter valid numbers")

            elif choice == "3":
                self.cart.display()
                if self.cart.items:
                    try:
                        item_num = int(input("Enter product number from inventory to remove: ")) - 1
                        if 0 <= item_num < len(self.inventory):
                            quantity = int(input("Enter quantity to remove: "))
                            self.cart.remove_item(self.inventory[item_num], quantity)
                        else:
                            print("Invalid product number")
                    except ValueError:
                        print("Please enter valid numbers")

            elif choice == "4":
                self.cart.display()

            elif choice == "5":
                self.cart.display()
                if self.cart.items:
                    print(f"Checkout Total: ${self.cart.get_total():.2f}")
                    confirm = input("Confirm purchase? (y/n): ").lower()
                    if confirm == 'y':
                        print("Thank you for your purchase!")
                        self.cart = ShoppingCart()  # Reset cart
                    else:
                        print("Checkout cancelled")
                else:
                    print("Nothing to checkout")

            elif choice == "6":
                print("Thank you for shopping with us!")
                break

            else:
                print("Invalid choice. Please try again")


# Run the application
if __name__ == "__main__":
    store = GroceryStore()
    store.run()