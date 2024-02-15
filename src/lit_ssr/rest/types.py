from abc import ABC, abstractmethod


class Client(ABC):

    @abstractmethod
    def method1(self):
        """
        Abstract method 1.
        """
        pass

    @abstractmethod
    def method2(self):
        """
        Abstract method 2.
        """
        pass
