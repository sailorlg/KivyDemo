
# # --------------------------------- 2.8.3 --------------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App  # 导入kivy的App类, 它是所有kivy应用的基类
# from kivy.uix.image import AsyncImage  # 引入异步加载图片控件
# from kivy.uix.boxlayout import BoxLayout  # 引入布局
# from kivy.uix.scatterlayout import ScatterLayout  # 引入布局
# from kivy.graphics import Rectangle, Color
#
# class ScatterLayoutWidget(ScatterLayout):  # 布局类
# 	pass
#
# class BoxLayoutWidget(BoxLayout):  # 布局类
# 	def __init__(self, **kwargs):  # 初始化
# 		super().__init__(**kwargs)
#
# 		# 设置背景颜色, 可忽略
# 		with self.canvas:
# 			Color(1, 1, 1, 1)
# 			self.rect =Rectangle(pos=self.pos, size=self.size)
# 			self.bind(pos=self.update_rect, size=self.update_rect)
#
# 		# 创建一个ScatterLayout布局
# 		scatter_layout = ScatterLayoutWidget()
# 		# 异步加载图片
# 		image = AsyncImage(source="https://bbswater-fd.zol-img.com.cn/t_s1200x5000/g6/M00/09/0A/ChMkKmERe3eICW8xAATSA6bjX84AASndwFxk6MABNIb638.jpg")
# 		# image1 = AsyncImage(source=r"./images/shan.jpg")
# 		# 将图片添加到ScatterLayout布局中
# 		scatter_layout.add_widget(image)
# 		# scatter_layout.add_widget(image1)
# 		# 将ScatterLayout布局嵌套在BoxLayout布局中
# 		self.add_widget(scatter_layout)
#
# 	def update_rect(self, *args):
# 		"""设置背景尺寸, 可忽略"""
# 		self.rect.pos = self.pos
# 		self.rect.size = self.size
#
# class ScatterApp(App):  # 继承App类
# 	def build(self):  # 实现App类的build()方法
# 		return BoxLayoutWidget()  # 返回根控件
#
# if __name__ == "__main__":  # 程序入口
# 	ScatterApp().run()  # 启动应用程序


import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/scatter.kv')

from kivy.app import App  # 导入kivy的App类, App类是所有kivy应用的基类
from kivy.uix.boxlayout import BoxLayout  # 引入布局

class ScatterLayoutWidget(BoxLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
		
class ScatterApp(App):  # 继承App类
	# 实现App类的build()方法, 继承自App类
	def build(self):
		return ScatterLayoutWidget()  # 返回根控件
	
if __name__ == "__main__":  # 程序入口
	ScatterApp().run()  # 启动应用程序