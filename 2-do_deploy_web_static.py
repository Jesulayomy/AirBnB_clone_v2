#!/usr/bin/python3

""" Deploys a web static to servers based on some weird shit """

import os
from fabric.api import env, local, put, run


env.user = 'ubuntu'
env.hosts = ['18.234.106.179', '34.207.83.122']


def do_pack():
    """ A function to pack the current webstatic version """

    local('mkdir -p versions')

    current = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current.year, current.month, current.day,
        current.hour, current.minute, current.second)

    path = local('tar -cvzf {} web_static'.format(filename))
    if path.succeeded:
        print("Packed webstatic to {}".format(filename))
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ Deploys a webstatic to a webserver """

    if not os.path.isfile(archive_path):
        return False

    packname = archive_path.split("versions/")[-1]
    temppath = "/tmp/{}".format(packname)
    comppath = "/data/web_static/releases/{}/".format(packname[:-4])

    put(archive_path, temppath)
    run('mkdir -p {}'.format(comppath))
    comp = run('tar -xzf {} -C {}'.format(temppath, comppath))
    if comp.failed:
        return False
    run('rm {}'.format(temppath))
    run('mv {}/web_static/* {}'.format(comppath, comppath))
    run('rm -rf {}/web_static/'.format(comppath))
    run('rm -rf /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(comppath))
    print("New version deployed!")

    return True
