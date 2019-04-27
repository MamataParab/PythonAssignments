###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Object Oriented Programming
#
###############################################################################
class BookStore:
    NoOfBooks=0;

    def __init__(self,Name,Author):
        self.Name=Name;
        self.Author=Author;
        self.NoOfBooks=self.NoOfBooks+1;


    def Display(self):
        print("Name of book is ",self.Name);
        print("Name of author is ",self.Author);
        print("Count of book is ",self.NoOfBooks);

Obj1=BookStore("Linux programming","Robert Love");
Obj1.Display();

Obj2=BookStore("C Programming","Dennis Ritchie");
Obj2.Display();


        
        
