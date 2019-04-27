###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: filter, map, reduce to find product of numbers from range 70 to 90        
# Input:   4                                  
# Output:  16
#
###############################################################################
import functools

print("Enter count of elements");
Value=int(input());

arr=list();
print("Enter actual elements");

for i in range(0,Value):
    iNo=input("");
    arr.append(int(iNo));
    

GreaterArr=list(filter(lambda iNo:((iNo>=70) &(iNo<=90)),arr));
print("List after filter ",GreaterArr);

AddArr=list(map(lambda iNo:(iNo+10),GreaterArr));
print("List after adding 10 in every element is",AddArr);

Multi=functools.reduce(lambda x,y:(x*y),AddArr)
print("Multiplication of all elements is ", Multi);


