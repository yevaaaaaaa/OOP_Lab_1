import math
from figures.triangle import Triangle

class Trapeze:
    
    # Class specific methods
    
    def __init__(self, a, b, c, d):
        self._a = int(a)
        self._b = int(b)
        self._c = int(c)
        self._d = int(d)
        
        self._check_trapeze_properties()
        
        
    def __repr__(self):
        print(
            f"""
              Trapeze
              A - {self.a}, B - {self.b}, C - {self.c}, D - {self.d},
              Perimeter - {self.perimeter()}
              Area = {self.area()}
            """
        )


    # Properties
    
    @property
    def a(self): return self._a
    
    @a.setter
    def a(self, value): 
        self._a = value
        
    @property
    def b(self): return self._b
    
    @b.setter
    def b(self, value):
        self._b = value
    
    @property
    def c(self): return self._c
    
    @c.setter
    def c(self, value):
        self._c = value
    
    @property
    def d(self): return self._d
    
    @d.setter
    def d(self, value):
        self._d = value
    
    
    # Methods
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def area(self):
        
        a, b, c = [self.a, self.b, self.c]
        if a == b: 
            return a * c
        return abs(a + b) * 0.5 * self.height()
        
    def height(self):
        a, b, c, d = [self.a, self.b, self.c, self.d]
        
        if a == b:
            return c
        
        tr = Triangle(c, d, abs(a - b))
        return 2 * tr.area() / abs(a - b)
        
    def _check_trapeze_properties(self):
        
        a, b, c, d = [self.a, self.b, self.c, self.d]
        
        is_trapeze_valid = False
        
        if a == b:
            is_trapeze_valid = c == d  
        else:
            is_trapeze_valid = b - a < d + c  
            
        # set all sides as zero if conditions are not met
        if not is_trapeze_valid:
            self.a, self.b, self.c, self.d = 0, 0, 0, 0