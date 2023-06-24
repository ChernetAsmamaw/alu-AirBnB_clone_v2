#!/usr/bin/python3
"""FabScript that deletes out-of-date archives"""

import os
from fabric.api import *

env.hosts = ["3.90.35.215", "54.159.189.41"]


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    number: number of archives to keep
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]


# Run the script like this:
# First "ls -ltr versions" | to see the list of archives
# >>> $ fab -f 100-clean_web_static.py do_clean:number=2
# -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
