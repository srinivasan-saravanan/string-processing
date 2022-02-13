import abc

class StringProcessing(abc.ABC):

    @abc.abstractmethod
    def process_string(self):
        pass

    @abc.abstractmethod
    def render_output(self, output):
        pass
