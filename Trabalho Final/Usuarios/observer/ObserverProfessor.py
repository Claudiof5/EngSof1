from Usuarios.observer.iObserver import iObserver
from typing import List, Dict

class ObserverProfessor(iObserver):

    def __init__(self) -> None:
        self._notificacoes: List[Dict] = []

    def update(self, notificacao) -> None:
        self._notificacoes.append(notificacao)

    @property
    def numero_notificacoes(self) -> int:
        return len(self._notificacoes)

    

