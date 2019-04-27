#############################################################################
#
# Author:   Mamata Anil Parab
# Project:  Display the contents of file on screen
# Input:   "Mamata.txt"
# Output:  Hello World
#
#############################################################################

import os

def main():

    try:
        print("Enter file name")
        FileName=input()
        exists=os.path.isfile(FileName)
        if exists:
            fd=open(FileName,"r")
            Data=fd.read()
            print(Data)
        else:
            print("File is not present")

    except Exception as e:
        print(e)

    finally:
        fd.close()
        print("End of program")


if __name__=="__main__":
    main()
