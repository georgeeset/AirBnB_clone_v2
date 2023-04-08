#!/usr/bin/python3
"""
 A Fabric script (based on the file 1-pack_web_static.py)
  that distributes an archive to your web servers
"""
import os
from fabric.api import env, run,put



def do_deploy(archive_path):
    """ deploy package to server"""

    env.hosts = ["34.227.94.41", "18.208.119.87"]
    env.user = "ubuntu"

    if not archive_path or not os.path.exists(archive_path):
        print("NOT PATH")
        return False

    split_path = os.path.basename(archive_path)
    file_name = split_path.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(file_name))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        split_path, file_name
    ))
    run("rm /tmp/{}".format(split_path))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ /data/web_static/current".format(
        file_name
    ))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True
