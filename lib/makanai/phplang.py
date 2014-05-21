from fabric.api import env,run,sudo,task,put,get
import os


@task
def version(*args):
    run("php -v")
