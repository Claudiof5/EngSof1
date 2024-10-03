
from Usuarios.AlunoGraduacao import AlunoGraduacao
from Usuarios.AlunoPosGraduacao import AlunoPosGraduacao
from Biblioteca import Biblioteca
from Livros.Livro import Livro
from Interface import Interface


def instancia_dados(biblioteca :Biblioteca):
    dict_codigo_livro = {
    "100": {'titulo': 'Engenharia de Software', 'autores': 'Ian Sommerville', 'editora': 'AddisonWesley', 'edicao': '6ª', 'ano': '2000'},
    "101": {'titulo': 'UML – Guia do Usuário', 'autores': 'Grady Booch, James Rumbaugh, Ivar Jacobson', 'editora': 'Campus', 'edicao': '7ª', 'ano': '2000'},
    "200": {'titulo': 'Code Complete', 'autores': 'Steve McConnell', 'editora': 'Microsoft Press', 'edicao': '2ª', 'ano': '2014'},
    "201": {'titulo': 'Agile Software Development, Principles, Patterns, and Practices', 'autores': 'Robert Martin', 'editora': 'Prentice Hall', 'edicao': '1ª', 'ano': '2002'},
    "300": {'titulo': 'Refactoring: Improving the Design of Existing Code', 'autores': 'Martin Fowler', 'editora': 'Addison-Wesley Professional', 'edicao': '1ª', 'ano': '1999'},
    "301": {'titulo': 'Software Metrics: A Rigorous and Practical Approach', 'autores': 'Norman Fenton, James Bieman', 'editora': 'CRC Press', 'edicao': '3ª', 'ano': '2014'},
    "400": {'titulo': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'autores': 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', 'editora': 'Addison-Wesley Professional', 'edicao': '1ª', 'ano': '1994'},
    "401": {'titulo': 'UML Distilled: A Brief Guide to the Standard Object Modeling Language', 'autores': 'Martin Fowler', 'editora': 'Addison-Wesley Professional', 'edicao': '3ª', 'ano': '2003'}
    }

    for codigo, dados in dict_codigo_livro.items():
        autores = [autor.strip().title() for autor in dados['autores'].split(',')]
        biblioteca.cadastrar_livro(codigo, dados['titulo'], autores, dados['editora'], dados['edicao'], dados['ano'])
        
    dict_codigo_exemplar = {
    "100": [
        {"codigo": 1, "disponivel": True},
        {"codigo": 2, "disponivel": True}
    ],
    "101": [
        {"codigo": 3, "disponivel": True}
    ],
    "200": [
        {"codigo": 4, "disponivel": True}
    ],
    "201": [
        {"codigo": 5, "disponivel": True}
    ],
    "300": [
        {"codigo": 6, "disponivel": True},
        {"codigo": 7, "disponivel": True}
    ],
    "400": [
        {"codigo": 8, "disponivel": True},
        {"codigo": 9, "disponivel": True}
    ]
    }

    for codigo_livro, exemplares in dict_codigo_exemplar.items():
        for exemplar in exemplares:
            biblioteca.cadastrar_exemplar(codigo_livro, exemplar['codigo'])

    dict_codigo_usuario = {
    "123": {"nome": "João da Silva", "tipo": "ALUNOGRADUACAO"},
    "456": {"nome": "Luiz Fernando Rodrigues", "tipo": "ALUNOPOSGRADUACAO"},
    "789": {"nome": "Pedro Paulo", "tipo": "ALUNOGRADUACAO"},
    "100": {"nome": "Carlos Lucena", "tipo": "PROFESSOR"}
    }

    for codigo, dados in dict_codigo_usuario.items():
        biblioteca.cadastrar_usuario(str(codigo), dados['nome'], dados['tipo'])


#biblioteca = Biblioteca()
#instancia_dados(biblioteca)
#biblioteca.inscreve_professor_a_livro(100, 1)
#biblioteca.reservar_livro( 123, 100)
#biblioteca.reservar_livro( 456, 100)

#biblioteca.retorna_informacoes_livro(100)
#biblioteca.retorna_informacoes_usuarios(456)
#print(biblioteca.find_user(100).notificacoes)
#biblioteca.find_user(123).devolver_livro(100)
#biblioteca.retorna_informacoes_usuarios(100)
biblioteca = Biblioteca.get_instance()
instancia_dados(biblioteca)
#print(biblioteca.retorna_informacoes_usuario("100"))
sistema = Interface()
sistema.executar_comando( ["obs", "100", "100"])
sistema.executar_comando( ["res", "100", "100"])
sistema.executar_comando( ["emp", "100", "100"])
sistema.iniciar_sistema()