import csv
from string_processing import StringProcessing

class CreateCSV(StringProcessing):

    def __init__(self, word):
        self.word = word

    def process_string(self):
        file_name = "output.csv"
        with open(file_name, "w") as f:
            w = csv.writer(f)
            w.writerow(list(self.word))
        self.render_output()

    def render_output(self, output=None):
        print("CSV created!")

