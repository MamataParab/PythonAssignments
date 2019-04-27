###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: filter, map, reduce         
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
#
###############################################################################
import functools

arr=list();
print("Enter count of list");
Value=int(input());

print("Enter actual elements");
for i in range(0,Value):
    iNo=input("");
    arr.append(int(iNo));

EvenArr= list(filter(lambda iNo:(iNo%2==0),arr));
print("List after filtering even number is ",EvenArr);

SquareArr= list(map(lambda iNo:(iNo*iNo),EvenArr));
print("List after mapping is ",SquareArr);

AddArr=functools.reduce(lambda a,b:a+b,SquareArr);
print("List after reduce is ",AddArr);


