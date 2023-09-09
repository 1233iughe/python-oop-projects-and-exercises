class BouncyBall:
     
    def __init__(self, price, size, brand):
    	self._price = price 
    	self._size = size  
    	self._brand = brand
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(self._price, int):
            self._price = value
        else:
            print("Price must be an integer")

    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, value):
        if isinstance(self._size, int):
            self._size = value
        else:
            print("Size must be an integer")
    
    @property
    def brand(self):
        return self._brand
        
    @brand.setter
    def brand(self, value):
        if isinstance(self._brand, str):
            self._brand = value
        else:
            print("Brand must be a string")
    
class BouncyBall:
     
    def __init__(self, price, size, brand):
    	self._price = price 
    	self._size = size  
    	self._brand = brand
    
    
    def get_price(self):
        return self._price

    
    def set_price(self, value):
        if isinstance(self._price, int):
            self._price = value
        else:
            print("Price must be an integer")

    def get_size(self):
        return self._size
        
    
    def set_size(self, value):
        if isinstance(self._size, int):
            self._size = value
        else:
            print("Size must be an integer")
    
    
    def get_brand(self):
        return self._brand
        
    
    def set_brand(self, value):
        if isinstance(self._brand, str):
            self._brand = value
        else:
            print("Brand must be a string")
    
    price = property(set_price, get_price)
    size = property(set_size, get_size)
    brand = property(set_brand, get_brand)