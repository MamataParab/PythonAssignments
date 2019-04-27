########################################################
#
# Author:  Mamata Anil Parab                           
# Project: Finding maximum of elements of list         
# Input:   70,30,80,90,50                                  
# Output:  90
#
########################################################

def Maximum(arr):

    i=0;
    iMax=arr[i]; # Assigning first element of list as maximum element

    for i in arr:
        if(i>iMax):  # Comparing each element of list with iMax
            iMax=i;
    return iMax;      # Returning maximum element

arr=list();

print("Enter count of elements in list"); 
Value=int(input());   # Accepting count of list

print("Enter actual elements of list");
for i in range(0,Value):
    No=input("");    # Accepting actual element of list
    arr.append(int(No));  # Inserting elements in list

Ret=Maximum(arr);      #Method call
print("Maximum element of list is {}".format(Ret));
