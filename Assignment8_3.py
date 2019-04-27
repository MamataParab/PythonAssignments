###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Multithreading to display addition of even number from list and
#          addition of odd numbers from list       
# Input:   1,2,3,4,5,6,7,8,9,10                                 
# Output:  Addition of Even List=30
#          Addition of Odd List=25
#
###############################################################################

import threading

def EvenList(arr):
    iSum=0;
    for i in arr:
        if i%2==0:
            iSum=iSum+i;
    print("Even list",iSum);
    
def OddList(arr):
    iSum=0;
    for i in arr:
        if i%2!=0:
            iSum=iSum+i;
    print("Odd list",iSum);

if __name__=="__main__":


    print("Entre count of list elements");
    iValue=int(input());

    arr=list();
    iNo=0

    print("Enter actual elements of list");
    for i in range(0,iValue):
        iNo=int(input())
        arr.append(iNo);

    print(arr);

    Thread1=threading.Thread(target=EvenList,args=(arr,));
    Thread2=threading.Thread(target=OddList,args=(arr,));

    Thread1.start();
    Thread2.start();

    Thread1.join();
    Thread2.join();
