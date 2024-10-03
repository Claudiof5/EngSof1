from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ConsultarUsuarioComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            codigoUsuario = parametro.getParametroUm()
            
            usuario = biblioteca.find_user(codigoUsuario)
            if not usuario:
                raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            return usuario.retorna_informacoes()

            