def AddDigit(No):
    digit=0;
    Sum=0;

    while(No!=0):
        digit=No%10;
        Sum=Sum+digit;
        No=No//10;
    return Sum;

print("Enter number");
x=int(input());

Result=AddDigit(x);
print("Addition of didgit is",Result);

