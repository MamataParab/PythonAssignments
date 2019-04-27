#############################################################################
#
# Author: Mamata Anil Parab
# Project: Compare the contents of two files 
# Input: "Source.txt" and "Destination.txt"
# Output: SUCCESS if contents are sane or FAIL if contents are different
#
#############################################################################

import sys
import os

def main():

    try:
        FileName1=sys.argv[1]
        FileName2=sys.argv[2]

        fd1=open(FileName1,"r")
        fd2=open(FileName2,"r")

        Data1=fd1.read()
        Data2=fd2.read()

        if Data1==Data2:
            print("SUCCESS")
        else:
            print("FAILED")
            
    except Exception as e:
        print(e)
        print("Unable to open file")

    finally:
        fd1.close()
        fd2.close()

if __name__=="__main__":
    main()
