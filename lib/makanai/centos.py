from fabric.api import task, run
from base import *
@task
def packages():
    run('rpm -qa')
