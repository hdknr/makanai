from fabric.api import task, run, sudo
from base import *

@task
def packages():
    run('rpm -qa')

@task
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
