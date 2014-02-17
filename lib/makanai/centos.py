from fabric.api import task, run
from base import *

@task
def packages():
    run('rpm -qa')

@task
def yum_update():
    run('sudo yum update --exclude=kernel* --exclude=grub*')

@task
def yum_check():
    run('sudo yum check-update --exclude=kernel* --exclude=grub*')

@task
def version():
    run('more /etc/redhat-release')
    run('uname -a')
