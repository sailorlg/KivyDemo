
# # --------------------------------- 1 ----------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
#
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.graphics import Rectangle, Color
#
#
# class BoxLayoutWidget(BoxLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		# 设置背景
# 		with self.canvas:
# 			# 设置背景颜色, rgba格式, 通常值为0~1之间(具体的值/255)
# 			Color(1, 1, 1, 1)
# 			Rectangle(pos=self.pos, size=self.size)
#
# class Page3App(App):
# 	def build(self):
# 		return BoxLayoutWidget()
#
# if __name__ == "__main__":
# 	Page3App().run()


# --------------------------------- 2 ----------------------
import os

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color


class BoxLayoutWidget(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		# 设置背景
		with self.canvas:
			# 设置背景颜色, rgba格式, 通常值为0~1之间(具体的值/255)
			Color(1, 1, 1, 1)
			self.rect = Rectangle(pos=self.pos, size=self.size)
			self.bind(pos=self.update_rect, size=self.update_rect)
			
	def update_rect(self, *args):
		"""设置背景尺寸"""
		self.rect.pos = self.pos
		self.rect.size = self.size


class Page3App(App):
	def build(self):
		return BoxLayoutWidget()


if __name__ == "__main__":
	Page3App().run()