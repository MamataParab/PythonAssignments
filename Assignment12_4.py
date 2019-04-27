###################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Accepting directory name from user and create logfile in that directory
#          and send mail with logfile as its attachment
#
###################################################################################

import os
import time
import psutil
import smtplib
import schedule
from sys import*
from email import encoders
import urllib.request
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.request.urlopen("http://216.58.192.142",timeout=10)
        return True
    except Exception as err:
        return False

def MailSender(toaddr,fileName,time):
    try:
        fromaddr="missparab93@gmail.com"
        #toaddr="parabm17.instru@coep.ac.in"

        msg=MIMEMultipart()
        msg['From']=fromaddr
        msg['To']=toaddr

        body="""
        Hello %s,
        Please find attached document which contains log file of running process
        Log file is created at: %s

        This is an auto generated mail.

        Thanks & regards,
        Mamata Anil Parab"""%(toaddr,time)

        Subject="""
        Process log filegenerated at : %s"""%(time)

        msg['Subject']=Subject

        msg.attach(MIMEText(body,'plain'))
        attachment=open(filename,'rb')

        p=MIMEBase('application','octet_stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment;fileName=%s"%fileName)
        msg.attach(p)

        s=smtplib.SMTP("smtp.gmail.com",587);

        s.starttls()
        s.login(fromaddr,"Mamataparab@123")

        text=msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        print("Log file successfully sent through mail")

    except  Exception as E:
        print("Unable to send mail",E);

def ProcessLog(log_dir):
    listProcess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"LogFile%s.txt"%(time.ctime()))
    fd=open(log_path,'w')
    fd.write(separator+"\n")
    fd.write("Logger File:"+time.ctime()+"\n");
    fd.write(separator+"\n")
    #fd.write("\n");

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)
        except:
            pass

    for element in listProcess:
        fd.write("%s\n"%element)
    print("LogFile is successfully generated at location %s"%(log_path))

    connected=is_connected()

    if connected:
        print("Connected");
        startTime=time.time()
        MailSender(argv[2],log_path,time.ctime())
        endTime=time.time()

        print("Took %s second to send mail"%(endTime-startTime))
    else:
        print("There is no internet connection")

def main():
    print("Application name:",argv[0])

    if(len(argv)!=3):
        print("Error:Invalid number of arguments")
        exit()

    if((argv[1]=='-h')or(argv[1]=='-H')):
        print("This script is used to maintain log of running process")
        exit()

    
    if((argv[1]=='-u')or(argv[1]=='-U')):
        print("Usage: Application_Name Absolute_path_of_directory")
        exit()

    

    try:
        ProcessLog(argv[1]);
        
    except Exception as E:
        print("Error:Invalid input",E)

    #ProcessLog(sys.argv[1])
    
if __name__=="__main__":
    main()

            


















        





        
