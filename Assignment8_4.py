###################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Multithreading to display small character, capital character and digit       
# Input:   Marvellous InfoSystems@123                                
# Output:  Capital=3, Small=18, digit=3
#
###################################################################################

import threading
import os

def Capital(string):
    iCount=0;
    for i in string:
        if i>='A':
            if i<='Z':
                iCount=iCount+1;
    print(iCount);
                
    print("Process id of capital is ",os.getpid());
                

def Small(string):
    iCount=0;
    for i in string:
        if i>='a':
            if i<='z':
                iCount=iCount+1;
    print(iCount);
                
    print("Process id of small is ",os.getpid());


def Digit(string):
    iCount=0
    for i in string:
        if i>='1':
            if i<='9':
                iCount=iCount+1;
    print(iCount);
                
    print("Process id of digit is ",os.getpid());


string="Marvellous INFOsystems12349"
                

Thread1=threading.Thread(target=Capital,args=(string,));
Thread2=threading.Thread(target=Small,args=(string,));
Thread3=threading.Thread(target=Digit,args=(string,));

Thread1.start();
Thread2.start();
Thread3.start();


Thread1.join();
Thread2.join();
Thread3.join();
