#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

import os
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists

env.hosts = ["3.90.35.215", "54.159.189.41"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"


def do_pack():
    """Create a .tgz archive from the web_static folder."""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)
    local("tar -cvzf {} web_static".format(archive_path))
    if os.path.exists(archive_path):
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers"""
    if not exists(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    file_wout = file_name.split(".")[0]
    path = "/data/web_static/releases/"
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_wout))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, file_wout))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_wout))
        run('rm -rf {}{}/web_static'.format(path, file_wout))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_wout))
        return True
    except Exception:
        return False


def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


# This script should be run this way:
# $ fab -f 3-deploy_web_static.py deploy\
# -i my_ssh_private_key -u ubuntu
