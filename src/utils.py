#!/usr/bin/python
# -*- coding: utf-8 -*-

# utils.py is a path of sun.

# Copyright 2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://github.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import re
import urllib2

from __metadata__ import (
    arch,
    conf_path,
    etc_slackpkg,
    changelog_txt,
    var_lib_slackpkg
)


def slack_ver():
    """ Open file and read Slackware version """
    with open("/etc/slackware-version", "r") as f:
        sv = f.read()
        f.close()
    return (".".join(re.findall(r"\d+", sv)))


def read_config(config):
    """ Read config file and return uncomment line """
    for line in config.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            return line


def mirror():
    """ Grab Slackware ChangeLog.txt mirror """
    if os.path.isfile("{0}{1}".format(etc_slackpkg, "mirrors")):
        f = open("{0}{1}".format(etc_slackpkg, "mirrors"), 'r')
        slackpkg_mirrors = f.read()
        f.close()
        slackpkg_mirror = read_config(slackpkg_mirrors)
    if os.path.isfile("{0}{1}".format(conf_path, "mirrors")):
        f = open("{0}{1}".format(conf_path, "mirrors"), 'r')
        slackware_mirrors = f.read()
        f.close()
        slackware_mirror = read_config(slackware_mirrors)
    if slackpkg_mirror and "current" in slackpkg_mirror:
        return "{0}slackware{1}-current/{2}".format(slackware_mirror, arch,
                                                    changelog_txt)
    else:
        return "{0}slackware{1}-{2}/{3}".format(slackware_mirror, arch,
                                                slack_ver(), changelog_txt)


def file_size():
    """ Get ChangeLog.txt file size """
    tar = urllib2.urlopen(mirror())
    meta = tar.info()
    server = int(meta.getheaders("Content-Length")[0])
    local = os.path.getsize("{0}{1}".format(var_lib_slackpkg, changelog_txt))
    return server, local
