from classes import Sistema, Blog, Nota, Comentario
from classes.sistema import User
import sys


def login():
    while(True):
        chave = input("""Escolha um para continuar
1- Logar
2- Criar conta
3- Sair\n
                    
        """)
        userId = None
        if chave == "1":
            email = input("insira email: ")
            userId = Sistema.getUserByEmail(email)
            if userId:
                opcoesUsuario( userId)
            else:
                print("email invalido")
        elif chave == "2":
            userId = None
            email = None
            
            
            email = input("insira um email não cadastrado para criar sua conta ou escreva 0 para sair: ")
            
            userId = Sistema.createUser(email)
            
            if email == "0":
                break
            opcoesUsuario( userId)
        elif chave == 3:
            break
            

def opcoesUsuario( userId):
    user : User = Sistema.getUserById(userId)
    while True:
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
    
        
def verBlogs(user):
        
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
def acessarBlog(user, blogId):
    blog = Sistema.getBlogById(blogId)
    blog.printAllNotas()
    chave = input("1-Ver comentarios de nota")



userId = login()
