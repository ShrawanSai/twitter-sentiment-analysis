
import subprocess as s
def killProcess(pid):
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)




def stop():
    f=open('pid.txt','r')
    x=f.read()
    print(x)
    f.close()
    
    killProcess(int(x))
