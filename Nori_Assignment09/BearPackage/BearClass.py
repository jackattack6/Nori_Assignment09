'''
BearClass
'''

class Bear():
    
    def __init__(self, color, weight): 
        self.color = color
        self.weight = weight
        
    def validateWeight(self, weight):
        # Validates the size of the shoe
        if weight < 0:
            print("Weight of bear must be a positive number")
        
        else:
            self.weight = weight
    def __repr__(self):
        # Returns a string representation of the object
        return "Color = " + self.color
    
    def __str__ (self):
        # Returns a nicer looking string representation of the object
        return "color = " + self.color + ", " + str(self.color)
            
    def setWeight(self, weight):
        # Sets the weight after it is validated
        self.validateWeight(weight)
        
    def printColor(self):
        # Prints out the color of the shoe
        print(self.color);
        
    def printWeight(self):
        # Prints out the weight of the shoe
        print(self.weight);
        
    def firstLetter(self):
        # Prints out the first letter of the color of the shoe
        print(self.color[0])

if __name__ == "__main__": 
   '''
    myBear = Bear("White", 400) 
    
    myBear.printWeight()    
    myBear.firstLetter()
    print(myBear.__str__())
    print(myBear.__repr__())
    '''