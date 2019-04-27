###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Object Oriented Programming        
# 
###############################################################################

class BankAccount:
    ROI=10.5;

    def __init__(self,Name,Amount):
        self.Name=Name;
        self.Amount=Amount;

    def Display(self):
        print("Name of account holder is ",self.Name);
        print("Amount in account is ",self.Amount);

    def Deposit(self,Amount):
        self.Amount=self.Amount+Amount;
        return self.Amount;

    def Withdraw(self,WithdrawAmt):
        self.Amount=self.Amount-WithdrawAmt;
        return self.Amount;

    def CalculateIntrest(self):
        Intrest=(self.Amount*2*self.ROI)/100;
        return Intrest;

Bobj1=BankAccount("Mamata",1000);
Bobj1.Display();

Ret=Bobj1.Deposit(1000);
print("Amount after depositing money is ",Ret);

Ret=Bobj1.Withdraw(1000);
print("Amount after withdrawing money is ",Ret);

Ret=Bobj1.CalculateIntrest();
print("For ROI=10.5 and duration =2 years,the intrest on amount is ",Ret);
























    
        
        
