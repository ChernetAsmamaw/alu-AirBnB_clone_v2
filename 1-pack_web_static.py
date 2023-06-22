#!/usr/bin/python3
"""Fabfile to generate a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo through
the function do_pack"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a compressed archive of the web_static dir"""
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive_name = "versions/web_static_{}.tgz".format(time_now)
    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.succeeded:
        return archive_name
    else:
        return None

# This file should be run using this syntax:
# fab -f 1-pack_web_static.py do_pack
