
# -------------------------- 3.4.1 / 1 ---------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/rotate.kv')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

class RotateGridLayoutWidget(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	
class RotateApp(App):
	def build(self):
		return RotateGridLayoutWidget()
	
if __name__ == "__main__":
	RotateApp().run()