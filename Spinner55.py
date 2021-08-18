
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/spinner55.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class GridLayoutWidget(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		

class Snipper55App(App):
	def build(self):
		return GridLayoutWidget()
	
if __name__ == "__main__":
	Snipper55App().run()
