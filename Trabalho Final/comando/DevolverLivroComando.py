from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class DevolverLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            biblioteca.devolver_livro(parametro.getParametroUm(), parametro.getParametroDois())
            