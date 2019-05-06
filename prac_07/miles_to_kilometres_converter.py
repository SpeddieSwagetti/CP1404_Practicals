"""CP1404/CP5632 Practical
Kivy GUI program to convert distance in miles to kilometres
Mitchell Marks
Started 06/05/2019"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometres(App):
    """kivy App for converting Miles to Kilometres"""
    def build(self):
        """build the kivy app from the kv file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres_converter.kv')
        return self.root

    def handle_calculation(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, increment):
        result = int(value) + int(increment)
        self.root.ids.input_number.text = str(result)


MilesToKilometres().run()
