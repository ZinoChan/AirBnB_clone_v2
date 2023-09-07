#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""
from fabric.api import local
import time


def create_directory():
    """Create versions directory if it doesn't exist."""
    local("mkdir -p versions")


def archive_path():
    """Generate the path for the archive based on the current timestamp."""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    return "versions/web_static_{}.tgz".format(timestamp)


def create_archive(path):
    """Generate the archive at the specified path."""
    return local("tar -cvzf {} web_static/".format(path))


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    create_directory()
    path = archive_path()

    if create_archive(path).succeeded:
        return path
    return None
