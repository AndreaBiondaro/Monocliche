from abc import ABCMeta, abstractmethod

class AbstractAction(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass