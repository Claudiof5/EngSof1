from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca
from Usuarios.Professor import Professor

class ConsultarNotificacaoComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            codigoUsuario = parametro.getParametroUm()
            usuario: None | Professor = biblioteca.find_user(codigoUsuario)
            if not usuario:
               raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            return usuario.retorna_numero_de_notificacoes()