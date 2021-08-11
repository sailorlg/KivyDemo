

# # ---------------------------- 2.7.2 ----------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App  # 导入kivy的App类, App类是所有kivy应用的基类
# from kivy.uix.button import Button  # 引入控件
# from kivy.uix.relativelayout import RelativeLayout  # 引入布局
# from kivy.uix.boxlayout import BoxLayout  # 引入布局
# from kivy.graphics import Rectangle, Color
#
# class MyButton(Button):  # 自定义控件类
# 	"""自定义一个按钮, 提出公共属性"""
# 	def __init__(self, **kwargs):  # 初始化
# 		super().__init__(**kwargs)
# 		self.font_size = 20  # 指定按钮字体大小
# 		self.size_hint =[0.2, 0.2]  # 指定按钮的大小
#
# class RelativeLayoutWidget(RelativeLayout):  # 布局类
# 	pass
#
# class BoxLayoutWidget(BoxLayout):  # 布局类
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)  # 初始化
#
# 		# 设置背景颜色, 可忽略
# 		with self.canvas:
# 			Color(1, 1, 1, 1)
# 			self.rect = Rectangle(pos=self.pos, size=self.size)
# 			self.bind(pos=self.update_rect, size=self.update_rect)
#
# 		# 创建一个RelativeLayout布局
# 		relative_layout = RelativeLayoutWidget()
#
# 		# 使用自定义按钮
# 		btn0 = MyButton(text="BTN*0", pos_hint={"right": 1, "top": 1}, background_color=(0.1, 0.5, 0.6, 0.1))
# 		btn1 = MyButton(text="BTN*1", pos_hint={"x": 0, "top": 1}, background_color=(1, 0, 0, 1))
# 		btn_relative = MyButton(text="BTN*Relative", pos_hint={"center_x": 0.5, "center_y": 0.5},
# 		                        background_color=(0.4, 0.5, 0.6, 0.1))
# 		btn2 = MyButton(text="BTN*2", pos_hint={"x": 0, "y": 0}, background_color=(0, 0, 1, 1))
# 		btn3 = MyButton(text="BTN*3", pos_hint={"right": 1, "y": 0}, background_color=(0.8, 0.9, 0.2, 1))
#
# 		# 向RelativeLayout布局循环添加元素
# 		for i in [btn0, btn1, btn_relative, btn2, btn3]:
# 			relative_layout.add_widget(i)
#
# 		# 放一个空的BoxLayout占位
# 		self.add_widget(BoxLayout())
#
# 		# 将RelativeLayout添加到布局中
# 		self.add_widget(relative_layout)
#
# 	def update_rect(self, *args):
# 		"""设置背景尺寸, 可忽略"""
# 		self.rect.pos = self.pos
# 		self.rect.size = self.size
#
# class RelativeApp(App):  # 继承App类
# 	# 实现App类的build()方法
# 	def build(self):
# 		return BoxLayoutWidget()  # 返回根控件
#
# if __name__ == "__main__":
# 	RelativeApp().run()


# ---------------------------- 2.7.3 ----------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/relative.kv')

from kivy.app import App  # 导入kivy的App类, 它是所有kivy应用的基类
from kivy.uix.boxlayout import BoxLayout  # 引入布局

class RelativeLayoutWidget(BoxLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
		

class RelativeApp(App):  # 继承App类
	# 实现App类的build()方法,继承自App类
	def build(self):
		return RelativeLayoutWidget()  # 返回根控件
	
if __name__ == "__main__":  # 程序入口
	RelativeApp().run()  # 启动应用程序