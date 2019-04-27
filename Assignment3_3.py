########################################################
#
# Author:  Mamata Anil Parab                           
# Project: Finding minimum of element of list         
# Input:   70,30,80,90,50                                  
# Output:  30
#
########################################################

def Minimum(arr):

    i=0;
    iMin=arr[i]; # Assigning first element of list as minimum element

    for i in arr:
        if(i<iMin):  # Comparing each element of list with iMax
            iMin=i;
    return iMin;      # Returning minimum element

arr=list();

print("Enter count of elements in list"); 
Value=int(input());   # Accepting count of list

print("Enter actual elements of list");
for i in range(0,Value):
    No=input("");    # Accepting actual element of list
    arr.append(int(No));  # Inserting elements in list

Ret=Minimum(arr);      #Method call
print("Minimum element of list is {}".format(Ret));
