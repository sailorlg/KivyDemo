# ------------------------- 7 ------------------------
import os

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/ux5.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown


class CustomDropDown(DropDown):
	"""在kv文件中添加下拉菜单"""
	pass

class UXWidget(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	
	def bubble_btn_clicked(self):
		print("bubble_btn_clicked is RUNNING")
		
	def dropdown_btn(c_widget, value):
		print("SELECTED ITEM == " + str(c_widget) + " \nVALUE ==" + value)
		# print(args)

class Ux5App(App):
	def build(self):
		return UXWidget()
	

if __name__ == "__main__":
	Ux5App().run()