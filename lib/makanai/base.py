from fabric.api import env,run,sudo,task,put,get
import os

try:
    from ilogue.fexpect import expect
    from ilogue.fexpect import expecting, run as expect_run
except:
    pass

@task
def ps():
    sudo("ps ax")

@task
def send_file(src,dst=None):
    if not dst:
        dst = os.path.basename(src)

    put(src,dst)

@task
def get_file(src,dst=None):
    if not dst:
        dst = '.' 
    get(src,dst )
