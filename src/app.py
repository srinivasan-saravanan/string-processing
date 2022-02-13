import argparse

from factory import FactoryClass
from models import StringProcessingMethods


def execute(word, action_method):
    obj = FactoryClass()
    cls = obj.get_strategy_class(action_method)
    cls(word).process_string()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, nargs=1, help="Enter a String to do the Operation")
    parser.add_argument("--operation", type=StringProcessingMethods, choices=list(StringProcessingMethods), nargs=1,
                        help="Enter the string manipulation operation to perform")
    args = parser.parse_args()
    execute(args.input[0], args.operation[0])
