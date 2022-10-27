'''
Name: Nori
email: 
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description:  collaborate with peers to develop an Eclipse project modeling something in the real world
Citations:
Anything else that's relevant:
'''
from BearPackage.BearClass import Bear
from FishPackage.FishClass import Fish
from DogPackage.DogClass import Dog


myBear = Bear("White", 400)
myBear.getColor() 
print(myBear.__str__())
    
    
myFish = Fish("Orange", 5)
myFish.getColor()
print(myFish.__str__())
    

myDog = Dog("Purple", 80)
myDog.getColor() 
print (myDog.__str__())

