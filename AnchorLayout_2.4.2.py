
# # --------------------------------- 2.4.2 ----------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App  # 导入kivy的App类, App类是所有kivy用用的的基类
# from kivy.uix.anchorlayout import AnchorLayout  # 引入布局
# from kivy.uix.button import Button  # 引入控件
# from kivy.graphics import Rectangle, Color
#
#
# class AnchorLayoutWidget(AnchorLayout):  # 布局类
# 	def  __init__(self, **kwargs):  # 初始化
# 		super().__init__(**kwargs)
#
# 		# 设置背景颜色, 可忽略
# 		with self.canvas:
# 			Color(1, 1, 1, 1)
# 			self.rect = Rectangle(pos=self.pos, size=self.size)
# 			self.bind(pos=self.update_rect, size=self.update_rect)
#
# 		# 嵌套第一个布局
# 		anchor_first = AnchorLayout(anchor_x='left', anchor_y='top')
#
# 		# 添加按钮
# 		anchor_first.add_widget(Button(text='Hello', size_hint=[0.3, 0.2]))
#
# 		# 嵌套第二个布局
# 		anchor_second = AnchorLayout(anchor_x='right', anchor_y='bottom')
#
# 		# 添加按钮
# 		anchor_second.add_widget(Button(text='Anchor', size_hint=[0.3, 0.2]))
# 		# 添加到父布局中
# 		self.add_widget(anchor_first)
# 		self.add_widget(anchor_second)
#
# 	def update_rect(self, *args):  # 设置背景尺寸, 可忽略
# 		self.rect.pos = self.pos
# 		self.rect.size = self.size
#
#
#
# class AnchorApp(App):  # 继承App类
# 	def build(self):  # 实现App类的build()方法
# 		return AnchorLayoutWidget()  # 返回根控件
#
# if __name__ == "__main__":  # 程序入口
# 	AnchorApp().run()  # 启动应用程序


# --------------------------------- 2.4.3 ----------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

# 与kv文件不在同一个目录,因此先把kv文件导入
from kivy.lang import Builder
Builder.load_file('./kvs/anchor.kv')

from kivy.app import App   # 导入kivy的App类, 它是所有kivy应用的基类
from kivy.uix.anchorlayout import AnchorLayout  # 引入布局

class AnchorLayoutWidget(AnchorLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
		
class AnchorApp(App):  # 继承App类
	# 实现App类的build()方法 (继承自App类)
	def build(self):
		return AnchorLayoutWidget()  # 返回根控件
	
if __name__ == "__main__":  # 程序入口
	AnchorApp().run()  # 启动应用程序
