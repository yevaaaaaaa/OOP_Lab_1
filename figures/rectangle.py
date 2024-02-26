class Rectangle:
    
    # Class specific methods
    
    def __init__(self, a, b):
        self._a = int(a)
        self._b = int(b)
        
    def __repr__(self):
        print(
            f"""
              Rectangle
              A - {self.a}, B - {self.b}
              Perimeter - {self.perimeter()}
              Area = {self.area()}
            """
        )


    # Properties
    
    @property
    def a(self): return self._a
    
    @property
    def b(self): return self._b
    
    
    # Methods
    
    def perimeter(self):
        return self.a * 2 + self.b * 2
    
    def area(self):
        return self.a * self.b