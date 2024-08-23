from abc import ABC, abstractmethod


class iObserver(ABC):
    
        @abstractmethod
        def update(self, subject) -> None:
            pass
