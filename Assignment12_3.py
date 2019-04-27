#####################################################################################
#
# Author:  Mamata Anil Parab                           
# Project: Accepting directory name from user and create logfile in that directory
#
#####################################################################################


from sys import *;
import os;
import psutil;
import time;
import datetime;

def ProcessDisplayLog(log_dir):
	listprocess= [];
	
	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir);
		except Exception:
			pass;
			
	seperator = "-"*80;
	log_path = os.path.join(log_dir, "LogFile%s.txt" %datetime.datetime.now());
	fd = open(log_path, 'w');
	fd.write(seperator + "\n");
	fd.write("Process Logger %s" %datetime.datetime.now() + "\n");
	fd.write(seperator + "\n");
	
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username']);
			pinfo['vms']=proc.memory_info().vms/(1024*1024);
			listprocess.append(pinfo)
			
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.Zombieprocess):
			pass;
			
	for element in listprocess:
		fd.write("%s\n" %element);
	
def main():
	print("Application name " + argv[0]);
	
	if(len(argv) != 2):
		print("Error: Invalid number of arguments");
		exit();
	
	if((argv[1]=="-h") or (argv[1]=="-H")):
		print("This script is used to maintain log of running processes");
		exit();
		
	if((argv[1]=="-u") or (argv[1]=="-U")):
		print("Usage: Application_Name Absolute_path_of_directory ");
		exit();
	
	
	try:
                print("Step1");
		ProcessDisplayLog(argv[1]);
		print("Step2");
	except Exception as eobj:
		print("Error: Invalid Input");
		print(eobj);

if __name__== "__main__":
	main();
