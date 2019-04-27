###############################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Display information of running process as name, PID and username
#
###############################################################################
import psutil

def ProcessDisplay():
    listprocess=[];

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
           # pinfo['vms']=proc.memory_info().vms/(1024*1024)

            listprocess.append(pinfo)
        except Exception:
            pass
        return listprocess;

def main():
    listprocess=ProcessDisplay();

    for element in listprocess:
        print(element)

if __name__=="__main__":
    main()
    
