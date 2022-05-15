from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
import logging

class ZoneMeowWidget(Widget):
    def __init__(self, **kwargs):
        super(TreeWidget, self).__init__(**kwargs)

        tv = TreeView(root_options=dict(text='Tree One'),
                      hide_root=False,
                      indent_level=4)
                      
        self.add_widget(tv)


class MeowMain(Widget):
    
    widthLabel = ObjectProperty(None)
    def update(self, dt):
        #self.width = self.get_parent_window().height
        #logging.info(self.width)
        pass

class MeowApp(App):
    def build(self):
        self.title = "ParseMeow"
        self.icon = "parsemeow.png"
        window = Window
        layout = GridLayout(cols=2)
        self.tv = TreeView()
        self.tv.add_node(TreeViewLabel(text = "kittens"))
        layout.add_widget(self.tv)
        mainWidget = MeowMain()
        layout.add_widget(mainWidget)
        
        
        Clock.schedule_interval(mainWidget.update, 1.0/60.0)
        return layout

if __name__ == '__main__':
    logging.info(help(App))
    MeowApp().run()