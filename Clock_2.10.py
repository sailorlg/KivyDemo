
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from time import strftime

from kivy.lang import Builder
Builder.load_file('./kvs/clock.kv')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

class ClockBoxLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.timing_flag = False
		self.timing_seconds = 0
		self.on_start()
		
	def on_start(self):
		# 每0秒执行一次update_time()方法
		Clock.schedule_interval(self.update_time, 0)
	
	def update_time(self, nap):
		# # 通过id获取到time_label_id控件, 并设置text属性值
		# self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')

		if self.timing_flag:
			self.timing_seconds += nap  # 这里的秒不是整数, 也就是说, 不是整秒
		# print(str(self.timing_seconds))
			
		# 通过ID获取到time_label_id控件, 并设置text的属性
		self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')
		m, s = divmod(self.timing_seconds, 60)
		
		# 同上设置text值
		self.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s*100%100)))
		
	def start_or_stop(self):
		# 切换状态
		self.ids.start_stop_button_id.text = 'Start' if self.timing_flag else 'Stop'
		self.timing_flag = not self.timing_flag
		
	def reset_clock(self):
		"""重置时钟"""
		if self.timing_flag:
			self.ids.start_stop_button_id.text = 'START'
			self.timing_flag = False
		self.timing_seconds = 0
		
class ClockApp(App):
	def build(self):
		return ClockBoxLayout()
	
	
if __name__ == "__main__":
	# 设置页面背景
	Window.clearcolor = [0.8, 0.8, 0.8, 0.8]
	
	ClockApp().run()

	