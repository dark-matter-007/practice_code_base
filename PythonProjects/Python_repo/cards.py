from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

Builder.load_string("""
<CardWidget>:
    orientation: 'vertical'
    size_hint: None, None
    size: '180dp', '220dp'
    canvas.before:
        Color:
            rgba: .4, .4, .4, 1 
        
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,20, 20, 20]

    Label:
        text: root.title
        halign: 'center'
        valign: 'middle'
        size_hint_y: None
        height: '40dp'
    Label:
        text: root.description
""")

class CardWidget(BoxLayout):
    title = StringProperty()
    description = StringProperty()
    image = StringProperty()

class SlidingCardsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        cards = Carousel(anim_move_duration = 0.6, loop = True )
        cards.size_hint_x = 0.3
        cards.pos_hint={'center_x': .5, 'center_y': .5}
        for i in range(1, 4):
            card = CardWidget(title='Card {}'.format(i), description='Description {}'.format(i),
                              image='card{}.png'.format(i))
            cards.add_widget(card)
            self.carousel = cards
        return cards

if __name__ == '__main__':
    SlidingCardsApp().run()