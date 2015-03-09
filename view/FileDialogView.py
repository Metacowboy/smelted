from gi.repository import Gtk
from GtkView import GtkView


class FileDialogView(GtkView):

	def __init__(self, controller):
		super(FileDialogView, self).__init__(controller)
		Gtk.Window.__init__(self, title="File Chooser")

	def open_dialog(self, type, title):
		dialog = Gtk.FileChooserDialog(title, self,
			type,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

		self.add_filters(dialog)

		response = dialog.run()
		file_name = dialog.get_filename()
		dialog.destroy()
		if response == Gtk.ResponseType.OK:
			self.controller.on_close_dialog(file_name)

	def add_filters(self, dialog):
		filter_xml = Gtk.FileFilter()
		filter_xml.set_name("XML files")
		filter_xml.add_mime_type("text/xml")
		dialog.add_filter(filter_xml)