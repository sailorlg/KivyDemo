# # --------------------------------- 2.6.2 ----------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App  # 导入kivy的App类, App类是所有kivy应用的基类
# from kivy.uix.button import Button  # 导入控件
# from kivy.uix.pagelayout import PageLayout  # 引入布局
#
# class PageLayoutWidget(PageLayout):  # 布局类
# 	def __init__(self, **kwargs):  # 初始化
# 		super().__init__(**kwargs)
#
# 		# 创建两个按钮
# 		btn0 = Button(text="BTN0", background_color=[0.0, 0.9, 0.9, 0.1])
# 		btn1 = Button(text="BTN1", background_color=[0.9, 0.0, 0.3, 0.9])
#
# 		# 添加到布局中
# 		self.add_widget(btn0)
# 		self.add_widget(btn1)
#
#
# class PageApp(App):  # 继承App类
# 	def build(self):  #  实现App类buind()方法
# 		return PageLayoutWidget()  # 返回根控件
#
# if __name__ == "__main__":  # 程序入口
# 	PageApp().run()  # 启动应用程序


# --------------------------------- 2.6.3 ----------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

# 与kv文件不在同一个目录,因此先把kv文件导入
from kivy.lang import Builder
Builder.load_file('./kvs/page.kv')

from kivy.app import App  # 导入kivy的App类, App类是所有kivy应用的基类
from kivy.uix.pagelayout import PageLayout  # 引入布局

class PageLayoutWidget(PageLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)
		

class PageApp(App):  # 继承App类
	# 实现App类的build()方法, 继承自App类
	def build(self):
		return PageLayoutWidget()  # 返回根控件
	

if __name__ == "__main__":  # 程序入口
	PageApp().run()   # 启动应用程序