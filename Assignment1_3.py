#3) Addition of two numbers ########################################

def Addition(No1,No2):
    Ans= No1+No2;
    return Ans;


print("Enter two numbers");

x=int(input());
y=int(input());

Result=Addition(x,y); #function call
print(Result);
