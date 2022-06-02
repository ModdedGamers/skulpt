#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import image as _image_module

__appname__     = "PIL"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = "PIL"


class PixelAccess():
    def __init__(self, parent):
        self._parent = parent

    def __getitem__(self, key):
        p = self._parent._image.getPixel(*key)
        return p.getRed(), p.getGreen(), p.getBlue()

    def __setitem__(self, key, value):
        r, g, b = value
        x, y = key
        self._parent._image.updatePixel(_image_module.Pixel(r, g, b, x, y))


class Image():
    def __init__(self, image):
        self._image = image
        self.size = (self._image.getWidth(), self._image.getHeight())

        self.pixels = PixelAccess(self)

    def open(filename):
        cls = Image
        self = cls(image=_image_module.Image(filename))
        return self

    def load(self):
        return self.pixels

    def show(self):
        win = _image_module.ImageWin(*self.size)
        self._image.draw(win)
