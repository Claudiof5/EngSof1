from datetime import datetime 


class Comentario:
    def __init__(self, escritorId:str, texto:str, comentarioId:str) -> None:
        self.escritor     : str = escritorId
        self.texto        : str = texto
        self.dataCriacao  : str = datetime.now().strftime("%x")
        self.comentarioId : str = comentarioId

    