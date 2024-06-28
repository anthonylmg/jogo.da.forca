import os
import random as rnd
os.system('cls')

lista_frutas = ['abacate', 'pitaya', 'melancia', 'kiwi', 'maçã']
lista_animais = ['cachorro', 'gato', 'hipopótamo', 'canguru', 'serpente']
lista_cores = ['vermelho', 'azul', 'amarelo', 'cinza', 'roxo']

def desenhar_hangman():
    
    if chances ==10:
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        
    if chances ==9:
        print('             ')
        print('            |')
        print('            |')
        print('            |')
        print('            |')
        print('          ---')
    
    if chances ==8:
        print('      ______')
        print('      |     |')
        print('            |')
        print('            |')
        print('            |')
        print('          ---')
        
    if chances ==7:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('            |')
        print('            |')
        print('          ---')
    
    if chances ==6:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('      |     |')
        print('            |')
        print('          ---')
        
    if chances ==5:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|     |')
        print('            |')
        print('          ---')

    if chances ==4:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('            |')
        print('          ---')
        
    if chances ==3:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('     /      |')
        print('          ---')
    if chances ==2:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('     / \    |')
        print('          ---')
        
    if chances ==1:
        print('      ______')
        print('      |     |')
        print('    (; ;)   |')
        print('     /|\    |')
        print('     / \    |')
        print('          ---')

def obter_input_sem_repeticao(letras_usuario):
    while True:
        tentativa = input("Entre com uma letra: ").lower()
        if tentativa in letras_usuario:
            print("Letra repetida! Tente novamente.")
        else:
            letras_usuario.append(tentativa)
            return tentativa

while True:

    lista = [lista_frutas, lista_animais, lista_cores]

    lista_sorteada = rnd.choice(lista)

    palavra = rnd.choice(lista_sorteada)
    
    chances = 10

    letras_usuario = []
    
    ganhou = False

    while True:
        os.system('cls')
        
        if lista_sorteada == lista_frutas:
            print('FRUTAS')

        elif lista_sorteada == lista_animais:
            print('ANIMAIS')

        elif lista_sorteada == lista_cores:
            print('CORES')
        
        desenhar_hangman()

        for letra in palavra:
            
            if letra.lower() in letras_usuario:

                print(letra, end=" ")

            else:

                print("_", end=" ")
        
        print(f"\nVocê tem {chances} chances")
        
        print('HISTÓRICO DE LETRAS:', letras_usuario)    
        
        tentativa = obter_input_sem_repeticao(letras_usuario)
            
        if tentativa not in palavra.lower():

            chances -= 1

        ganhou = True

        for letra in palavra:

            if letra.lower() not in letras_usuario:

                ganhou = False 
             
        if chances == 0 or ganhou:
            os.system('cls')
            break
    
    if ganhou:
            print(f"Parabéns, você ganhou! A palavra era {palavra}")

    else:
        if chances ==0:       
            print('      ______')
            print('      |     |')
            print('    (;-;)   |')
            print('     /|\    |')
            print('     / \    |')
            print('          ---')
        print(f"Você perdeu! A palavra era {palavra}")
            
    play = input('Insira ''p'' para continuar jogando ou ''s'' para encerrar o jogo: ')
        
    if play == 's':
            print('Jogo finalizado!')
            break