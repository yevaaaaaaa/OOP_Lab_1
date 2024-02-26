class Parallelogram:
    
    def __init__(self, a, b, h):
        self._a = int(a)
        self._b = int(b)
        self._h = int(h)
        
    @property
    def a(self): return self._a
    
    @property
    def b(self): return self._b
    
    @property
    def h(self): return self._h
    