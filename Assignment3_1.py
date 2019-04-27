
########################################################
#
# Author:  Mamata Anil Parab                           
# Project: Addition of elements of list         
# Input:   10,20,30,40,50                                  
# Output:  150
#
########################################################
    
def AddElement(arr):
    iSum=0;

    for i in arr:
        iSum=iSum+i;
    return iSum;

arr=list();
print("Enter number of elements of list");
Value=int(input()); # Accepting element count

print("Enter elements of list");
for i in range(0,Value):
    no=input("");   # Accepting actual elements
    arr.append(int(no));  # Inserting enterd values in list 
    
print("Elements that you enterd are");
for i in arr:
    print(i);
    
Ret=AddElement(arr); # Method call
print("Addition of elements of list is {}".format(Ret)); # Printing result
