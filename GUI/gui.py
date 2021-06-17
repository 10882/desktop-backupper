import kivy
import threading
import pymsgbox


import core
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.config import Config


def gui_main():
    class DBApp(App):
        def build(self):
            
            Config.set('graphics', 'width', 1280)
            Config.set('graphics', 'height', 720)
            Config.write()

            main = FloatLayout(size = (1280, 720))

            main.add_widget(Image(
                pos = (0, 0),
                source = 'GUI\\bg.jpg',
                size = (1280, 720)
            ))
        
            disk_lay = FloatLayout(
                size = (800, 300),
                pos = (0, 300)
            )

            disks = core.get_disk()
            xl = 0

            for name in disks:
            
                disk_lay.add_widget(Button(
                    pos = (xl, 400),
                    on_press = self.st_copy,
                    text = name,
                    size_hint = (.1, .05)
                ))
                xl += 150
            main.add_widget(disk_lay)

            main.add_widget(Label(
                font_size = 20,
                text = 'Select disk',
                size_hint = (.1, .06),
                pos = (250, 500)
            ))

            main.add_widget(Label(
                font_size = 20,
                text = 'ZIP',
                size_hint = (.1, .06),
                pos = (320, 170)
            ))


            main.add_widget(Label(
                font_size = 20,
                text = '',
                size_hint = (.1, .06),
                pos = (420, 550)         
            ))

            main.add_widget(Switch(
                active = True,
                pos = (350, 100),
                size_hint = (.1, .06)
            ))
            return(main)

        def st_copy(self, instance):
            zip = self.root.children[0].active
            self.threadcopy = threading.Thread(target = core.backup, args = (instance.text, zip))
            self.threadcopy.start()
            
            check_copy = threading.Thread(target= self.check_copy)
            check_copy.start()
            self.root.children[1].text = "Идет копирование, не закрывайте программу."

        def check_copy(self):
            while self.threadcopy.is_alive() == True:
                pass
            self.root.children[1].text = ''
            pymsgbox.alert(text = 'Копирование завершено. Вы можете закрыть программу.', title= 'Копирование завершено')



    DBApp().run()

    
if __name__ == '__main__':
    gui_main()