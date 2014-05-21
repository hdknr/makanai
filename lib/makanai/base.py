from fabric.api import env,run,sudo,task,put,get
import os

try:
    from ilogue.fexpect import expect
    from ilogue.fexpect import expecting, run as expect_run
except:
    pass

@task
def ps(*args):
    if args:
        for key in args:
            sudo("ps ax | grep %s" % key ) 
    else:
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
