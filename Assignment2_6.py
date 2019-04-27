def Pattern2(No):
    for i in range(0,No):
        for j in range(0,No):
            if(i<=j):
                print("*",end=" ");
        print("\n");

print("Enter Number");
x=int(input());

Pattern2(x);        
