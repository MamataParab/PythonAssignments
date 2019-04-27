def Pattern4(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            if(i>=j):
                print(j,end=" ");
            
        print("\n");

print("Enter Number");
x=int(input());

Pattern4(x);
        
