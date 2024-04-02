from datetime import datetime 


class Comentario:
    def __init__(self, escritorId:str, texto:str, comentarioId:str) -> None:
        self.escritor     : str = escritorId
    
        self.texto        : str = texto
        self.dataCriacao  : str = datetime.now().strftime("%x")
        self.comentarioId : str = comentarioId

    def printaComentario(self):
        aux = ("~~"*20)+ "texto" +("~~"*20)
        print(f"escritor: {self.escritor}".center(100))
        print(aux.center(100))
        print(f" {self.texto}".center(100))
        print("~~texto~~"*10)