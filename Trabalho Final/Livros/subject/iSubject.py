from abc import ABC, abstractmethod
from Usuarios.observer.iObserver import iObserver
from typing import Set

class iSubject(ABC):
    
    
    def __init__(self) -> None:
        self._observers: Set[iObserver] = set()

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def object_of_interest(self) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self.object_of_interest())