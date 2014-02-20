from fabric.api import task, run, sudo
from base import *

@task
def packages():
    run('rpm -qa')

@task
def chkconfig(name=''):
    name = name and '| grep ' + name
    sudo('chkconfig --list %s' % name )

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
