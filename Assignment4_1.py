########################################################
#
# Author:  Mamata Anil Parab                           
# Project: Lambda function to display square         
# Input:   4                                  
# Output:  16
#
########################################################

# Normal Function

#def Power(iNo):
#   iPower=0;
#   iPower=iNo*iNo;
#   return iPower;


#print("Enter the number ");
#x= int(input());

#Ret=Power(x);
#print("The power of given number is {}".format(Ret));

#Lambda Function

Value=lambda iNo:iNo*iNo;  #lambda function


print("Enter the number "); 
x= int(input());   #Accepting input user

Ret= Value(x);  # Storing return value of lambda function into Ret
print("The square of given number is {}".format(Ret));  # Displaying output

