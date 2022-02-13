import pytest
from src.strategy.string_to_alternate_upper import StringToAlternateUpper

class TestStringToAlternateUpper(object):

    @pytest.mark.parametrize("word, expected", [("hello world", "hElLo wOrLd")])
    @pytest.mark.process_string
    def test_process_string(self, word, expected):
        result = StringToAlternateUpper(word).process_string()
        assert result == expected
