from fabric.api import task, run
from base import *

@task
def packages():
    run('dpkg -l')

@task
def apache(cmd='reload'):
    sudo('/etc/init.d/apache2 %s' % cmd )
