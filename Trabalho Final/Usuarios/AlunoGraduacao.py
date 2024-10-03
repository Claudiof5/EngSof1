from Usuarios.iAluno import *

class AlunoGraduacao(iAluno):

    limiteDeLivrosMaximo = 3
    diasDeEmprestimoMaximo = 3
    
    def __init__(self, nome :str, codigoIdentificador:int) -> None:
        super().__init__(nome, codigoIdentificador)
    


