###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Object Oriented Programming        
# 
###############################################################################

class Numbers:

    def __init__(self,Value):
        self.Value=Value;

    def Factor(self):
        arr=list();
        i=0;
        for i in range(0,int(self.Value/2+1)):
            if((self.Value%(i+1))==0):
                arr.append(int(i+1));
        print(arr);

    def SumFactor(self):
        Sum=0;
        i=0;
        arr=list();
        for i in range(0,int(self.Value/2+1)):
            if((self.Value%(i+1))==0):
                arr.append(int(i+1));
                
        for i in arr:
            Sum=Sum+i;
        return Sum;

    def ChkPerfect(self):
        Sum=0;
        i=0;
        arr=list();
        for i in range(0,int(self.Value/2+1)):
            if((self.Value%(i+1))==0):
                arr.append(int(i+1));
                
        for i in arr:
            Sum=Sum+i;
        if(Sum==self.Value):
            return True;
        else:
            return False;


    def ChkPrime(self):
        i=0;
        iCount=0;
        
        for i in range(1,self.Value):
            if((self.Value%i)==0):
                iCount=iCount+1;
        if(iCount==2):
            return True;
        else:
            return False;
        

            
                


Obj=Numbers(6);
Obj.Factor();
Ret=Obj.SumFactor();
print("Sum of factor is ",Ret);

Ret=Obj.ChkPerfect();
if(Ret==True):
    print("The given number is perfect number");
else:
    print("The given number is not perfect number");
    
Ret=Obj.ChkPrime();
if(Ret==True):
    print("The given number is prime number");
else:
    print("The given number is not prime number");
    
    



































                
            
