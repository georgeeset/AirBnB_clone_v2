#!/usr/bin/python3
"""
a Fabric script that generates a .tgz
archive from the contents of the web_static folder
"""
import datetime
import os
from fabric.api import local


def do_pack():
    """
    pack data
    """
    if not os.path.isdir("versions"):
        os.makedirs("versions")
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response = local(
        f"tar -czzf versions/web_static_{current_time}.tgz web_static/*"
        )
    if response.succeeded:
        return "versions/web_static_{}".format(current_time)
