####################################################################################
#
# Author: Mamata Anil Parab
# Project: Checking presence of particular string and printing frequency of string
# Input: "Mamata.txt","Marvellous"
# Output: Yes,5
#
####################################################################################

        
import os
import sys

def main():

    try:
        FileName=sys.argv[1]
        String=sys.argv[2]

        fd=open(FileName,"r")
        Data=fd.read()

        arr=Data.split("\n")
        Count=0

        for i in arr:
            print(str(i))
            #if i==String:
            Value=i.split(" ")
            for j in Value:
                if j==String:
                    Count=Count+1
        print(Count)
        
    except Exception as e:
        print(e)
        print("Unable to open file")

    finally:
        fd.close()

if __name__=="__main__":
    main()
