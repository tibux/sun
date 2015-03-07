.. image:: https://img.shields.io/github/release/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/releases
.. image:: https://travis-ci.org/dslackw/sun.svg?branch=master
    :target: https://travis-ci.org/dslackw/sun
.. image:: https://landscape.io/github/dslackw/sun/master/landscape.png
    :target: https://landscape.io/github/dslackw/sun/master
.. image:: https://img.shields.io/codacy/6464ba0bd1e342e28388c71a34b3a5e8.svg
    :target: https://www.codacy.com/public/dzlatanidis/slpkg/dashboard
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


About
-----

Slackware Update Notifier is a tray notification applet for informing about
package updates in Slackware.

.. image:: https://raw.githubusercontent.com/dslackw/sun/master/icon/sun.png
    :target: https://github.com/dslackw/sun


Installing
----------

.. code-block:: bash

    $ pip install sun

Usage
-----

.. code-block:: bash

    $ sun start
    Starting sun daemon:  /usr/bin/sun_daemon

    $ sun stop
    Stoping sun daemon:  /usr/bin/sun_daemon

    $ sun status
    sun is not running

    Also you can add sun in your windows manager session startup.
    As for xfce:
    Settings --> Settings Manager --> Session and Startup --> Application Autostart --> +Add
    
    Name: sun
    Description: Slackware Update Notifier
    Command: /usr/bin/sun start
    [Ok]

Screenshot
---------

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/sun_screenshot.png
    :target: https://github.com/dslackw/sun
 
