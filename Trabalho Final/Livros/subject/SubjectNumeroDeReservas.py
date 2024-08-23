from Livros.subject.iSubject import *
from datetime import datetime

class SubjectNumeroDeReservas(iSubject):
    
    def __init__(self, codigo_livro : int) -> None:
        super().__init__()
        self._numeroReservas : int = 0
        self._codigo_livro : int = codigo_livro

    def attach(self, observer: iObserver) -> None:
        self._observers.add(observer)    
    
    def detach(self, observer: iObserver) -> None:
        self._observers.remove(observer)
    
    def object_of_interest(self, codigo_livro : int ) -> dict:
        return {"codigo do livro": codigo_livro ,"numero de Reservas": self._numeroReservas, "horario": datetime.now()}

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self.object_of_interest(self._codigo_livro ))

    def update_numero_reservas(self, numero_de_reservas) -> None:
        self._numeroReservas = numero_de_reservas
        if self._numeroReservas >= 2:
            self.notify()