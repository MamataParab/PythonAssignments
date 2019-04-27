def AddFactor(No):
    Sum=0;
    for i in range(1,No):
        if((No%i)==0):
            Sum=Sum+i;
    return Sum;
    

print("Enter number");
x=int(input());

Result=AddFactor(x);
print("Addition of factor is",Result);
