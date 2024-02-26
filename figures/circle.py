import math

class Circle:
    
    # Class specific methods
    
    def __init__(self, radius):
        self._radius = int(radius)
        
    def __repr__(self):
        print(
            f"""
              Circle
              Radius - {self.radius}
              Perimeter - {self.perimeter()}
              Area = {self.area()}
            """
        )


    # Properties
    
    @property
    def radius(self): return self._radius
    
    
    # Methods
    
    def perimeter(self):
        return math.pi * self.radius * 2
    
    def area(self):
        return math.pi * math.pow(self.radius, 2)