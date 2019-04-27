###############################################################
#
# Author:  Mamata Anil Parab                           
# Project: Class design and demonstration of OOP class
#
#
###############################################################

class Demo:
    Value=0;

    def __init__(self,No1,No2):
        self.i=No1;
        self.j=No2;

    def Fun(self):
        print("Inside Fun()");
        print(self.i);
        print(self.j);

    def Gun(self):
        print("Inside Gun()");
        print(self.i);
        print(self.j);
        


Value1=0;
Value2=0;
print("Enter two numbers");  #Accepting input from user for first object
Value1=int(input());
Value2=int(input());

dobj1=Demo(Value1,Value2); #First object
dobj1.Fun();               #Behaviour call from first object
dobj1.Gun();               #Behaviour call from first object


print("Enter two numbers");  #Accepting input from user for first object
Value1=int(input());
Value2=int(input());

dobj2=Demo(Value1,Value2); #First object
dobj2.Fun();               #Behaviour call from first object
dobj2.Gun();               #Behaviour call from first object

Demo.Value=100
print(Demo.Value);


    
          
        
