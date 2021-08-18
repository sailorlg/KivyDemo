
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/filechooser5.kv')

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyFileChooser(BoxLayout):
	load = ObjectProperty(None)  # 在show_load中进行实例化的时候, 重新复制了.
	cancel = ObjectProperty(None)
	

class FileChooserBox(BoxLayout):
	loadfile = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	def show_load(self):
		content = MyFileChooser(load=self.load, cancel=self.dismiss_popup)
		print(content.load)
		print(content.cancel)

		content_test = MyFileChooser()
		print(content_test.load)
		print(content_test.cancel)
		
		# 打开可以弹窗
		self.__popup = Popup(title="Load File", content=content, size_hint=(0.9, 0.9))
		self.__popup.open()
		
	def load(self, path, filename):
		print(path, filename)
		self.dismiss_popup()
	
	def dismiss_popup(self):
		# 关闭窗口
		self.__popup.dismiss()

class FileChooser5App(App):
	def build(self):
		return FileChooserBox()
	
if __name__ == "__main__":
	FileChooser5App().run()