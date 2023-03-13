from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.menu import MDDropdownMenu
import mysql.connector as ms
from dotenv import load_dotenv
import os

load_dotenv()
USER=os.getenv('USER')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')

mydb = ms.connect(host=HOST, user=USER, database=DATABASE, password=PASSWORD, port=PORT)
print(mydb)

#Set pre defined window size
Window.size = (600, 600)

class WindowManager(ScreenManager):
    pass

class Park_n_Go(MDApp):
    def build(self):
        self.screen = Builder.load_file("./Components/main.kv")
        menu_items=[{"text": "Light Vehicle", "viewclass": "OneLineListItem", "on_release": lambda text="Light":self.display_text(text)}, 
                    {"text": "Heavy Vehicle", "viewclass": "OneLineListItem", "on_release": lambda text="Heavy":self.display_text(text)},
                    {"text":"Bicycle", "viewclass": "OneLineListItem", "on_release": lambda text="cycle":self.display_text(text)},
                    {"text":"Three wheeler", "viewclass": "OneLineListItem", "on_release": lambda text="3-wheel":self.display_text(text)}]
        self.menu = MDDropdownMenu(
            caller=self.screen.get_screen('mainscreen').ids.drop,
            items=menu_items,
            width_mult=4,
        )

        return self.screen
    
    def display_text(self,text):
        self.menu.dismiss()
        print(text)

    def hello(self):
        cur = mydb.cursor()
        cur.execute("select * from admin")
        res = cur.fetchall()
        print(res)
        print(self.screen.get_screen('login').ids.text1.text)
        print(self.screen.get_screen('login').ids.passw.text)

    def show_time_picker(self):
        '''Open time picker dialog.'''
        time_dialog = MDTimePicker()
        time_dialog.open()
        time_dialog.bind(on_save=self.get_time)

    def saveTodb(self):
        print("Data saved to database")

    def get_time(self, instance, time):
        print(time)

if __name__=="__main__":
    LabelBase.register(name="MPoppins", fn_regular="assets/fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="assets/fonts/Poppins-SemiBold.ttf")
Park_n_Go().run()