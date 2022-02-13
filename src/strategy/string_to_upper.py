from string_processing import StringProcessing

class StringToUpper(StringProcessing):

    def __init__(self, word):
        self.word = word

    def process_string(self):
        s = self.word.upper()
        self.render_output(s)

    def render_output(self, output):
        print(output)