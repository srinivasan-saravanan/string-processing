import pytest
import os
from src.strategy.create_csv import CreateCSV


class TestCreateCSV(object):
    @pytest.mark.parametrize("word, file_path", [("hello world", "output.csv")])
    @pytest.mark.process_string
    def test_process_string(self, word, file_path):
        CreateCSV(word).process_string()
        if not os.path.isfile(file_path):
            raise Exception("File not exists")

