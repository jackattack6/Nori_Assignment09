class Dog
    def __init__(self, color, size)
        self.color = color
        self.size = size
 
    def getColor(self):
        return self.color
    
    def getSize(self):
        return self.size
    
    def setColor(self, color):
        self. color = color
        
    def __str__(self):
        return f"{self.color} Dog that  is {self.size} size"
    
    def __repr__(self):
        return f"Dog(\{self.color}\", \"{self.size}\")" 