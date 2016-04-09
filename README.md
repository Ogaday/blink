# Blink

## Blink - An app idea.

Daily screen users struggle with a littany of health risks: RSI, eye strain, bad posture and more. There are guidelines, advice and routines that can be followed. However, it's hard to remember to look away from the screen every twenty minutes and stand up every hour. Wouldn't it be nice to have a configurable pop-up notifier that could remind you to take a break, check your posture and look after yourself? That's the aim of this project.

I also want to use it as a personal experiment in software development.

## Aims

- **Crossplatform**: Either a truely cross platform approach, or it will be necessary to develop independent techniques for each of the big three platofrms.
- **Desktop**: This application is for desktop not for mobile.
- **Notifications**: Periodic notifications for looking away from the screen, checking posture, taking a walk/stretch and drinking water etc. Would be good to use default system notifications one way or another.
- **Run when**: Run when the desktop is being used, not otherwise.
- **Configurable**: It would be nice to be able to configure the timings of the notifications and warnings, as well as have a sane default configuration.
- **Package/distributable installer**: I would like to be able to package this and make it distributable.

## Solutions

- **Language**: Would be nice to use Python as I am a) already familiar with Python b) it is cross platform, to some extent.
- **System notifications**: wxPython, TKinter, Python Global Object introspection, freedesktop.org, dbus, notify, notify2, libnotify, notify send, pgi (pure python GObject Introspection bindings). http://blog.z3bra.org/2014/04/pop-it-up.html
- **Distribution**: http://cyrille.rossant.net/create-a-standalone-windows-installer-for-your-python-application/ https://wiki.python.org/moin/DistributionUtilities https://github.com/pyinstaller/pyinstaller
