
# # ------------------------------ 2.9.2 ---------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.stacklayout import StackLayout
# from kivy.graphics import Rectangle, Color
#
# class StackLayoutWidget(StackLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		with self.canvas:
# 			Color(1, 1, 1, 1)
# 			self.rect = Rectangle(pos=self.pos, size=self.size)
# 			self.bind(pos=self.update_rect, size=self.update_rect)
#
# 		# 遍历添加按钮
# 		for i in range(25):
# 			btn=Button(text=str(i), width=40 + i*5, size_hint=(None, 0.15))
# 			self.add_widget(btn)
#
# 	def update_rect(self, *args):
# 		self.rect.pos = self.pos
# 		self.rect.size = self.size
#
# class StackApp(App):
# 	def build(self):
# 		return StackLayoutWidget()
#
# if __name__ == "__main__":  # 程序入口
# 	StackApp().run()


# ------------------------------ 2.9.3 ---------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/stack.kv')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class StackLayoutWidget(StackLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
class StackApp(App):
	def build(self):
		return StackLayoutWidget()
	
if __name__ == "__main__":  # 程序入口
	StackApp().run()
	
	