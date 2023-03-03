## this module will contain a circle class with a parameter for radius
## as well as methods for calculating the circumference of a circle
## and a method to print the circumference of a circle
## for our purposes we will utlize following formulas
## circumference = pi * diameter
## diameter = radius * 2
#pi will be coded to 3.14 manually

class Circle:
    def __init__ (self,radius):
        self.radius = radius
    def circumference(self):
        pi = 3.14 #hardcoding pi for our method
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue
    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

## end of code