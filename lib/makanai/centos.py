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
def rpm_search(name):
    run('rpm -qa | grep %s' % name)

@task
def rpm_list(name):
    run('rpm -ql %s' % name)

@task
def version():
    run('more /etc/redhat-release')
    run('uname -a')
    run('uptime')

@task
def chkconfig(name=None):
    name = name and " | grep " + name or ''
    sudo('chkconfig --list ' + name )
