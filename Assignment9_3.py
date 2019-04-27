#############################################################################
#
# Author: Mamata Anil Parab
# Project: Copy the contents of one file into another file
# Input: "Source.txt" and "Destination.txt"
# Output: In destination file: Marvellous Infosystems
#
#############################################################################

import sys
import os

def main():
    try:
        SourceName=sys.argv[1]
        DestinationName=sys.argv[2]
        
        fd1=open(SourceName,'r');
        fd2=open(DestinationName,'w');

        for i in fd1.readlines():
            fd2.write(i)
            
        fd2=open(DestinationName,'r')
        print(fd2.read())

    except Exception as e :
        print(e)
        print("Unable to open file")
        
    finally:
        fd1.close()
        fd2.close()
        
if __name__=="__main__":
    main()

    
