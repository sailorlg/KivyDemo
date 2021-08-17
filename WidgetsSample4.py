
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

# ------------------------- 5 ------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/labelrefer.kv')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class LableBoxLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	# 未使用到self, 建议设置为静态方法
	@staticmethod
	def print_it(*args):
		print("print_it is running~!")


class LabelReferApp(App):
	def build(self):
		return LableBoxLayout()


if __name__ == "__main__":
	LabelReferApp().run()