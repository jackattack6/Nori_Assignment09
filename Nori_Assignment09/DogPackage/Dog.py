'''
Name: Bill Tummler
email: N/A (Group Project)
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Collaborate with peers to develop an Eclipse project modeling something 
in the real world 
Citations: N/A
Anything else that's relevant: N/A
'''
class Dog():
    def __init__(self, color, size):
        self.color = color
        self.size = size
 
    def getColor(self):
        return self.color
    
    def getSize(self):
        return self.size
    
    def setColor(self, color):
        self. color = color
        
    def __str__(self):
        return f"{self.color} Dog that is {self.size} size"
    
    def __repr__(self):
        return f"Dog(\{self.color}\", \"{self.size}\")" 
    
    def walk(self):
        print (f"the {self.color} dog of size {self.size} walked a litte")