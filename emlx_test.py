import os
from pydoc import pathdirs
import emlx
import glob

#sudo chown -R user:group venv/

#fname = glob.glob('./Users/<username>/Library/Mail/V9/**/*.emlx', recursive = True)
#files = glob.glob(pathname="/*",root_dir="/Users/lxp/Library/Mail/V9/",recursive = True)

mail_dir = "/".join(os.getcwd().split("/")[:3])+'/Library/Mail/V9/'
print(mail_dir)
os.chdir(mail_dir)

cwd = os.getcwd()
print("cwd: ",cwd)
