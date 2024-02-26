import math

class Triangle:
    
    # Class specific methods
    
    def __init__(self, a, b, c):
        self._a = int(a)
        self._b = int(b)
        self._c = int(c)
        
        self._check_triangle_properties()
        
        
    def __repr__(self):
        print(
            f"""
                Triangle
                A - {self.a}, B - {self.b}, C - {self.c}
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
    
    # Methods
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        a, b, c = [self.a, self.b, self.c]
        
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    def _check_triangle_properties(self):
        a, b, c = [self.a, self.b, self.c]
        
        is_triangle_valid = True
        
        if a > b + c or b > a + c or c > a + b:
            is_triangle_valid = False
        
        # set all sides as zero if conditions are not met
        if not is_triangle_valid:
            self.a, self.b, self.c = 0, 0, 0