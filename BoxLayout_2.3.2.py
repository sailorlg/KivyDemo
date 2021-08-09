import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'


from kivy.app import App  # 导入kivy的App类, 它是所有kivy应用的基类
from kivy.uix.button import Button  # 引入控件
from kivy.uix.boxlayout import BoxLayout  # 引入布局
from kivy.graphics import Rectangle, Color

class BoxLayoutWidget(BoxLayout):  # 布局类
	def __init__(self, **kwargs):  # 初始化
		super().__init__(**kwargs)

		# 设置背景颜色
		with self.canvas:
			Color(1, 1, 1, 1)
			
			self.rect = Rectangle(pos=self.pos, size=self.size)
			self.bind(pos=self.update_rect, size=self.update_rect)
			
		# 添加两个按钮
		self.add_widget(Button(text='Hello'))
		self.add_widget(Button(text='Boxlayout'))
		
	def update_rect(self, *args):
		"""
		设置背景尺寸, 可忽略
		:param args:
		:return:
		"""
		self.rect.pos = self.pos
		self.rect.size = self.size
		

class BoxApp(App):  # 继承App类
	def build(self):  # 实现App类的build()方法
		return BoxLayoutWidget()  # 返回根控件
	

if __name__ == "__main__":  # 程序入口
	BoxApp().run()