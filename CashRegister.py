class CashRegister:


    def __init__(self, cashier='Jhon Doe', purchase = []):
        self._purchase = purchase
        self.__cashier = cashier
        self._subtotal = 0

    
    def add_product(self, product, quantity=1):
        if quantity > 0:
            for i in range(quantity):
                self._purchase.append(product)
                self.update_subtotal(product, True)
        else:
            print('Quantity should be greater than 0')
    
    def get_products(self):
        return self._purchase 

    def remove_product(self, product):
        if product in self.get_products(): 
            self._purchase.remove(product)
            self.update_subtotal(product, False)
        else:
            print("Product not in list")

    def update_price(self, product_name, new_price):
        for item in self._purchase:
            if item['name'] == product_name:
                self.update_subtotal(item, False)
                item['price'] = new_price
                self.update_subtotal(item, True)


    def update_subtotal(self, product, adding_product=True):
        if adding_product:
            self._subtotal += product['price']
        else:
            self._subtotal -= product['price']

    def get_subtotal(self):
        return self._subtotal
    
    def get_taxes(self):
        return round(self.get_subtotal()*0.05, 2)

    def get_total(self):
        return round(self.get_subtotal()*1.05, 2)

    def clear_register(self):
        self._purchase = []
        self._subtotal = 0

myRegister = CashRegister()
print(myRegister.get_products(), myRegister.get_subtotal(), myRegister.get_taxes(), myRegister.get_total())
myRegister.add_product({"name": "Pizza", "price": 10.34})
myRegister.add_product({"name": "Panini", "price": 20.00})
myRegister.add_product({"name": "Panini", "price": 20.00})
print(myRegister.get_products(), myRegister.get_subtotal(), myRegister.get_taxes(), myRegister.get_total())
myRegister.remove_product({"name": "Panini", "price": 20.00})
myRegister.update_price('Pizza', 15.00)
print(myRegister.get_products(), myRegister.get_subtotal(), myRegister.get_taxes(), myRegister.get_total())
myRegister.clear_register()
print(myRegister.get_products(), myRegister.get_subtotal(), myRegister.get_taxes(), myRegister.get_total())