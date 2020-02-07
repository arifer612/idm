import subprocess
import sys

idm = subprocess.check_output('dir \idman.exe /s', shell = True).decode("utf-8").partition("Directory of ")[2].partition("\r\n\r")[0] # Retrieve directory for idman.exe

class download():
    def __init__(self,url,directory,args):
        while isinstance(url,str) and isinstance(directory,str) and isinstance(args,str):
            cmd = 'cd ' + idm + ' /d ' + url + ' /p ' + directory + ' ' + args
            subprocess.Popen(cmd, shell = True)
        else:
            print("Only string inputs. For more information on the external arguments allowed, please refer to the IDM documentation")
            sys.exit(1) # Abort because of error