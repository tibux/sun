#!/usr/bin/python
# -*- coding: utf-8 -*-

# sun_gtk is a path of sun.

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
        self.sun_icon = "{0}{1}.png".format(icon_path, __all__)
        self.icon = gtk.status_icon_new_from_file(self.sun_icon)
        self.icon.connect('popup-menu', self.right_click)
        self.cmd = "/etc/rc.d/rc.sun"
        gtk.main()

    def sub_menu(self):

        self.start = gtk.MenuItem("Start")
        self.stop = gtk.MenuItem("Stop")
        self.restart = gtk.MenuItem("Restart")
        self.status = gtk.MenuItem("Status")

        self.start.show()
        self.stop.show()
        self.restart.show()
        self.status.show()

        submenu = gtk.Menu()
        submenu.append(self.start)
        submenu.append(self.stop)
        submenu.append(self.restart)
        submenu.append(self.status)

        self.daemon = gtk.ImageMenuItem("Daemon")
        self.img_daemon = gtk.image_new_from_stock(gtk.STOCK_MEDIA_RECORD,
                                                   gtk.ICON_SIZE_MENU)
        self.img_daemon.show()
        self.daemon.set_submenu(submenu)

    def menu(self, event_button, event_time, data=None):

        self.sub_menu()
        menu = gtk.Menu()
        menu.append(self.daemon)

        menu_About = gtk.ImageMenuItem("About")
        img_About = gtk.image_new_from_stock(gtk.STOCK_ABOUT,
                                             gtk.ICON_SIZE_MENU)
        img_About.show()

        self.daemon.set_image(self.img_daemon)
        menu.append(self.daemon)
        self.daemon.show()

        menu_Quit = gtk.ImageMenuItem("Quit")
        img_Quit = gtk.image_new_from_stock(gtk.STOCK_QUIT,
                                            gtk.ICON_SIZE_MENU)
        img_Quit.show()

        menu_About.set_image(img_About)
        menu_Quit.set_image(img_Quit)

        menu.append(menu_About)
        menu.append(menu_Quit)

        menu_About.show()
        menu_Quit.show()

        menu_About.connect_object("activate", self._About, "About")
        self.start.connect_object("activate", self._start, "Start daemon")
        self.stop.connect_object("activate", self._stop, "Stop daemon")
        self.restart.connect_object("activate", self._restart, "Restart daemon")
        self.status.connect_object("activate", self._status, "Status: ")
        menu_Quit.connect_object("activate", self._Quit, "Quit")

        menu.popup(None, None, None, event_button, event_time, data)

    def message(self, data):
        """ Function to display messages to the user """

        msg = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO,
                                gtk.BUTTONS_OK, data)
        img = gtk.Image()
        img.set_from_file(self.sun_icon)
        msg.set_image(img)

        # action_area = msg.get_content_area()
        # label_2 = gtk.Label("Slackware Update Notifier")
        # action_area.add(label_2)

        msg.show_all()
        msg.run()
        msg.destroy()

    def right_click(self, data, event_button, event_time):
        self.menu(event_button, event_time)

    def _About(self, data):
        self.message(data)

    def _start(self, data):
        subprocess.call("{0} {1}".format(self.cmd, "start"), shell=True)
        self.message(data)

    def _stop(self, data):
        subprocess.call("{0} {1}".format(self.cmd, "stop"), shell=True)
        self.message(data)

    def _restart(self, data):
        subprocess.call("{0} {1}".format(self.cmd, "restart"), shell=True)
        self.message(data)

    def _check(self, data):
        upgraded, packages = fetch()[2:]
        if upgraded > 0:
            self.message("{0} software updates are available "
                         "!\n\n{1}".format(str(upgraded), "\n".join(packages)))
        else:
            self.message("No news is good news !")

    def _status(self, data):
        out = commands.getoutput("ps -A")
        if "sun_daemon" in out:
            self.message(data + " sun is running ...")
        else:
            self.message(data + " sun not running")

    def _Quit(self, data):
        subprocess.call("{0} {1}".format(self.cmd, "stop"), shell=True)
        gtk.main_quit()


if __name__ == '__main__':
    GtkStatusIcon()
