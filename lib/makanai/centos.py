from fabric.api import task, run, sudo
from base import *

@task
def packages():
    run('rpm -qa')

@task
<<<<<<< HEAD
def install_requires():

    #: builds
    sudo('yum install gcc gcc-c++  autoconf automake kernel-devel ncurses-devel')

    #: Name service tools
    sudo('yum install bind-utils')

    #: Python build
    sudo('yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel')
    sudo('yum install ncurses-devel tk-devel gdbm-devel openssl-devel')
    sudo('yum install mysql-devel -y')

    # others
    sudo('yum install tree subversion')

@task
def install_apache():
    sudo('yum groupinstall "Web Server" "MySQL Database client" "MySQL Database server" "PHP Support" -y')
=======
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
>>>>>>> 43f23e16181cf26f79c1fcff01623e5504f9e4e1
