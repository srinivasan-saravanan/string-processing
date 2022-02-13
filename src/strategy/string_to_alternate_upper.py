from string_processing import StringProcessing

class StringToAlternateUpper(StringProcessing):

    def __init__(self, word):
        self.word = word

    def process_string(self):
        s = [ch.lower() if i % 2 == 0 else ch.upper() for i, ch in enumerate(self.word)]
        self.render_output("".join(s))

    def render_output(self, output):
        print(output)
