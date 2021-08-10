
# # --------------------------------- 2.5.2 ----------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App  # 导入kivy的App类, 它是所有kivy应用的基类
# from kivy.uix.gridlayout import GridLayout  # 引入布局
# from kivy.uix.button import Button  # 引入控件
# from kivy.graphics import Rectangle, Color
#
# class GridLayoutWidget(GridLayout):  # 布局类
# 	def __init__(self, **kwargs):  # 初始化
# 		super().__init__(**kwargs)
#
# 		# 设置背景颜色, 可忽略
# 		with self.canvas:
# 			Color(1, 1, 1, 1)
# 			self.rect = Rectangle(pos=self.pos, size=self.size)
# 			self.bind(pos=self.update_rect, size=self.update_rect)
#
#
# 		# 指定行数
# 		self.rows = 3
#
# 		# 指定列数
# 		self.cols = 3
#
# 		# 添加按钮
# 		for i in  range(6):
# 			btn = Button(text="Btn : " + str(i))
# 			self.add_widget(btn)
# 		"""
# 		实际显示的行列数不仅取决于行数和列数的设置,也取决于控件的数量.
# 		例如, 把行数和列数都设置为9, 共九宫格, 但是如果控件数量不足7个, 还是显示为3行*2列
# 		先曼珠行数条件
# 		"""
#
# 	def update_rect(self, *args):  # 设置背景尺寸, 可忽略
# 		self.rect.pos = self.pos
# 		self.rect.size = self.size
#
# class GridApp(App):  # 继承App类
# 	# 实现App类的build()方法, 继承自App类
# 	def build(self):
# 		return GridLayoutWidget()
#
# if __name__ == "__main__":  # 程序入口
# 	GridApp().run()  # 启动应用程序



# --------------------------------- 2.5.1 ----------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'


from kivy.lang import Builder
Builder.load_file('./kvs/grid.kv')

from kivy.app import App  # 导入kivy的App类, App类是kivy所有应用的基类
from kivy.uix.gridlayout import GridLayout  # 导入布局


class GridLayoutWidget(GridLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
		
class GridApp(App):  # 继承App类
	# 实现 App类的build()方法, 继承自App类
	def build(self):
		return GridLayoutWidget()  # 返回根空间
	
if __name__ == "__main__":  # 程序入口
	GridApp().run()  # 启动应用程序