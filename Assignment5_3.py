###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Remove a word from particular position      
# Input :  Python          Position : 3
# Output:  Pyhon 
#
###############################################################################

def RemoveWord(String,iPosition):
    
    Result= String.replace(String[iPosition], "");
    return Result;

print("Enter a string");
str=input();

print("Enter a position");
Value=int(input());


Ret=RemoveWord(str,Value);
print("String is ",Ret);
    
