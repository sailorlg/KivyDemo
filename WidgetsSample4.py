
# ------------------------- # ------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'


from kivy.lang import Builder
Builder.load_file('./kvs/buttonsample.kv')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ButtonSampleWidget(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def press_button(self, arg):
		"""按下按钮触发事件的回调函数"""
		print("------press_button---------")
		
	def release_button(self, arg):
		"""按下按钮并释放触发事件的回调函数"""
		print("----------release_button--------------")
		
		

class ButtonSampleApp(App):
	def build(self):
		self.root_canvas = ButtonSampleWidget()
		return self.root_canvas
	

if __name__ == "__main__":
	ButtonSampleApp().run()