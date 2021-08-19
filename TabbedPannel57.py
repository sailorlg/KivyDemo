
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/tabbedpannel57.kv')


from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel

class TabbedPannelTest(TabbedPanel):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		print('\n'.join(("Hello World", "----------------", "You Are In The Third Tab")))

class TabbedPannel57App(App):
	def build(self):
		return TabbedPannelTest()
	

if __name__ == "__main__":
	TabbedPannel57App().run()
 
