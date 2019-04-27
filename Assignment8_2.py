###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Multithreading to display addition of even factors and
#          addition of odd factors numbers        
# Input:   100                                 
# Output:  Even factor=2+2=4
#          Odd factor=5+5=10
#
###############################################################################

import threading

def AddEvenFactor(iNo):
    iSum=0;
    for i in range (1,int(iNo)):
        if iNo%i==0:
            if i%2==0:
                iSum=iSum+i;
            #print(i);
    print("EvenFact",iSum);

def AddOddFactor(iNo):
    iSum=0;
    for i in range(1,int(iNo)):
        if iNo%i==0:
            if i%2!=0:
                iSum=iSum+i;
            #print(i);
    print("OddFact",iSum);

if __name__=="__main__":

    print("Enter number");
    iNo=int(input());

    Thread1=threading.Thread(target=AddEvenFactor,args=(iNo,));
    Thread2=threading.Thread(target=AddOddFactor,args=(iNo,));

    Thread1.start();
    Thread2.start();

    Thread1.join();
    Thread2.join();

    print("Exit from main");
    
            
