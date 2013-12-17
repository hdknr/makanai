Makanai
========================================================================

configure bash
--------------------

::

    $ source $VIRTUAL_ENV/bin/makanai.bash
    
provide .credential.fab
--------------------------------


::

     fabfile=fabrics.py
     user=remote_user
     hosts=remote_host.com
     key_filename=~/.ssh/id_rsa
     password=remote_passwod


provide fabrics.py
--------------------------------

- if remote server is Debian.

::

    from fabric.api import task,sudo
    from makanai.debian import *    

    @task
    def your_task(cmd='reload'):
        sudo('your_app_management.bash %s' % cmd)


run remote command
---------------------

::

    $ fabs your_task:stop


ssh
------

::

    $ fabs ssh
