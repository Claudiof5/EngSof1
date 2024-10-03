from Usuarios.iAluno import *

class AlunoPosGraduacao(iAluno):

    limiteDeLivrosMaximo = 4
    diasDeEmprestimoMaximo = 5
    
    def __init__(self, nome :str, codigoIdentificador:int) -> None:
        super().__init__(nome, codigoIdentificador)
    


