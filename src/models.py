from enum import Enum

class StringProcessingMethods(Enum):
    to_upper = 'to_upper'
    to_alternate_upper = 'to_alternate_upper'
    create_csv = 'create_csv'

    def __str__(self):
        return self.value
