#Car.py
class Car:
    def __init__(self,make,model,year,price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
        
    def __gt__(self,rhs):
        if self.make == rhs.make and self.model == rhs.model and self.year == rhs.year:
            return self.price > rhs.price
        elif self.make == rhs.make and self.model == rhs.model:
            return self.year > rhs.year
        
        elif self.make == rhs.make:
            return self.model > rhs.model
        
        else:
            return self.make > rhs.make
        
    def __lt__(self,rhs):
        if self.make == rhs.make and self.model == rhs.model and self.year == rhs.year:
            return self.price < rhs.price
        elif self.make == rhs.make and self.model == rhs.model:
            return self.year < rhs.year
        
        elif self.make == rhs.make:
            return self.model < rhs.model
        
        else:
            return self.make < rhs.make
        
    def __eq__(self,rhs):
        if self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price == rhs.price:
            return True
        else:
            return False
        
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make,self.model,self.year,self.price)
        
        
    
