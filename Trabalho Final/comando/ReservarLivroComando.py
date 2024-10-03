from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca
from Livros.Reserva import Reserva

class ReservarLivroComando(iComando):
        
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
            
            if usuario.apto_a_reserva(livro):
            
                reserva = Reserva(livro, usuario)
                usuario.adiciona_reserva(reserva)
                livro.adiciona_reserva(reserva)
                biblioteca._reservas.append(reserva)
                retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": None, "dataDevolucao": None}
                return retorno