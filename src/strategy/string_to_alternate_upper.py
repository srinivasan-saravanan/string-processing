from src.string_processing import StringProcessing


class StringToAlternateUpper(StringProcessing):

    def __init__(self, word):
        self.word = word

    def process_string(self):
        s = [ch.lower() if i % 2 == 0 else ch.upper() for i, ch in enumerate(self.word)]
        formatted_text = "".join(s)
        self.render_output(formatted_text)
        return formatted_text

    def render_output(self, output):
        print(output)
