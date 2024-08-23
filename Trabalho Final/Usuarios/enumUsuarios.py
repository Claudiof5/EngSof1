from enum import Enum
from Usuarios.AlunoGraduacao import AlunoGraduacao
from Usuarios.AlunoPosGraduacao import AlunoPosGraduacao
from Usuarios.Professor import Professor   

class enumUsuarios(Enum):
    ALUNOGRADUACAO = AlunoGraduacao
    ALUNOPOSGRADUACAO = AlunoPosGraduacao
    PROFESSOR = Professor
