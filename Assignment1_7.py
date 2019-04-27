#7)Divisible by 5 ######################################

def DivBy5(No):
    if((No%5)==0):
        return True;
    else:
        return False;

print("Enter number");
x=int(input());

Result=DivBy5(x); #function call
print(Result);
