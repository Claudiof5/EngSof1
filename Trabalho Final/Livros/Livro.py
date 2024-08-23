from typing import List
from Livros.Reserva import Reserva
from Livros.Emprestimo import Emprestimo
from Livros.Exemplar import Exemplar
from Livros.subject.SubjectNumeroDeReservas import SubjectNumeroDeReservas
from Livros.subject.SubjectNumeroDeReservas import SubjectNumeroDeReservas
from dataclasses import dataclass

class Livro:
    def __init__(self, codigoIdentificador: int, titulo: str, autores: List[str], editora: str
                 , edicao:int , anoDePublicacao:str)-> None:
        self._codigoIdentificador = codigoIdentificador
        self._titulo = titulo
        self._autores = autores
        self._editora = editora
        self._edicao = edicao
        self._anoDePublicacao = anoDePublicacao
        self._exemplares  :List[Exemplar]   = []
        self._reservas    :List[Reserva]    = []
        self._emprestimos :List[Emprestimo] = []
        self.subject_numero_reservas = SubjectNumeroDeReservas(codigoIdentificador)

    # Getters
    @property
    def codigoIdentificador(self) -> int:
        return self._codigoIdentificador
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def autores(self) -> List[str]:
        return self._autores
    
    @property
    def editora(self) -> str:
        return self._editora
    
    @property
    def edicao(self) -> int:
        return self._edicao
    
    @property
    def anoDePublicacao(self) -> str:
        return self._anoDePublicacao
    
    @property
    def exemplares(self) -> List[Exemplar]:
        return self._exemplares
    
    @property
    def reservas(self) -> List[Reserva]:
        return self._reservas
    
    @property
    def emprestados(self) -> List[Emprestimo]:
        return self._emprestimos

    def get_numero_exemplares_disponiveis(self) -> int:
        return len(self.get_exemplares_disponiveis())
    
    def get_numero_reservas(self) -> int:
        return len(self._reservas)
    
    def adiciona_reserva(self, reserva: Reserva) -> None:
        self._reservas.append(reserva)
        self.subject_numero_reservas.update_numero_reservas(self.get_numero_reservas())
    
    def remove_reserva(self, reserva: Reserva) -> None:
        self._reservas.remove(reserva)
        self.subject_numero_reservas.update_numero_reservas(self.get_numero_reservas())

    def adiciona_emprestimo(self, emprestimo: Emprestimo) -> None:
        self._emprestimos.append(emprestimo)

    #Operações com exemplar
    def cadastrar_exemplar(self, codigoExemplar: int) -> None:
        exemplar = Exemplar(self, codigoExemplar)
        self._exemplares.append(exemplar)

    def get_exemplares(self) -> List[Exemplar]:
        return self._exemplares
    
    def get_exemplares_disponiveis(self) -> List[Exemplar]:
        disponiveis = [ exemplar for exemplar in self.get_exemplares() if exemplar.disponivel ]
        return disponiveis
    
    def retorna_emprestimo_ativo_por_exemplar(self, codigoExemplar: int) -> Emprestimo:
        for emprestimo in self._emprestimos:
            if emprestimo.codigoExemplar == codigoExemplar and emprestimo.emCurso:
                return emprestimo
        return None
    
    def retorna_exemplar_disponivel_para_emprestimo(self) -> Emprestimo:

        exemplares = self.get_exemplares_disponiveis()
        if len(exemplares) == 0:
            return None
        exemplar = exemplares[0]
        exemplar.disponivel = False

        return exemplar
    
    def retorna_informacoes(self) -> None:
        numero_de_reservas = self.get_numero_reservas()

        print("Titulo: ", self._titulo)
        
        print(f"Quantidade de reservas: {numero_de_reservas}")

        if numero_de_reservas > 0:
            for reserva in self._reservas:
                print(f"\t-{reserva.get_nome_usuario()}")

        print("Exemplares")
        exemplares :List[Exemplar] = self.get_exemplares()
        existem_exemplares = len(exemplares) > 0
        if existem_exemplares:
            for exemplar in exemplares:

                if exemplar.disponivel:
                    print(f"\t-Codigo Exemplar:{exemplar.codigoExemplar}\n\tStatus: Disponivel\n\t")
                else:
                    emprestimo = self.retorna_emprestimo_ativo_por_exemplar(exemplar.codigoExemplar)
                    if emprestimo:
                        print(f"\t-Codigo Exemplar:{exemplar.codigoExemplar}\n\tStatus: Emprestado")
                        print(f"\tUsuario: {emprestimo.nomeUsuario}\n\tData de Emprestimo: {emprestimo.dataEmprestimo} | Data de Devolução Esperada: {emprestimo.dataDeDevolucaoEsperada}\n")  

    def inscreve_observador_a_livro(self, observer: SubjectNumeroDeReservas) -> None:
        self.subject_numero_reservas.attach(observer)