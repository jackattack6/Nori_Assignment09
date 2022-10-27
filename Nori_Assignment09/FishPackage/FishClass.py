'''
Created on Oct 25, 2022

FishClass

Name: Nori
email: 
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: collaborate with peers to develop an Eclipse project 
modeling something in the real world. 
Citations:

@author: jundi
'''
class Fish():
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
    def getColor(self):
        print(self.color)
    
    def getSize(self):
        print(self.size)
    
    def setColor(self, color):
        self.color = color
        
    def __str__(self):
        return f"{self.color} fish that is {self.size} size"

    def __repr__(self):
        return f"Fish(\"{self.color}\", \"{self.size}\")"
    
    def swim(self):
        print(f"the {self.color} fish of size {self.size} swam a little")
