from abc import ABC, abstractmethod
from comando.parametro.Parametro import Parametro

class iComando(ABC):

    @abstractmethod
    def executar(self, parametro: Parametro):
        pass