from Usuarios.regrasEmprestimo.iRegrasEmprestimo import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Usuarios.Professor import Professor

class RegrasEmprestimoProfessor(iRegrasEmprestimo):

    def apto_a_emprestimo(self, livro :Livro, user: 'Professor'  ) -> bool:
        numeroExemplaresDisponiveis = livro.get_numero_exemplares_disponiveis()
        semExemplaresDisponiveis = numeroExemplaresDisponiveis == 0

        condicionais = [ 
            { "condicao": semExemplaresDisponiveis,             "erro": AssertionError(f"O livro {livro.titulo} não possui exemplares disponíveis") },
            { "condicao": user.esta_em_debito(),                "erro": AssertionError(f"O usuário {user.nome} está em débito") },
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                raise condicional["erro"]
        return True