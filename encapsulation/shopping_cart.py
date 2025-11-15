# Implement shopping cart
# Total amount 
# Items
# Discount
# Add item to cart
# Remove item
# Add for later
# View cart contents


class CartItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__quantity = 1
    def total(self):
        return self.__price * self.__quantity
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self.__quantity = value
        else:
            self.__quantity = 0
        
         


class ShoppingCart:
    
    def __init__(self):
        self.__items: dict[str, CartItem] = {}

    def add_item(self, name, price, quantity=1): 
        if name in self.__items:
            existing: CartItem = self.__items[name]
            existing.quantity = existing.quantity + quantity
        else:
            new_item = CartItem(name, price)
            new_item.quantity = quantity
            self.__items[name] = new_item
        
    def remove_item(self, name, quantity=1):
        if name in self.__items:
            existing: CartItem = self.__items[name]
            existing.quantity = existing.quantity - quantity

    def total(self):
        sum = 0
        for _, item in self.__items.items():
            sum += item.total()
        return sum
    
    def __len__(self) -> int:
        total_quantity = 0
        for item in self.__items.values():
            total_quantity += item.quantity
        # sum(item.quanitiy for item in self.__items.values())        
        return total_quantity
    
    def __str__(self):
        return f"Shopping Cart: Total Price {self.total()} Total Items: {len(self)}"

        
shopping_cart = ShoppingCart()

shopping_cart.add_item("Winter tire", 300, 4)


print(shopping_cart)

