###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Average of ascii value of characters of string       
# Input :  ABCDE       
# Output:  67   ((65+66+67+68+69)/5)   
#
###############################################################################

arr=list();
def CharAvg(String):
    for i in String:
        arr.append(i);

    iSum=0;
    iAvg=0;

    for i in arr:
        print(ord(i));
        iSum=iSum+ord(i);
        iAvg=iSum/len(String);
    return iAvg;    

print("Enter string");
Str=input();

Ret=CharAvg(Str);
print("Average of ascii value of characters is ",Ret);        

    

        
