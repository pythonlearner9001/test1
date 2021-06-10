import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from OpenGL.GL import *
from OpenGL.GL import shaders

builder = Gtk.Builder()
builder.add_from_file('test1.glade')
window1 = builder.get_object('window1')
glarea1 = builder.get_object('glarea1')
button1 = builder.get_object('button1')

class Signals:
    def on_window1_destroy(widget):
        Gtk.main_quit()

def on_realize(area):
    area.make_current()
    if (area.get_error() != None):
      return

def on_render(area, context):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()
    print("draw")
    return True

glarea1.connect('realize', on_realize)
glarea1.connect('render', on_render)

builder.connect_signals(Signals())
window1.show_all()
Gtk.main()