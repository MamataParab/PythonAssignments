###############################################################
#
# Author:  Mamata Anil Parab                           
# Project: Finding the frequency of given element from list         
# Input:   10,70,30,10,80,90,50,10  Value=10                                 
# Output:  3
#
###############################################################

def Frequency(arr,Value):
    
    iCount=0;
    for i in arr:
        if(i==Value):
            iCount=iCount+1;
    return iCount;

arr=list();

print("Enter count of elements in list"); 
Value=int(input());   # Accepting count of list

print("Enter actual elements of list");
for i in range(0,Value):
    No=input("");    # Accepting actual element of list
    arr.append(int(No));  # Inserting elements in list

print("Enter the element whose frequency need to be checked");
element=int(input())

Ret=Frequency(arr,element);      #Method call
print("Frequency of given element is {} ".format(Ret));


            

