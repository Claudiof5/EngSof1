from datetime import datetime 

class Comentario:
    def __init__(self, escritorId:str, texto:str, comentarioId:str) -> None:
        self.escritor = escritorId
        self.texto = texto
        self.dataCriacao = datetime.now().strftime("%x")
        self.comentarioId = comentarioId

    