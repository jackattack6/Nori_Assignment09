'''
Name: Jack Hutz
email: hutzjm@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Collaborate with peers to develop an Eclipse project modeling something 
in the real world 
Citations: N/A
Anything else that's relevant: N/A
'''

class Bear():
    
    def __init__(self, color, weight): 
        self.color = color
        self.weight = weight
    
    def setWeight(self, weight):
        self.weight = weight
        
    def getColor(self):
        print(self.color)
        
    def getWeight(self):
        print(self.weight)
        
    def firstLetterOfColor(self):
        print(self.color[0]) 
   
    def __repr__(self):
        return "Color = " + self.color
    
    def __str__ (self):
        return self.color + " bear that is " + str(self.weight) + " pounds"
            
  

if __name__ == "__main__": 
 
    myBear = Bear("White", 400) 
    myBear.setWeight(500)
    myBear.getColor()
    myBear.getWeight()  
    myBear.firstLetterOfColor()
    print(myBear.__str__())
    print(myBear.__repr__())
    