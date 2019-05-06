"""CP1404/CP5632 Practical
Kivy GUI program to convert distance in miles to kilometres
Mitchell Marks
Started 06/05/2019"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometres(App):
    """kivy App for converting Miles to Kilometres"""
    kilometres = StringProperty()

    def build(self):
        """build the kivy app from the kv file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres_converter.kv')
        return self.root

    def handle_calculation(self, text):
        """ handle calculation (could be button press or other call), output miles to label widget """
        print("handle_calculation")
        miles = self.convert_input_to_float(text)
        self.miles_to_kilometres(miles)

    def handle_increment(self, text, increment):
        miles = self.convert_input_to_float(text) + increment
        self.root.ids.input_number.text = str(miles)

    def miles_to_kilometres(self, miles):
        print("final conversion from miles to kilometers")
        self.kilometres = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_input_to_float(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesToKilometres().run()
