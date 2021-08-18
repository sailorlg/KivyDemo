# # ------------------------- 7 ------------------------
# import os
#
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.lang import Builder
# Builder.load_file('./kvs/ux52.kv')
#
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.dropdown import DropDown
# from kivy.uix.button import Button
# from kivy.base import runTouchApp
#
#
# class CustomDropDown(DropDown):
# 	# """在kv文件中添加下拉菜单"""
# 	# def __init__(self, **kwargs):
# 	# 	super().__init__(**kwargs)
# 	# 	self.auto_dismiss = True
# 	pass
#
# class UXWidget(GridLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		dropdown = CustomDropDown()
# 		# 单击该按钮触发下拉框
# 		main_button = Button(text="ClickMe", size_hint=(0.2, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
# 		main_button.bind(on_release=dropdown.open)  # 绑定事件
# 		# 绑定选中的回调方法, 把mian_button的text属性设置为转递过来的"X"
# 		dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
#
# 		# self.add_widget(main_button)
# 		# 创建一个MTWindow并将窗口小部件作为根窗口的小部件添加到窗口中
# 		runTouchApp(main_button)
#
#
#
# 	def bubble_btn_clicked(self):
# 		print("bubble_btn_clicked is RUNNING")
#
# 	def dropdown_btn(c_widget, value):
# 		print("SELECTED ITEM == " + str(c_widget) + " \nVALUE ==" + value)
# 		# print(args)
#
#
#
#
# class Ux52App(App):
# 	def build(self):
# 		return UXWidget()
#
#
# if __name__ == "__main__":
# 	Ux52App().run()


#
#
# # ------------------------- 7 ------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.lang import Builder
# Builder.load_file('./kvs/ux53.kv')
#
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.dropdown import DropDown
# from kivy.uix.button import Button
# from kivy.base import runTouchApp
# from kivy.uix.popup import Popup
#
#
#
# class PopupBox(Popup):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
#
# class Ux53App(App):
# 	def build(self):
# 		return PopupBox()
#
#
# if __name__ == "__main__":
# 	Ux53App().run()





# ------------------------- 7 ------------------------
import os

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder

Builder.load_file('./kvs/ux53.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.popup import Popup


class PopupBox(Popup):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class Ux53App(App):
	def build(self):
		return PopupBox()


if __name__ == "__main__":
	Ux53App().run()