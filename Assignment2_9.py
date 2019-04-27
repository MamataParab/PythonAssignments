def CountDigit(No):
    iCnt=0;
    
    while(No!=0):
        No=No//10;
        iCnt=iCnt+1;
    return iCnt;

print("Enter Number");
x=int(input());

Result=CountDigit(x);
print("Count of didgit is",Result);

        
