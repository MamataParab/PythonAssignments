###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Permutation of string      
# Input :  XYZ      
# Output:  XYZ XZY YXZ YXZ ZXY ZYX  
#
###############################################################################

from itertools import permutations

def Permutation(String):
    arr=permutations(String);

    for i in list(arr):
        print(''.join(i));

print("Enter string");
Str=input();

Permutation(Str);

    
