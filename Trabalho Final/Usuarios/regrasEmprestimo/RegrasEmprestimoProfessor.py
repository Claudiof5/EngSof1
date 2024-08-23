from Usuarios.regrasEmprestimo.iRegrasEmprestimo import *
#from Interface import Interface 

class RegrasEmprestimoProfessor(iRegrasEmprestimo):

    def apto_a_emprestimo(self, livro :Livro, user  ) -> bool:
        numeroExemplaresDisponiveis = livro.get_numero_exemplares_disponiveis()
        semExemplaresDisponiveis = numeroExemplaresDisponiveis == 0

        condicionais = [ 
            { "condicao": semExemplaresDisponiveis,             "mensagem": Interface.Erro_livro_indisponivel},
            { "condicao": user.esta_em_debito(),                "mensagem": Interface.Erro_usuario_em_debito},
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                condicional["mensagem"]()
                return False
        return True