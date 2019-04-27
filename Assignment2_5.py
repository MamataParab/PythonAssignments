def ChkPrime(No):
    iCnt=0;
    for i in range(1,No+1):
        if((No%i)==0):
            iCnt=iCnt+1;


    if(iCnt==2):
        return True;
    else:
        return False;

print("Enter Number");
x=int(input());

Ret=ChkPrime(x);
if(Ret==True):
    print("Given number is Prime");

else:
    print("Given number is not prime");

    
    
    
