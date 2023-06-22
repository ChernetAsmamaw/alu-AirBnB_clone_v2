#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api env, put, run
from os.path import exists

env.hosts = ["3.90.35.215", "34.226.202.215"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path_name))
        run("tar -xzf /tmp/{} -C {}/".format(archive_name, path_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}/".format(path_name, path_name))
        run("rm -rf {}/web_static".format(path_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(path_name))
        return True
    except Exception:
        return False

# This file should be run using this syntax:
# fab -f 2-do_deploy_web_static.py 
# do_deploy:archive_path=versions/web_static_20170315003959.tgz
