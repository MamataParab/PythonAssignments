##############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Accepting list from user and displying addition of prime elements         
# Input:   5,6,3,1,9,7,4                                 
# Output:  16
#
#############################################################################
from NumOperation import *
def ListPrime(brr):
	
	addition=0;
	for i in brr:
		bret=ChkPrime(i);
		if(bret==True):
			addition+=i
	return addition;
			
				
	

arr= list();

N=input("Enter Number of elements in the array: ");

print("Enter elements in the array");

for i in range(0,int(N)):
	element=input("");
	arr.append(int(element));
	
ret=ListPrime(arr);
print(ret);
     
    
