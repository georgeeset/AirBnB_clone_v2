#!/usr/bin/python3

"""
 A Fabric script (based on the file 1-pack_web_static.py)
  that distributes an archive to your web servers
"""
import os
from fabric.api import env, run, put


def do_deploy(archive_path):
    """ deploy package to server """

    env.hosts = ["34.227.94.41", "18.208.119.87"]
    env.user = "ubuntu"

    if os.path.exists(archive_path):
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


def do_pack():
    """ pack files """
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    created_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(
        crated_at
    ))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), created_at))


def deploy():
    """ package && deploy to servers """
    path = do_pack()
    if path is None:
        return False
    return (do_deploy(path))
