import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.vkeyboard import VKeyboard

class VKeyboardTest(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		vk = VKeyboard()
		vk.bind(on_key_up=self.key_up)
		self.add_widget(vk)
		
	def key_up(self, *args):
		print(args)
		print("You've pressed the key is: ", args[2])
		
class VKeyboard59App(App):
	def build(self):
		return VKeyboardTest()
	
if __name__ == "__main__":
	VKeyboard59App().run()