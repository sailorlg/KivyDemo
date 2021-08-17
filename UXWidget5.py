# ------------------------- 7 ------------------------
import os

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/ux5.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class UXWidget(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		

class Ux5App(App):
	def build(self):
		return UXWidget()
	

if __name__ == "__main__":
	Ux5App().run()