#!/usr/bin/python3
import sys
import os

from random import choice

class gerador():
    def gerador_senha(tamanho):
        caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
        senha = ""
        for i in range(tamanho):
            senha += choice(caracteres)
        return senha
    def pergunta_arquivo(resposta):
        
        while resposta != "sim" and resposta != "não" and resposta != "nao":
            resposta = input("Deseja salvar em um arquivo? sim/não: ")
        if resposta == "sim":
            nome_do_arquivo = input("Nome do arquivo: ")
            arquivo = open("{}.txt".format(nome_do_arquivo), "a")
            arquivo.write("Nome do user: {}\n".format(nome))
            arquivo.write("Senha: {}\n".format(senha))
            arquivo.write("Link: {}".format(link))
            arquivo.close()
            sair = input("Deseja sair? sim/não: ")
            while sair == "não" or sair == "nao":
                sair = input("Deseja sair? sim/não: ")
        elif resposta == "não" or resposta == "nao":
            print()
            print()
            print("+--------------------------")
            print("|Nome de User: {}".format(nome))
            print("|Senha: {}".format(senha))
            print("|Link: {}".format(link))
            print("+--------------------------")
            print()
            sair = input("Deseja sair? sim/não: ")
            while sair == "não" or sair == "nao":
                sair = input("Deseja sair? sim/não: ")
    def pergunta_link(resposta):
        link = ""
        while resposta != "sim" and resposta != "não" and resposta != "nao":
            resposta = input("Quer digitar o link do site? sim/não: ")
        if resposta == "sim":
            link = input("Digite o link do site: ") 
        return resposta, link 

print()
print("------------------------------")
print("GERADOR DE SENHAS CMR HACKING")
print("-----------------------------")
print("Info: Este programa irá gerar uma senha para ser utilizada em cadastros e contas!")
print()

nome = input("Digite o nome de user: ")
quantidade = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))
pergunta_link = input("Quer digitar o link do site? sim/não: ")
pergunta_link, link = gerador.pergunta_link(pergunta_link) 

senha = gerador.gerador_senha(quantidade)
print("\n Sua senha: {}".format(senha))
print()
pergunta = input("Deseja salvar em um arquivo? sim/não: ")
pergunta = gerador.pergunta_arquivo(pergunta)