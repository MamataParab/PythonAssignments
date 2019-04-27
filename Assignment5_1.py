###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: String reverse       
# Input :  Python Programming
# Output:  gnimmargorP nohtyP 
#
###############################################################################

def StringReverse(str):
    Result=str[::-1];
    return Result;

print("Enter a string");
String=input();
Ret=StringReverse(String);
print("String reverse is ",Ret);
