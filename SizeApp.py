import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.app import App  # 导入Kivy的App类, 它是所有Kivy应用的基类
from kivy.uix.floatlayout import FloatLayout  # 引入布局

class SizeFloat(FloatLayout):
	"""
	布局类
	"""
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
	
class SizeApp(App):  # 继承App类
	"""
	实现App类的build()方法(继承自App类)
	"""
	def build(self):
		return SizeFloat()  # 返回根空间
	
if __name__ == "__main__":  # 程序入口
	SizeApp().run()  # 启动应用程序