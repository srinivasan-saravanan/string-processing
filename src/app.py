import argparse
from factory import FactoryClass
from models import StringProcessingMethods

def execute(word, actionMethod):
    obj = FactoryClass()
    cls = obj.get_strategy_class(actionMethod)
    cls(word).process_string()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str,nargs=1, help="Enter a String to do the Operation")
    parser.add_argument("--operation", type=StringProcessingMethods, choices=list(StringProcessingMethods),nargs=1, help="Enter the string manipulation operation to perform")
    args = parser.parse_args()
    execute(args.input[0], args.operation[0])
