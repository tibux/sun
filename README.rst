.. image:: https://img.shields.io/github/release/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/releases
.. image:: https://travis-ci.org/dslackw/sun.svg?branch=master
    :target: https://travis-ci.org/dslackw/sun
.. image:: https://landscape.io/github/dslackw/sun/master/landscape.png
    :target: https://landscape.io/github/dslackw/sun/master
.. image:: https://img.shields.io/codacy/ea3c2619e1124874a7d53079092dc956.svg
    :target: https://www.codacy.com/public/dzlatanidis/sun/dashboard
.. image:: https://img.shields.io/pypi/dm/sun.svg
    :target: https://pypi.python.org/pypi/sun
.. image:: https://img.shields.io/badge/license-GPLv3-blue.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/stars/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/forks/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/issues/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/issues

.. contents:: Table of Contents:

About
-----

SUN (Slackware Update Notifier) is a tray notification applet for informing about
package updates in Slackware and CLI tool for monitoring upgraded packages.

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/sun.png
    :target: https://github.com/dslackw/sun

How works
---------
Actually read the two dates of ChangeLog.txt files one the server and a local by counting
how many packages have been upgraded and rebuilt.
 
Installing
----------

.. code-block:: bash

    $ tar xvf sun-1.0.6.tar.gz
    $ cd slpkg-1.0.6
    $ ./install.sh

    or

    $ pip install sun --upgrade

Usage
-----

.. code-block:: bash

    Add sun in your windows manager session startup.
    
    As for xfce:
    Settings Manager --> Session and Startup --> Application Autostart --> +Add
    
    Name: sun
    Description: Slackware Update Notifier
    Command: /usr/bin/sun start --gtk
    [Ok]

i3 wm
-----
Example my_i3status.sh for i3 wm.
Put that in some script, say .bin/my_i3status.sh and execute that instead 
of `i3status <http://i3wm.org/i3status/manpage.html#_external_scripts_programs_with_i3status>`_

.. code-block:: bash

    #!/bin/bash
    i3status | while :
    do
    read line
    # get number of packages it have upgraded
    # fetch()[0] number of upgraded packages
    # fetch()[1] list of upgraded packages
    num="$(python -c 'from sun.utils import fetch; print fetch()[0]')"
    # check if upgraded
    if (($num > 0)); then
        msg="$num software updates are available"
    else
        msg="No news is good news"
    fi
    # print message
    echo "SUN: $msg | $line" || exit 1
    done

    and add my_i3status.sh in ~/.i3/config:
    ~/.i3/config
    bar {
            status_command my_i3status.sh
    }

    
CLI
---

.. code-block:: bash

    $ sun help
    SUN (Slackware Update Notifier) - Version: 1.0.6

    Usage: sun [OPTION]

    Optional  arguments:
      help           display this help and exit
      start          start sun daemon
      stop           stop sun daemon
      restart        restart sun daemon
      check          check for software updates
      status         sun daemon status
      info           os information
    
    $ sun start
    Starting sun daemon:  /usr/bin/sun_daemon

    $ sun stop
    Stoping sun daemon:  /usr/bin/sun_daemon

    $ sun status
    sun is not running
    
    $ sun check
    3 software updates are available !
    samba-4.1.17-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-firefox-31.5.0esr-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-thunderbird-31.5.0-x86_64-1_slack14.1.txz:  Upgraded.


Configuration files
-------------------

.. code-block:: bash

    /etc/sun/sun.conf
        General configuration of sun

    /etc/sun/mirrors
        List of Slackware ChangeLog.txt Mirrors

    /etc/rc.d/rc.sun
        Runtime configuration file

    
Screenshots
-----------

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/gtk_daemon.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/xfce_screenshot.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/kde_screenshot.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/check_updates.png
    :target: https://github.com/dslackw/sun

 
Donate
------
If you feel satisfied with this project and want to thank me go
to `Slackware <https://store.slackware.com/cgi-bin/store/slackdonation>`_ and make a donation 
or visit the `store <https://store.slackware.com/cgi-bin/store>`_.


Copyright 
---------

- Copyright © Dimitris Zlatanidis
- Slackware® is a Registered Trademark of Slackware Linux, Inc.
- Linux is a Registered Trademark of Linus Torvalds.
