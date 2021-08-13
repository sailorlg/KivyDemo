
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
		
		

class ButtonSampleApp(App):
	def build(self):
		return ButtonSampleWidget()
	

if __name__ == "__main__":
	ButtonSampleApp().run()