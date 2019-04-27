###################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Multithreading to display 1 to 50 in forward and in reverse direction
#          with synchronization
# Input:   50                                
# Output:  1,2,3,4,.........50 and 50,49,48,47.............
#
###################################################################################

import threading
from threading import Lock;
lock=Lock();

def Forward(iNo):
    lock.acquire()
    for i in range(1,iNo+1):
        print(i);
    lock.release();
        
def Reverse(iNo):
    lock.acquire()
    for i in range(iNo,0,-1):
        print(i);
    lock.release()



if __name__=="__main__":

    iNo=50

    Thread1=threading.Thread(target=Forward,args=(iNo,));
    Thread2=threading.Thread(target=Reverse,args=(iNo,));

    Thread1.start();
    Thread2.start();

    Thread1.join();
    Thread2.join();
    
