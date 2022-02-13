import pytest
from src.strategy.string_to_upper import StringToUpper

class TestStringToUpper(object):

    @pytest.mark.parametrize("word, expected", [("hello world", "HELLO WORLD")])
    @pytest.mark.process_string
    def test_process_string(self, word, expected):
        result = StringToUpper(word).process_string()
        assert result == expected
        