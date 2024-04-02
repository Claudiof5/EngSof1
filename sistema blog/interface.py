from classes import Sistema, Blog, Nota, Comentario
from classes.sistema import User
from os import system


def login():
    system("clear")
    while(True):    
        chave = input("""Escolha um para continuar
1- Logar
2- Criar conta
3- Sair
 """)
        if chave == "1":
            system("clear")
            print("Efetuando Login")
            email = input("insira email: ")
            user = Sistema.getUserByEmail(email)
            if isinstance(user, User):
                opcoesUsuario( user)
            else:
                system("clear")
                print("email invalido")
        elif chave == "2":
            userId = None
            while True:
                system("clear")
                print("Efetuando Cadastro")
                email = input("insira um email não cadastrado para criar sua conta ou escreva 0 para sair: ")
                
                userId = Sistema.createUser(email)
                user = Sistema.getUserById(userId)
                if email == "0":
                    break
                if isinstance(user, User):
                    opcoesUsuario( user)
                    break
                
                
        elif chave == 3:
            break
            

def opcoesUsuario( user: User):
    while True:
        system("clear")
        print(f"Logado como {user.email}\n")
        chave = input("""Escolha um para continuar
1-Checar blogs existentes
2-Criar blogs
3-Administrar seus blogs
4-Voltar
""")

        if chave == "1":
            verBlogs(user)
        elif chave == "2":
            titulo = input("insira um titulo para seu blog: ")
            user.createBlog(titulo)
        elif chave == "3":
            administrarBlog(user)
        elif chave == "4":
            break


def administrarBlog( user: User ):
    system("clear")
    print(f"Logado como {user.email}")
    existeBlog = user.printAllBlogsCriados()
    if existeBlog:
        blogId = input("digite o id do blog que você quer administrar ou 0 para sair: ")
        while blogId not in user.blogsCriados:
            blogId = input("digite o id do blog que você quer administrar ou 0 para sair: ")
            if blogId == "0":
                return False
        while True:    
            chave = input("""
1-Criar Nota
2-Apagar Nota
3-Voltar\n
""")
            if chave == "1":
                titulo = input("Insira o titulo desejado: ")
                texto = input("Insira o texto: ")
                user.createNota(blogId, titulo, texto)
                break
            elif chave == "2":
                noteId = input("Insira o Id da nota: ")
                Sistema.deleteNota(user.userId, noteId)
            elif chave == "3":
                break
    else:
            print("Sem blogs criados")
            return False
    
        
def verBlogs(user: User):
    system("clear")
    print(f"Logado como {user.email}")

    while True:
        print("\nLista de blogs")
        Sistema.printAllBlogs()
        chave= input("""
1-Acessar um blog
2-Voltar\n
    """)
        if chave == "1":
            blogId = input("insira o id do blog: ")
            acessarBlog(user,blogId)
        if chave == "2":
            break
def acessarBlog(user, blogId : str):
    blog = Sistema.getBlogById(blogId)
    while True:
        blog.printAllNotas()
        chave = input("""
    1-Ver comentarios de nota
    2-Voltar
    """)
        if chave == "1":
            while True:
                noteId = input("Insira o id da Nota valido que você quer ver a fundo ou 0 para sair: ")    
                nota = Sistema.getNoteById(noteId)
                notaExiste = nota in blog.notes
                if noteId == "0":
                    break
                if (notaExiste):
                    verNota(user, nota)
                    break
        elif chave == "2":
            break

def verNota(user : User ,nota: Nota ):
    system("clear")
    print(f"Logado como {user.email}")

    while True:
        nota.checaNotaAFundo()

        chave = input("""
    1-Comentar
    2-Voltar
    """)
        if chave == "1":
            comentario = input("Insira seu comentario aqui: ")
            user.createComentario(nota.noteId, comentario)
        if chave == "2":
            break

userId = login()
