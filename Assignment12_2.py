#####################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Display information as name, PID and username of process if it is running
#
#####################################################################################
import psutil
import sys

def CheckProcessRunning(ProcessName):
    for proc in psutil.process_iter():
        try:
            if ProcessName.lower()in proc.name().lower():
                return True
        except Exception:
            print("Error");
            pass;
    return False

def main():
    print("Process Name :", (sys.argv[0]));
    if CheckProcessRunning(sys.argv[1]):
        print("The given process is Running");
        for proc in psutil.process_iter():
            try:
                pinfo=proc.as_dict(attrs=['pid','name','username'])
           # pinfo['vms']=proc.memory_info().vms/(1024*1024)

                listprocess.append(pinfo)
            except Exception:
                pass


    else:
        print("The given process is not Running");

if __name__=="__main__":
    main()
        
            
