import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.swipetodelete import SwipeBehavior

kivy.require('1.9.0')

# Things to demo
# 1. Swipe transitions
# 2. Effect of different layouts
# 3. Properties
# 4. On Android, not reloading after you move off
# 5. Effective use of Inheritence + Composition in kv
# 6. Borders on labels
# 7. C8lours of buttons
# 8. Font sizes

class SimpleBackground(Widget):
  bg_rgba = ListProperty((1,1,0.8,1))
  fg_rgba = ListProperty((0,1,0.8,1))
  border_width = 6

class FirstScreen(Screen):
  pass

class Layout1Screen(SwipeBehavior, Screen):
  def on_touch_down(self, touch):
    if self.collide_point(touch.x, touch.y):
      self.move_to = self.x,self.y
      print "L1 down %d,%d " % (self.x,self.y)
      return super(Layout1Screen, self).on_touch_down(touch)
  
  def on_touch_move(self, touch):
    if self.collide_point(touch.x, touch.y):
      print "L1 move %d,%d " % (self.x,self.y)
      self.reduce_opacity()
      return super(Layout1Screen, self).on_touch_move(touch)
  
  def on_touch_up(self, touch):
    if self.collide_point(touch.x, touch.y):
      print "L1 up %d,%d" % (self.x,self.y)
      self.check_for_left()
      self.check_for_right()
      return super(Layout1Screen, self).on_touch_up(touch)

class LayoutDemoApp(App):

#   def __init__(self, **kwargs):
#        super(App, self).__init__(**kwargs)
#        print "App.__init__"

  def first_transition(self, dt):
    print "on_first_transition"
    self.sm.current = 'layout1'

  def on_start(self):
    print "on_start"

  def on_stop(self):
    print "on_stop"

  def build(self):
    print "build"
    self.title = 'Layouts Demo'
    sm = ScreenManager()
    sm.add_widget(FirstScreen(name='layout0'))
    sm.add_widget(Layout1Screen(name='layout1'))
    Clock.schedule_once(self.first_transition, 2)
    self.sm = sm
    return sm

if __name__ == '__main__':
  print "main"
  LayoutDemoApp().run()
