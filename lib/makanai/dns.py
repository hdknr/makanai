from fabric.api import task, run, sudo

@task
def check_port():
    sudo('lsof -i:53; echo $?')
