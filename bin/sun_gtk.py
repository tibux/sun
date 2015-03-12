#!/usr/bin/python
# -*- coding: utf-8 -*-


import gtk
import commands
import subprocess
from sun.__metadata__ import (
    __all__,
    icon_path
)
from sun.utils import fetch


class GtkStatusIcon(object):

    def __init__(self):
        # status = GtkStatusIcon()
        self.icon = gtk.status_icon_new_from_file("{0}{1}.png".format(icon_path,
                                                                      __all__))
        self.icon.connect('popup-menu', self.right_click)

        self.cmd = "/etc/rc.d/rc.sun"

    def icon_menu(self, event_button, event_time, data=None):
        menu = gtk.Menu()
        about = gtk.MenuItem("About")
        start = gtk.MenuItem("Start daemon")
        stop = gtk.MenuItem("Stop daemon")
        restart = gtk.MenuItem("Restart daemon")
        check = gtk.MenuItem("Check updates")
        status = gtk.MenuItem("Status daemon")
        exit = gtk.MenuItem("Exit")

        menu.append(about)
        menu.append(start)
        menu.append(stop)
        menu.append(restart)
        menu.append(check)
        menu.append(status)
        menu.append(exit)

        about.connect_object("activate", self._about, "About")
        start.connect_object("activate", self._start, "Start daemon")
        stop.connect_object("activate", self._stop, "Stop daemon")
        restart.connect_object("activate", self._restart, "Restart daemon")
        check.connect_object("activate", self._check, "Check updates")
        status.connect_object("activate", self._status, "Status daemon")
        exit.connect_object("activate", self._exit, "Exit")

        about.show()
        start.show()
        stop.show()
        restart.show()
        check.show()
        status.show()
        exit.show()

        menu.popup(None, None, None, event_button, event_time, data=None)

    def message(self, data):
        """ Function to display messages to the user """

        msg = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO,
                                gtk.BUTTONS_OK, data)
        msg.run()
        msg.destroy()

    def right_click(self, data, event_button, event_time):
        self.icon_menu(event_button, event_time)

    def _about(self, data=None):
        self.message(data)

    def _start(self, data=None):
        subprocess.call("{0} {1}".format(self.cmd, "start"), shell=True)
        self.message("Starting sun daemon ...")

    def _stop(self, data=None):
        subprocess.call("{0} {1}".format(self.cmd, "stop"), shell=True)
        self.message("Stoping sun daemon ...")

    def _restart(self, data=None):
        subprocess.call("{0} {1}".format(self.cmd, "restart"), shell=True)
        self.message("Restarting sun daemon ...")

    def _check(self, data=None):
        upgraded, packages = fetch()[2:]
        if upgraded > 0:
            self.message("{0} software updates are available "
                         "!\n\n{1}".format(str(upgraded), "\n".join(packages)))
        else:
            self.message("No news is good news !")

    def _status(self, data=None):
        out = commands.getoutput("ps -A")
        if "sun_daemon" in out:
            self.message("sun is running ...")
        else:
            self.message("sun not running")

    def _exit(self, data=None):
        subprocess.call("{0} {1}".format(self.cmd, "stop"), shell=True)
        gtk.main_quit()


if __name__ == '__main__':
    GtkStatusIcon()
    gtk.main()
