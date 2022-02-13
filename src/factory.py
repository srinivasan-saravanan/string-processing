from models import StringProcessingMethods
from strategy.create_csv import CreateCSV
from strategy.string_to_alternate_upper import StringToAlternateUpper
from strategy.string_to_upper import StringToUpper

class FactoryClass(object):

    def __init__(self):
        self.class_mapping = {
            StringProcessingMethods.to_upper: StringToUpper,
            StringProcessingMethods.to_alternate_upper: StringToAlternateUpper,
            StringProcessingMethods.create_csv: CreateCSV
        }

    def get_strategy_class(self, operation):
        return self.class_mapping[operation]
