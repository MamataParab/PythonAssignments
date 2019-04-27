###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Object Oriented Programming        
# 
###############################################################################

class Circle:
    Pi=3.14;

    def __init__(self):
        self.Radius=0.0;
        self.Area=0.0;
        self.Circumference=0.0;

    def Accept(self):
        print("Enter the value of radius");
        self.Radius=int(input());
        print("Entered value of radius is",self.Radius);

    def CalculateArea(self):
        self.Area=self.Pi*self.Radius*self.Radius;

    def CalculateCircum(self):
        self.Circumference=2*self.Pi*self.Radius;
        

    def Display(self):
        print("Area of circle is ",self.Area);
        print("Circumference of circle is ",self.Circumference);

obj1=Circle();
obj1.Accept();
obj1.CalculateArea();
obj1.CalculateCircum();
obj1.Display();

        
