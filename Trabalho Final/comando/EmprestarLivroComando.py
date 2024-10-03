from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca
from Livros.Emprestimo import Emprestimo
from Livros.Reserva import Reserva

class EmprestarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            codigoUsuario = parametro.getParametroUm()
            codigoLivro = parametro.getParametroDois()

            usuario = biblioteca.find_user(codigoUsuario)
            livro = biblioteca.find_book(codigoLivro)

            if not usuario:
                raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            
            if not livro:
                raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
            
            if usuario.apto_a_emprestimo(livro):
                exemplar = livro.retorna_exemplar_disponivel_para_emprestimo()
                emprestimo :Emprestimo = Emprestimo( exemplar, usuario)
            
                reserva: Reserva = usuario.find_reserva(livro)
                if reserva:
                    usuario.retira_reserva(reserva)
                    livro.remove_reserva(reserva)

                usuario.adiciona_emprestimo(emprestimo)
                livro.adiciona_emprestimo(emprestimo)
                biblioteca._emprestados.append(emprestimo)

                
                #Interface.emprestimo_realizado(emprestimo.dataDeDevolucaoEsperada)
                retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": emprestimo.dataDeDevolucaoEsperada, "dataDevolucao": None}
                return retorno
            