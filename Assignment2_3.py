def Factorial(No):
    Ret=1;
    while(No>1):
       Ret=Ret*No;
       No=No-1;
    return Ret;

print("Enter number");
x=int(input());

Result=Factorial(x);
print(Result);
    
