from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ObservarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            biblioteca.inscreve_professor_a_livro(parametro.getParametroUm(), parametro.getParametroDois())
            