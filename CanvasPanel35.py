import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/paint35.kv')

from kivy.app import App
from kivy.graphics import Line, Color  # 引入绘图
from kivy.uix.widget import Widget  # 引入控件
from kivy.uix.togglebutton import ToggleButton
from kivy.utils import get_color_from_hex

class DrawCanvasWidget(Widget):  # 布局类
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		# 设置默认颜色
		# self.canvas.add(Color(rgb=[0, 0, 0]))
		self.change_color("#000000")
		
		self.line_width = 2
		
	
	def on_touch_down(self, touch):
		"""触摸显示轨迹"""
		if Widget.on_touch_down(self, touch):
			return
		with self.canvas:
			touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=self.line_width)
			
	def on_touch_move(self, touch):
		"""连线"""
		if "current_line" in touch.ud:
			touch.ud["current_line"].points += (touch.x, touch.y)
		
	def change_color(self, new_color):
		"""调色"""
		self.canvas.add(Color(*new_color))
		


class Paint35App(App):
	def build(self):
		self.draw_canvas_widget = DrawCanvasWidget()
		return self.draw_canvas_widget
	
if __name__ == "__main__":
	Paint35App().run()
