from Controller import Controller
from model import ModelManager
import os


class MainInterfaceController(Controller):

	melted_telnet_controller = None
	main_controller = None

	playlist_list_store = None

	def __init__(self, main_controller, melted_telnet_controller):
		self.main_controller = main_controller
		self.melted_telnet_controller = melted_telnet_controller

	def on_view_added(self, view):
		self.playlist_list_store = self.view.builder.get_object("playlist_list_store")
		ModelManager.register_on_model_added_callback(self.new_clip, ModelManager.MODEL_CLIP)

	def add_file_handler(self, paths):
		if len(paths) > 0:
			path = paths[0]
			self.melted_telnet_controller.load_clip(0, path)
			self.main_controller.get_unit_controller().find_clips_on_unit(ModelManager.get_models(ModelManager.MODEL_UNIT)[0]['model'])
		else:
			print("No file selected")

	def play_handler(self):
		self.melted_telnet_controller.play_clip(0)

	def pause_handler(self):
		self.melted_telnet_controller.pause_clip(0)

	def stop_handler(self):
		self.melted_telnet_controller.stop_clip(0)

	def rewind_handler(self):
		self.melted_telnet_controller.rewind_clip(0)

	def forward_handler(self):
		self.melted_telnet_controller.forward_clip(0)

	def loop_handler(self, active):
		if active:
			self.melted_telnet_controller.loop_clip(0)
		else:
			self.melted_telnet_controller.stop_looping_clip(0)

	def seek_bar_button_release_handler(self, percent):
		self.melted_telnet_controller.goto_position_clip(0, percent)

	def new_clip(self):
		self.playlist_list_store.clear()
		clips = ModelManager.get_models(ModelManager.MODEL_CLIP)
		for clip in clips:
			clip = clip['model']
			self.playlist_list_store.append([os.path.basename(clip.path)])