#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local

d = datetime.now()


def do_pack():
    """
    Returns the archive files into .tgz file
    """

    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(d.year,
                                                              d.month,
                                                              d.day,
                                                              d.hour,
                                                              d.minute,
                                                              d.second)
    local('mkdir -p versions')
    check = local("tar -cvzf " + file_name + " ./web_static/")
    if check.succeeded:
        return file_name
    return None
