#! /usr/bin/env python

import sys

import gtk
import webkit

class WKWindow(gtk.Window):
	def __init__(self, uri, width, height):
		gtk.Window.__init__(self,gtk.WINDOW_TOPLEVEL)
		self.sw = None

		self.renderHTML(uri, width, height)

	def renderHTML(self, uri, width, height):
		view = webkit.WebView() 
		self.sw = gtk.Window()
		self.sw.add(view)

		self.connect("destroy", gtk.main_quit)

		#self.fullscreen()
		self.set_size_request(1280, 720)
		self.move(0, 0)
		self.add(self.sw)
		self.show_all()

		view.open(uri)

	def capture(self):
		sys.stdout.flush()
		(x, y, width, height, depth) = self.sw.window.get_geometry()
		pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, width, height)
		pixbuf.get_from_drawable(self.sw.window, self.sw.get_colormap(), 0, 0, 0, 0, width, height)
		pixbuf.save('test.png', 'png')

	def loop(self):
		gtk.main()

def main():
	w = WKWindow(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
	w.loop()

if __name__ == '__main__':
	main()
