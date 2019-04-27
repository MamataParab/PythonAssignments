###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: filter, map, reduce       
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62 
#
###############################################################################

import functools

#Normal Function

arr=list();
brr=list();
def Prime(iNo):
    iCount=0;
    for i in range(2,iNo):
        if iNo % i == 0:
            return False
    return True
        

def MultBy2(iNo):
        iNo=iNo*2;
        print(iNo);
               

def Maximum(iNo1,iNo2):
    if(iNo1>iNo2):
        return iNo1;
    else:
        return iNo2;

print("Enter count of list");
value=int(input());

print("Enter actual elements");


for i in range(0,value):
    iNo=input("");
    arr.append(int(iNo));

PrimeArr=list(filter(Prime,arr));
print("List after filter is ", arr);

MultiArr=list(map(MultBy2,PrimeArr));
print("List after multiplication by 2 ",MultiArr);

MaxArr=functools.reduce(Maximum,MultiArr);
print(MaxArr);
