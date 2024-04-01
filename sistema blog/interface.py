from classes.sistema import*
import sys


def login():
    chave = input("""Escolha um para continuar
    1- Logar
    2- Criar conta
    3- Sair\n
                
    """)
    userId = None
    if chave == "1":
        email = input("insira email")
        userId = Sistema.getUserByEmail(email)

        return userId
    
    elif chave == "2":
        userId = None
        email = None
        while( not userId or email != "0"):
            email = input("insira um email não cadastrado para criar sua conta ou escreva 0")
            userId = Sistema.createUser(email)

        return userId
    elif chave == 3:
        sys.exit()

def opcoesUsuario( userId):
    user : User = Sistema.getUserById(userId)

    chave = input("""
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
        sys.exit()


def administrarBlog( user: User ):
    user.printAllBlogsCriados()
    blogId = None
    while( blogId not in user.blogsCriados):
        blogId = input("escolha o id do blog que você quer administrar: ")
    
    chave = input("""
    1-Criar Nota
    2-Apagar Nota
    3-Voltar\n
""")
    if chave == "1":
        titulo = input("Insira o titulo desejado: ")
        texto = input("Insira o texto: ")
        user.createNota(blogId, titulo, texto)
    elif chave == "2":
        noteId = input("Insira o Id da nota: ")
        Sistema.deleteNota(user.userId, noteId)
    elif chave == "3":
        sys.exit()

def verBlogs(user):
    Sistema.printAllBlogs()
    chave= input("""
    1-Acessar um blog
    2-Voltar\n
""")
    if chave == "1":
        blogId = input("insira o id do blog: ")
        acessarBlog(blogId)
    if chave == "2":
        sys.exit()
def acessarBlog(blogId):
    pass

sistema = Sistema()