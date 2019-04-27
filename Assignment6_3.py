###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Object Oriented Programming        
# 
###############################################################################

class Arithmatic:

    def __init__(self):
        self.Value1=0;
        self.Value2=0;
        self.Result=0;

    def Accept(self):      # This method accepts two values from user
        print("Enter first value");
        self.Value1=int(input());

        print("Enter second value");
        self.Value2=int(input());

    def Addition(self):     # This method add two number
        self.Result=self.Value1+self.Value2;
        return self.Result;

    def Subtraction(self):    # This method subtract two number
        self.Result=self.Value1-self.Value2;
        return self.Result;

    def Multiplication(self):   # This method multiply two number
        self.Result=self.Value1*self.Value2;
        return self.Result;

    def Division(self):      # This method divide two number
        self.Result=self.Value1/self.Value2;
        return self.Result;

obj1=Arithmatic();  # First object creation

obj1.Accept();    
Ret=obj1.Addition();
print("Addition of two number is ",Ret);

Ret=obj1.Subtraction();
print("Subtraction of two number is ",Ret);

Ret=obj1.Multiplication();
print("Multiplication of two number is ",Ret);

Ret=obj1.Division();
print("Division of two number is ",Ret);    
    

obj2=Arithmatic();  # Second object creation

obj2.Accept();    
Ret=obj2.Addition();
print("Addition of two number is ",Ret);

Ret=obj2.Subtraction();
print("Subtraction of two number is ",Ret);

Ret=obj2.Multiplication();
print("Multiplication of two number is ",Ret);

Ret=obj2.Division();
print("Division of two number is ",Ret);    
    






