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
from Bearpackage.BearClass import Bear
if __name__ == "__main__":

    myBear = Bear("white", 400)
    
    print(myBear.__str__())
    
    
from FishPackage.FishClass import Fish

if __name__ == "__main__":

    myFish = Fish("Orange", 5)
    
    print(myFish.__str__())
    
    
from DogPackage.DogClass import Dog

if __name__ == "__main__":

    myDog = Dog("purple",80)
    
    print (myDog.__str__())

