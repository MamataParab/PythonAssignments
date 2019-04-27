#6)Display possitive,negative or zero #######################################

def ChkNumber(No):
    if(No>0):
        print("Number is positive");
    elif(No==0):
        print("Number is zero");
    else:
        print("Number is negative");

x=int(input("\nEnter number\n"));

ChkNumber(x); #function call
