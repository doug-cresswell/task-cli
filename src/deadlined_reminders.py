from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        required_methods = ("__iter__", "is_due")
        if not all(attr_in_hierarchy(attr)) for attr in required_methods:
            return NotImplemented

        return True


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])
