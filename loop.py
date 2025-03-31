import subprocess
import sys
import os

if __name__=='__main__':
    ret = 1
    while ret!=0:
        ret = subprocess.call(sys.argv[1:], shell=True, text=True)
        # ret = os.system(' '.join(sys.argv[1:]))
