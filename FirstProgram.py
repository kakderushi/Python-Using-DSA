class Test:
    def f1(self):
        pass
    @staticmethod
    def f2():
        pass
    @classmethod
    def f3(cls):
        pass
        
    
    # __init__ is act as constrcutor in python
    def __init__(self):
      self.a=5
      self.b=4
  

      
    
t1=Test()
t2=Test()
print(t1.a,t1.b)
