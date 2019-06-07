import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

Window.clearcolor = .0,127,255,1
Window.clearcolor = get_color_from_hex('#FFFFFF')

kv ='''

#:import c kivy.utils.get_color_from_hex

<fv@FloatLayout>:

    Label:
        text:'ESTACIONAPP'
        bold: True
        pos_hint:{'center_x':.5,'center_y':.9}
    
    TextInput:
        text:'Nome'
        size_hint:.8,.05
        pos_hint:{'center_x':.5,'center_y':.7}
    TextInput:
        text:'Email'
        size_hint:.8,.05
        pos_hint:{'center_x':.5,'center_y':.6}
    TextInput:
        text:'Password'
        size_hint:.8,.05
        pos_hint:{'center_x':.5,'center_y':.5}
    TextInput:
        text:'Confirm Paswword'
        size_hint:.8,.05
        pos_hint:{'center_x':.5,'center_y':.4} 
    Button:
        markup:True
        text:'Confirm'
        text_color:0,0,0,1
        size_hint:.4,.05
        pos_hint:{'center_x':.5,'center_y':.2}
        canvas.before:
            Color:
                rgba:c('#FFFFFF')
            Rectangle:
                pos: self.pos
                size: self.size
            
    Label:
        text:'Privacy policy'
        pos_hint:{'center_x':.4,'center_y':.1} 
    Label:
        text:'Privacy policy'
        pos_hint:{'center_x':.6,'center_y':.1} 
fv:        
        
    
'''

class pyy(App):
    def build(self):
        return Builder.load_string(kv)

janela = pyy()
janela.run()







