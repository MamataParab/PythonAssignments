###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Multithreading to display Even and Odd numbers        
# Input:   10                                  
# Output:  Even=2,4,6,8,10,12,14,16,18,20
#          Odd= 1,3,5,7,9,11,13,15,17,19
#
###############################################################################

import threading

def DisplayEven(iNo):
    for i in range (1,iNo+1):
        print("Even",i*2);

def DisplayOdd(iNo):
    for i in range(0,iNo):
        print("Odd",i*2+1);

iNo=10

Thread1=threading.Thread(target=DisplayEven,args=(iNo,));
Thread2=threading.Thread(target=DisplayOdd,args=(iNo,));

Thread1.start();
Thread2.start();

Thread1.join();
Thread2.join();
        
