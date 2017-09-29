import os
import _thread
import threading
from win32com.shell import shell
from win32com.shell import shellcon
import pythoncom

def GetpathFromLink(lnkpath):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.QueryInterface( pythoncom.IID_IPersistFile ).Load(lnkpath)
    path = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]

    return path
	
def ExecTask(rootdir,file):
	path = os.path.join(rootdir,file)
	if "exe" in path:
		realpath = GetpathFromLink(path)
		print("正在启动……"+realpath)
		os.system("start " + realpath)

		
		
rootdir = os.getcwd()
print(rootdir)
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
#	_thread.start_new_thread(ExecTask,(rootdir,list[i], ))
#	threading.Thread(target=ExecTask,args=(rootdir,list[i])).start()
	ExecTask(rootdir,list[i])