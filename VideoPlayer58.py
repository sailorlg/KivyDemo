
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

# from kivy.lang import Builder
# Builder.load_file('./kvs/videoplayer58.kv')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer

class VideoPlayerTest(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		player = VideoPlayer(source="./images/videotest.mp4", state="play", options={"allow_stretch": True, "eos": "loop"})
		
		self.add_widget(player)
		
class VideoPlayer58App(App):
	def build(self):
		return VideoPlayerTest()
	
if __name__ == "__main__":
	VideoPlayer58App().run()