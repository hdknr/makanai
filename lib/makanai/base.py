from fabric.api import env,run,sudo,task

try:
    from ilogue.fexpect import expect
    from ilogue.fexpect import expecting, run as expect_run
except:
    pass
    
@task
def ps():
    sudo("ps ax")
