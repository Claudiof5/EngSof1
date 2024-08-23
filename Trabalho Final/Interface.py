from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from comando.EmprestarLivroComando import EmprestarLivroComando
from comando.DevolverLivroComando import DevolverLivroComando
from comando.ReservarLivroComando import ReservarLivroComando
from comando.ObservarLivroComando import ObservarLivroComando
from comando.ConsultarLivroComando import ConsultarLivroComando
from comando.ConsultarUsuarioComando import ConsultarUsuarioComando
from comando.ConsultarNotificacaoComando import ConsultarNotificacaoComando
from comando.SaiDoSistemaComando import SaiDoSistemaComando

class Interface:

    def __init__(self) -> None:
        self.comandos: dict[str, dict[str, iComando|int ]] = {}
        self.iniciar_Comandos()


    def iniciar_Comandos(self):
        self.comandos['emp'] = {"comando": EmprestarLivroComando(), "parametros": 2}
        self.comandos['dev'] = {"comando": DevolverLivroComando(), "parametros": 2}
        self.comandos['res'] = {"comando": ReservarLivroComando(), "parametros": 2}
        self.comandos['obs'] = {"comando": ObservarLivroComando(), "parametros": 1}
        self.comandos['liv'] = {"comando": ConsultarLivroComando(), "parametros": 1}
        self.comandos['usu'] = {"comando": ConsultarUsuarioComando(), "parametros": 1}
        self.comandos['ntf'] = {"comando": ConsultarNotificacaoComando(), "parametros": 1}
        self.comandos['sai'] = {"comando": SaiDoSistemaComando(), "parametros": 0}


    def recebe_entrada(self) -> str:
        entrada = input("Digite o comando: ")
        return self.trata_entrada(entrada)
    
    def trata_entrada(self, entrada: str)-> list[str]:
        listaDeEntrada = entrada.split(" ")
        listaDeEntrada = [parametro.strip() for parametro in listaDeEntrada]
        return listaDeEntrada
    
    def criar_parametros(self, listaDeEntrada: list[str]) -> Parametro:
        if len(listaDeEntrada) == 1:
            return Parametro(None, None)
        elif len(listaDeEntrada) == 2:
            return Parametro(listaDeEntrada[1], None)
        else:
            return Parametro(listaDeEntrada[1], listaDeEntrada[2])
    
    
    def comando_valido(self, comando: list[str]) -> bool:
        if comando[0] in self.comandos:
            if len(comando) -1 == self.comandos[comando[0]]["parametros"]:

                return True

            self.Erro_numero_de_parametros_invalido()
            return False
        self.Erro_comando_invalido()
        return False
    
    def executar_comando(self, comando: list[str]):
        if self.comando_valido(comando):
            print(comando)
            parametro :Parametro = self.criar_parametros(comando)
            comando   :iComando  = self.comandos[comando[0]]["comando"]
            
            try:
                comando.executar(parametro)
            except Exception as e:
                print(e)

    def iniciar_sistema(self):
        while True:
            entrada = self.recebe_entrada()
            self.executar_comando(entrada)

    def Erro_numero_de_parametros_invalido(self):
        print("Operação não concluída. Número de parâmetros inválido\n")
    
    def Erro_comando_invalido(self):
        print("Operação não concluída. Comando inválido\n")
    
    def Erro_livro_indisponivel(self):
        print("Operação não concluída. Livro indisponivel\n")
    
    def Erro_usuario_em_debito(self):
        print("Operação não concluída. Usuário em débito\n")
    
    def Erro_limite_de_livros_alcancado(self):
        print("Operação não concluída. Limite de livros alcançado\n")
    
    def Erro_reserva_excedida(self):
        print("Operação não concluída. Número de reservas excedido\n")

    def Erro_emprestimo_ativo(self):
        print("Operação não concluída. Usuário já tem um empréstimo ativo de um exemplar do livro\n")

    def Erro_livro_nao_encontrado(self):
        print("Operação não concluída. Livro não encontrado\n")
        
    def Erro_usuario_nao_encontrado(self):
        print("Operação não concluída. Usuário não encontrado\n")
    
    def Erro_emprestimo_nao_encontrado(self):
        print("Operação não concluída. Empréstimo não encontrado\n")

    def Erro_reservas_maximas_atingidas(self):
        print("Operação não concluída. Número de reservas máximas atingidas\n")

    def Erro_livro_ja_reservado(self):
        print("Operação não concluída. Livro já reservado\n")

    def Erro_livro_ja_emprestado(self):
        print("Operação não concluída. Livro já emprestado\n")

    def emprestimo_realizado(dataDeDevolucaoEsperada):
        print(f"Empréstimo realizado com sucesso, data de devolução esperada: {dataDeDevolucaoEsperada}\n")

    def reserva_realizada(self):
        print("Reserva realizada com sucesso\n")

        
