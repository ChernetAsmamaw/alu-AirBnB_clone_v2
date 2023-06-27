#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["3.90.35.215", "54.159.189.41"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"


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


# Run the script like this:
# $ fab -f 2-do_deploy_web_static.py
# do_deploy:archive_path=versions/file_name.tgz
