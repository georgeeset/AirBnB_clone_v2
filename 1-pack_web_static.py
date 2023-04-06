#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local



def do_pack():
    """
    Returns the archive files into .tgz file
    """
    df = datetime.now()
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        df.year,
        df.month,
        df.day,
        df.hour,
        df.minute,
        df.second
    )

    local('mkdir -p versions')
    check = local("tar -cvzf {} ./web_static/".format(file_name))
    if check.succeeded:
        return file_name
    return None
