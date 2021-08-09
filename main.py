import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

# # 原始的main.py文件内容
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/




# 导入kivy的App类,它是所有kivy应用的基类
from kivy.app import App

# kivy内置了丰富的控件(widget),如
# 按钮(button), 复选框(checkbox), 标签(label), 输入框(textinput), 滚动容器(scrollable_container)等
from kivy.uix.button import Button

# 引入BoxLayout布局
# from kivy.uix.boxlayout import BoxLayout

from kivy.uix.floatlayout import FloatLayout  # 引入布局

from kivy.graphics import Rectangle, Color



# class IndexPage(BoxLayout):
#     # 初始化
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # 添加一个按钮
#         # self.join = Button(text="Hellow World")
#         # # 将按钮添加到页面控件中
#         # self.add_widget(self.join)
#
# # 从App类中继承了kivy应用最基本的方法, 如创建窗口, 设置窗口大小和位置等
# class TestApp(App):
#     # 实现TestApp类的build()方法(继承自App类)
#     def build(self):
#         # build()方法返回的控件, 在kivy中, 称之为"根控件1"(root widget)
#         # kivy将自动缩放跟控件, 让她填满整个窗口
#         return IndexPage()
#
    

# 2.2.2

class FloatLayoutApp(App):  # 继承App类
    
    def build(self):  # 实现App类的build()方法
        
        def update_rect(layout, * args):
            """
            设计背景尺寸, 可忽略
            :param layout:
            :param args:
            :return:
            """
            layout.rect.pos = layout.pos
            layout.rect.size = layout.size
        
        float_layout = FloatLayout()
        
        # 设置背景颜色(可忽略)
        with float_layout.canvas:
            Color(1, 1, 1, 1)
            float_layout.rect = Rectangle(pos=float_layout.pos, size=float_layout.size)
            float_layout.bind(pos=update_rect, size=update_rect)
            
        # 在布局内的[300, 200]处添加一个0.3,0.3的按钮
        button = Button(text="Hello FloutLayout", size_hint=(0.3, 0.2), pos=(300, 200))
        
        # 将按钮添加到布局内
        float_layout.add_widget(button)
        
        # 返回布局
        return float_layout


# 当.py文件被直接运行时, if __name__ == "__main__"之下的代码块被运行
# 当.py文件以模块形式被导入时, if __name__ == "__main__"之下的代码块不被运行
if __name__ == "__main__":
    FloatLayoutApp().run()  # 启动应用容器

