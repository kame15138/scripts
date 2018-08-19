import time as t
from os import path


def createFile(dest):
    '''

    kamesh

    '''
    date=t.localtime(t.time())

    for i in range(0,5):
        name="%d.txt"%(i)
        if not(path.isfile(dest +name)):
            f=open(dest+name,'w')
            f.write("kamesh\n"*3)
            f.close()
        
        
if __name__=='__main__':
    sys_name=os.getlogin()
    des='/home/'+sys_name+'/Desktop/'
    createFile(des)
    input("done")
