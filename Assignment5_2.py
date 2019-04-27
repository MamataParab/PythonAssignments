###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Number of words in string       
# Input :  Python Programming is fun
# Output:  4 
#
###############################################################################

def WordCount(String):
    iCnt=0;
    Result=String.rsplit(" ");

    for i in Result:
        iCnt=iCnt+1;
    return iCnt;    
    

print("Enter a string");
str=input();

Ret=WordCount(str);
print("Count of word in string is ",Ret);
    
