import gi
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Power Options")
        self.set_border_width(10)
        self.set_resizable(False)

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        hbox1 = Gtk.HBox(spacing=6)
        vbox.pack_start(hbox1, True, True, 0)

        button1 = Gtk.Button(label="󰐥")
        self.set_button_font(button1, 24)
        button1.connect("clicked", self.on_poweroff_clicked)
        hbox1.pack_start(button1, True, True, 0)

        button2 = Gtk.Button(label="󰜉")
        self.set_button_font(button2, 25)
        button2.connect("clicked", self.on_reboot_clicked)
        hbox1.pack_start(button2, True, True, 0)

        button3 = Gtk.Button(label="Cancel")
        button3.connect("clicked", self.on_cancel_clicked)
        vbox.pack_start(button3, True, True, 0)

    def set_button_font(self, button, size):
        label = button.get_child()
        if isinstance(label, Gtk.Label):
            font_desc = Pango.FontDescription(f"normal {size}")
            label.override_font(font_desc)

    def on_poweroff_clicked(self, widget):
        subprocess.run(["poweroff"])

    def on_reboot_clicked(self, widget):
        subprocess.run(["reboot"])

    def on_cancel_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
