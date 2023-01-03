from turtle import pos
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color, Canvas

import random

COLORS = {
'Black':(0,0,0),
'White':(255,255,255),
'Red':(255,0,0),
'Lime':(0,255,0),
'Blue':(0,0,255),
'Yellow':(255,255,0),
'Cyan':(0,255,255),
'Magenta':(255,0,255),
'Silver':(192,192,192),
'Gray':(128,128,128),
'Maroon':(128,0,0),
'Olive':(128,128,0),
'Green':(0,128,0),
'Purple':(128,0,128),
'Teal':(0,128,128),
'Navy':(0,0,128)
  }
CARROT = r'''||| | |||
\\\|///
\\\|///
 -------
|       |
|       |
|       |
|       |
|       |
\      /
 \    /
  \_/'''

class Player(Widget):
    
    def __init__(self, dx , dy, color, name, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.layout = GridLayout(rows=2)
        with self.layout.canvas:
            Color(color[0], color[1], color[2])
            Rectangle(pos=(self.x, self.y),size=(250,250))
            """ 
            self.layout.add_widget(Button(text=name, font_size=dx/10)) """
        
        

# Builds the app
class BlackBoxApp(App):
     
    def get_player_block(self, player,color, layout):
        def NameEntered(instance):
            layoutPlayer.children[2].text = f"{instance.text}'s Box"
            layoutPlayer.remove_widget(instance)
            layoutPlayer.add_widget(Label(text=instance.text,size_hint=(.4, .4),
                    pos_hint={'x':.3, 'y':.1}, font_size='20sp'), index=0)
            dropDownButton.disabled = False
            if self.gameState == 1 or self.gameState == 2:
                self.gameState += player
            else:
                self.gameState = player
            if self.gameState == 3:
                layout.children[1].children[0].text = "Choose Colors (2)!!!"
            
            
        def select_color(self, x):
            layoutPlayer.children[2].background_color = COLORS[x]
            layoutPlayer.children[2].text = f"{layoutPlayer.children[2].text[0:-3]}{x} Box"
            
            if layout.children[1].children[0].text == "Choose Colors (1)!!!":
                layout.children[1].children[2].disabled = False
                layout.children[1].children[0].text = ''  
            elif layout.children[1].children[0].text == "Choose Colors (2)!!!":
                layout.children[1].children[0].text = "Choose Colors (1)!!!"
                
            dropDown.disabled = True
            dropDownButton.disabled = True
        
        def hide_block(dt):
            _ = layoutPlayer.children[2]
            layoutPlayer.remove_widget(_)
            Clock.schedule_once(lambda dt: layoutPlayer.add_widget(_), 0.5)
            layoutPlayer.children[1].disabled = True
            layout.children[1].children[1].disabled = False
            layout.children[1].children[2].disabled = False
            layout.children[1].children[2].text = 'Show Prizes'
            layout.children[1].children[0].text = layout.children[0 if player == 1 else 2].children[0].text + " May elect to swap the boxes!!!"
             
        layoutPlayer=FloatLayout()
        dropDown = DropDown()
        for colors in COLORS:
            btn = Button(text=colors, background_color=(COLORS[colors][0], COLORS[colors][1], COLORS[colors][2]), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropDown.select(btn.text))
            dropDown.add_widget(btn)
        dropDownButton = Button(text="Choose a color", size_hint=(.3,.1), pos_hint={'x':.35,'y':.85})
        dropDownButton.bind(on_release=dropDown.open)
        dropDown.bind(on_select=select_color)
        dropDownButton.disabled = True
        layoutPlayer.add_widget(dropDownButton)
        
        layoutPlayer.add_widget(Button(text=f"{self.carrot[player-1]}",size_hint=(.5, .4),
                pos_hint={'x':.25, 'y':.4}, color=(0, 0, 0), font_size="20sp", background_color=(255,116,0)))
        layoutPlayer.add_widget(Button(text=f"Player {player}'s Box" ,size_hint=(.5, .4),
                pos_hint={'x':.25, 'y':.4}, background_color=color, color=(255,255,255)))
        
        text = TextInput(hint_text=f"Player {player} Enter Name: ",size_hint=(.4, .05),
                pos_hint={'x':.3, 'y':.2}, font_size='20sp', multiline=False, hint_text_color=(0,0,0))
        layoutPlayer.add_widget(text)
        text.bind(on_text_validate=NameEntered)
        layoutPlayer.add_widget(Button(text=f"Check Box", on_press=hide_block ,size_hint=(.3, .05),
                pos_hint={'x':.35, 'y':.1}, color=(0,0,0), background_color=(255,255,255)))
        
        return layoutPlayer

    
        
    def game_state(self, layout):
        
        def set_start(dt):
            
            if dt.text == "Show Prizes":
                layoutGameManager.children[1].disabled = True
                dt.disabled = True
                p1Box = [val for val in layout.children[0].children if "'s" in val.text][0]
                p2Box = [val for val in layout.children[2].children if "'s" in val.text][0]
                p1Carrot = [val.text for val in layout.children[0].children if val.text == "" or val.text == CARROT][0]
                p1Name = [val.text for val in layout.children[0].children if val.text == p1Box.text[0: p1Box.text.index("'s")]][0]
                p2Name = [val.text for val in layout.children[2].children if val.text == p2Box.text[0: p2Box.text.index("'s")]][0]
                layout.children[0].remove_widget(p1Box)
                layout.children[2].remove_widget(p2Box)
                layoutGameManager.children[0].text = p1Name + " Wins!!!!!" if p1Carrot == CARROT else p2Name + " Wins!!!!!"
                layoutGameManager.children[0].text += '\n\nThank you for playing!!!!!'
            else:
                self.gameState = 'Started'
                randomNum = random.choice([0,2,0,2,0,2,0,2,0,2])
                layoutGameManager.children[0].text = layout.children[randomNum].children[0].text + ' Click the check box below to reveal your prize, once the other player has looked away.'
                layout.children[randomNum].children[1].disabled = False
            layoutGameManager.children[2].disabled = True
        
        def swap_boxes(dt):
            dt.disabled = True
            layoutGameManager.children[0].text = 'Boxes swapped...Check Winner below!!!'
            
            
            p1BoxName = [val.text for val in layout.children[0].children if "'s" in val.text][0]
            p2BoxName = [val.text for val in layout.children[2].children if "'s" in val.text][0]
            p1Name = [val.text for val in layout.children[0].children if val.text == p1BoxName[0: p1BoxName.index("'s")]][0]
            p2Name = [val.text for val in layout.children[2].children if val.text == p2BoxName[0: p2BoxName.index("'s")]][0]
            
            p1Box = [val for val in layout.children[0].children if "'s" in val.text][0]
            p1Box.text = p2Name + "'s New Box"
            p2Box = [val for val in layout.children[2].children if "'s" in val.text][0]
            p2Box.text = p1Name + "'s New Box"
            
            p1Label = [val for val in layout.children[0].children if val.text == p1Name][0]
            p2Label = [val for val in layout.children[2].children if val.text == p2Name][0]
            p1Label.text = p2Name
            p2Label.text = p1Name
            
            self.gameState = 'Swap'
            
        layoutGameManager = FloatLayout(size_hint_max_x=300)
        swapButton = Button(text="Swap", size_hint=(1, .1), pos_hint={'x': .1, 'y': .05}, on_press=swap_boxes)
        restartButton = Button(text='Play', size_hint=(.5, .1), pos_hint={'x': .3, 'y': .5}, on_press=set_start)
        layoutGameManager.add_widget(restartButton)
        layoutGameManager.add_widget(swapButton)
        layoutGameManager.add_widget(Label(text="Enter names below!!!", size_hint=(.5, .5), pos_hint={'x': .2, 'y': .5}))
        if self.gameState != 'Swap':
            layoutGameManager.children[1].disabled = True
            layoutGameManager.children[2].disabled = True
            
        return layoutGameManager
    
    def build(self):
        self.gameState = "Play"
        self.carrot = []
        if random.randint(0,100) % 2 == 0:
            self.carrot.append(CARROT) 
        else:
            self.carrot.append('') 
        
        if self.carrot[0] == '':
            self.carrot.append(CARROT) 
        else:
            self.carrot.append('')
        random.shuffle(self.carrot) 
        layout = GridLayout(cols=3)
        layout.add_widget(self.get_player_block(1, (255,255,255), layout))
        layout.add_widget(self.game_state(layout))
        layout.add_widget(self.get_player_block(2, (255,255,255), layout))
        layout.children[0].children[0].disabled = True
        layout.children[2].children[0].disabled = True
          
        """ layout.add_widget(Player(dx=250, dy=350, color=(255,0,0), name="Player 1"))
        layout.add_widget(Player(dx=950, dy=350, color=(0,0,255), name="Player 2")) """
        return layout
    
def Main():
    BlackBoxApp().run()

if __name__ == '__main__':
    Main()