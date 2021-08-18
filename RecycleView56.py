import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/recycleview56.kv')

from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RecycleViewWidget(RecycleView):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.data = [{'text': str(x)} for x in range(100)]
		
class RecycleView56App(App):
	def build(self):
		return RecycleViewWidget()
	
if __name__ == "__main__":
	RecycleView56App().run()