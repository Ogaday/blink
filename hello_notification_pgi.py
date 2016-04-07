# coding: utf-8
# Requires pydbus and pgi to be installed via pip.
# I think requires some stuff linux side that should already be installed, such
# as python-gobject and libnotify-bin
from pgi.repository import Notify
Notify.init('Hello World')
n = Notify.Notification.new("Hello, world!", "This is an example notification.", "dialog-information")
n.show()
