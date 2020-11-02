import math
class circle():
    #_init_used to initialize values of class
    def __init__(self,radius):
        self.radius=radius
    #Method c_area to calculate the area of the circle
    def c_area(self):
        return math.pi*(self.radius**2)
    #Method c_perimeter to calculate the perimeter of the circle
    def c_perimeter(self):
        return 2*math.pi*self.radius

#Take the input from the user
r=int(input("Enter radius of circle: "))
#An object for class is created
obj=circle(r)
#Using object,area mehod is called
print("Area of circle:",round(obj.c_area(),2))
#Using object,Perimeter method is called
print("Perimeter of circle:",round(obj.c_perimeter(),2))

