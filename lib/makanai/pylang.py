from fabric.api import env,run,sudo,task,put,get
import os


class PyLang(object):
    def __init__(self, venv_home, venv_name):
        self.venv_home = venv_home
        self.venv_name = venv_name
    
    @property
    def activate(self):
        if not self.venv_home:
            return ""

        return "source %s/%s/bin/activate && " % (self.venv_home, self.venv_name)

    def do(self,subcommand,*args):
        cmd = self.activate + " ".join((subcommand,)+args)
        run(cmd)

    def run(self, subcommand, *args):
        if subcommand in ['pip', 'yolk', ]:
            return self.do(subcommand, *args)

        print "No supported", subcommand, args

@task
def py(*args):
    if env.pylang:
        env.pylang.run(*args)
