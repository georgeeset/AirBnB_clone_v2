#!/usr/bin/python3
"""
 A Fabric script (based on the file 1-pack_web_static.py)
  that distributes an archive to your web servers
"""
import os
from fabric.api import env, run, put, local
from datetime import datetime


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


def do_deploy(archive_path):
    """ deploy package to server """

    print("deploying")
    env.hosts = ["34.227.94.41", "100.24.205.173"]
    env.user = "ubuntu"

    if not os.path.exists(archive_path):
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
    run("rm -rf /data/web_static/current/web_static")

    return True


def deploy():
    """ package and deploy files to servers """
    path = do_pack()
    if path is None:
        return False
    return (do_deploy(path))
