import pytest
from src.app import StringToUpper, StringToAlternateUpper, CreateCSV


class TestStringToUpper(object):

    @pytest.mark.parametrize("word, expected", [("hello world", "HELLO WORLD")])
    @pytest.mark.process_string
    def test_process_string(self, word, expected):
        result = StringToUpper(word).process_string()
        assert result == expected


class TestStringToAlternateUpper(object):

    @pytest.mark.parametrize("word, expected", [("hello world", "HELLO WORLD")])
    @pytest.mark.process_string
    def test_process_string(self, word, expected):
        result = StringToAlternateUpper(word).process_string()
        assert result == expected
