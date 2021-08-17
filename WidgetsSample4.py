
# # ------------------------- 1 ------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
#
# from kivy.lang import Builder
# Builder.load_file('./kvs/buttonsample.kv')
#
#
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
#
#
# class ButtonSampleWidget(BoxLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 	def press_button(self, arg):
# 		"""按下按钮触发事件的回调函数"""
# 		print("------press_button---------")
#
# 	def release_button(self, arg):
# 		"""按下按钮并释放触发事件的回调函数"""
# 		print("----------release_button--------------")
#
#
# class ButtonSampleApp(App):
# 	def build(self):
# 		self.root_canvas = ButtonSampleWidget()
# 		return self.root_canvas
#
#
# if __name__ == "__main__":
# 	ButtonSampleApp().run()


# # ------------------------- 2 ------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# # from kivy.lang import Builder
# # Builder.load_file('./kvs/labelrefer.kv')
#
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
#
# class LableBoxLayout(BoxLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		# 设置引用时, markup属性必须设置为真(True, 1, 等)
# 		# 将"LABEL"文本标记, 单击"LABEL"文本时会触发绑定的事件, 单机"HELLO"文本则不会
# 		label_ref = Label(text='HELLO [ref=label] LABEL [/ref] ', markup=True, color=(0.9, 0.2, 0.1, 1))
#
# 		# 绑定触发事件, 回调方法
# 		label_ref.bind(on_ref_press=self.print_it)
# 		self.add_widget(label_ref)
#
# 	# 未使用到self, 建议设置为静态方法
# 	@staticmethod
# 	def print_it(*args):
# 		print("print_it is running~!")
#
# class LabelRefApp(App):
# 	def build(self):
# 		return LableBoxLayout()
#
# if __name__ == "__main__":
# 	LabelRefApp().run()



# # ------------------------- 3 ------------------------
# import os
#
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# # from kivy.lang import Builder
# # Builder.load_file('./kvs/labelrefer.kv')
#
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
#
#
# class LableBoxLayout(BoxLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		# 设置引用时, markup属性必须设置为真(True, 1, 等)
# 		# 将"LABEL"文本标记, 单击"LABEL"文本时会触发绑定的事件, 单机"HELLO"文本则不会
# 		label_ref = Label(text='HELLO [ref=label] LABEL [/ref] ', markup=True, color=(0.9, 0.2, 0.1, 1))
#
# 		# 绑定触发事件, 回调方法
# 		label_ref.bind(on_ref_press=self.print_it)
# 		self.add_widget(label_ref)
#
# 	# 未使用到self, 建议设置为静态方法
# 	@staticmethod
# 	def print_it(*args):
# 		print("print_it is running~!")
#
#
# class LabelRefApp(App):
# 	def build(self):
# 		return LableBoxLayout()
#
#
# if __name__ == "__main__":
# 	LabelRefApp().run()


# # ------------------------- 6 ------------------------
# import os
#
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.lang import Builder
#
# Builder.load_file('./kvs/image4.kv')
#
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
#
#
# class ImageBoxLayout(BoxLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
#
# class Image4App(App):
# 	def build(self):
# 		return ImageBoxLayout()
#
#
# if __name__ == "__main__":
# 	Image4App().run()


# ------------------------- 7 ------------------------
import os

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/inputwidiget.kv')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class ImageBoxLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		# 通过ID获取到CheckBox部件并绑定方法
		self.ids.first_check_00.bind(active=self.on_checkbox_active)
		self.ids.first_check_01.bind(active=self.on_checkbox_active)
		self.ids.first_check_02.bind(active=self.on_checkbox_active)
		self.ids.second_check_02.bind(active=self.on_checkbox_active_test)
		
		self.i = 0
		
	@staticmethod
	def on_checkbox_active(checkbox, value):
		if value:
			print("The RadioButton", checkbox, " Is Actived; Value Is ", value)
		else:
			print("The RadioButton", checkbox, " Is IN-Actived; Value Is ", value)
			

	@staticmethod
	def on_checkbox_active_test(checkbox, value):
		if value:
			print("The CheckBox", checkbox, " Is Actived; Value Is ", value)
		else:
			print("The CheckBox", checkbox, " Is IN-Actived; Value Is ", value)
			
	def on_slider_event(slider, value):
		print("The CheckBox", slider, " Is Actived; Value Is ", value)
		
	def text_input_ref(self):
		print("---INPUT 001----")
		
	def clicked(self):
		# 每0.5秒调用update_bar()方法一次
		self.update_bar_trigger = Clock.schedule_interval(self.update_bar, 0.5)
		
	def update_bar(self, dt):
		if self.i <= 100:
			self.ids.process_bar.value += self.i
			self.i += 1
			self.update_bar_trigger()


class InputWidiget(App):
	def build(self):
		return ImageBoxLayout()


if __name__ == "__main__":
	InputWidiget().run()