########################################################
#
# Author:  Mamata Anil Parab                           
# Project: Lambda function to display multiplication of two number     
# Input:   4  3                                 
# Output:  12
#
########################################################

#Normal Function

#def Multiplication(iNo1,iNo2):
#    iResult=0;
#    iResult=iNo1*iNo2;
#    return iResult;

#print("Enter first number");
#iValue1=int(input());

#print("Enter second number");
#iValue2=int(input());

#Ret=Multiplication(iValue1,iValue2);
#print("The multiplication of two number is {}".format(Ret));

#Lambda Function

Multi=lambda iNo1,iNo2:iNo1*iNo2;

print("Enter first number");
iValue1=int(input());

print("Enter second number");
iValue2=int(input());

Ret=Multi(iValue1,iValue2);
print("Multiplication of two number is {}".format(Ret));


