#############################################################################
#
# Author: Mamata Anil Parab
# Project: Check whether particular file exists in current directory or not
# Input: "Mamata.txt"
# Output: File is present
#
#############################################################################

import os

def main():

    try:
        print("Enter file Name")
        FileName=input()
        
        exists=os.path.isfile(FileName)
        if exists:
            print("File is present")
        else:
            print("File is not present")
            
    except exception as e:
        print(e)
        print("Unable to find file")

    finally:
        print("End of program")

if __name__=="__main__":
    main()
        
