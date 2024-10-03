from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca
from Usuarios.Professor import Professor
from Livros.Livro import Livro

class ObservarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            codigoUsuario = parametro.getParametroUm()
            codigoLivro = parametro.getParametroDois()

            usuario: None | Professor = biblioteca.find_user(codigoUsuario)
            livro:   None | Livro     = biblioteca.find_book(codigoLivro)

            if not usuario:
                raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            
            if not livro:
                
                raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
            
            observador = usuario._observerProfessor
            livro.inscreve_observador_a_livro(observador)
            retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": None, "dataDevolucao": None}
            return retorno