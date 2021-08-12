# # ------------------------------- 1 ---------------------------
# import os
#
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.graphics import Rectangle, Color
# from kivy.graphics.instructions import InstructionGroup
#
#
# class RelativeLayoutWidget(RelativeLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		blue = InstructionGroup()
# 		blue.add(Color(0, 0, 1, 0.2))
# 		blue.add(Rectangle(pos=self.pos, size=(300, 300)))
# 		self.canvas.add(blue)
#
# 		green = InstructionGroup()
# 		green.add(Color(0, 1, 0, 0.4))
# 		green.add(Rectangle(pos=(300, 300), size=(300, 300)))
# 		self.canvas.add(green)
#
#
# class CanvasApp(App):
# 	def build(self):
# 		return RelativeLayoutWidget()
#
#
# if __name__ == "__main__":
# 	CanvasApp().run()


# # ------------------------------- 2 ---------------------------
# import os
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
#
# from kivy.app import App
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.graphics import Rectangle, Color
# from kivy.graphics.instructions import InstructionGroup
#
#
# class RelativeLayoutWidget(RelativeLayout):
# 	def __init__(self, **kwargs):
# 		super().__init__(**kwargs)
#
# 		with self.canvas:
# 			blue = InstructionGroup()
# 			blue.add(Color(0, 0, 1, 0.2))
# 			blue.add(Rectangle(pos=self.pos, size=(300, 300)))
# 			self.canvas.add(blue)
#
# 			green = InstructionGroup()
# 			green.add(Color(0, 1, 0, 0.4))
# 			green.add(Rectangle(pos=(300, 300), size=(300, 300)))
# 			self.canvas.add(green)
#
#
# class CanvasApp(App):
# 	def build(self):
# 		return RelativeLayoutWidget()
#
#
# if __name__ == "__main__":
# 	CanvasApp().run()



# ------------------------------- 3 ---------------------------
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

from kivy.lang import Builder
Builder.load_file('./kvs/canvas.kv')


from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color
from kivy.graphics.instructions import InstructionGroup



class RelativeLayoutWidget(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class CanvasApp(App):
	def build(self):
		return RelativeLayoutWidget()


if __name__ == "__main__":
	CanvasApp().run()