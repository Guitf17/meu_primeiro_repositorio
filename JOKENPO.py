import random
import time
from colorama import Fore, Back

#DIZ AO PYTHON QUAIS SÃO AS OPÇÕES (1, 2 e 3) E O QUE ELAS SIGNIFICAM
ppt = {1: "PEDRA", 2: "PAPEL", 3: "TESOURA"}

while True:
    #Solicita que o jogador escolha entre PEDRA, PAPEL OU TESOURA
    ler = int(input(f'{Fore.LIGHTMAGENTA_EX}Vamos jogar JOKENPÔ!\n'
      f'{Fore.RESET}SUAS OPÇÕES SÃO:\n'
      f'{Fore.LIGHTCYAN_EX}[ 1 ] PEDRA{Fore.RESET}\n'
      f'{Fore.LIGHTYELLOW_EX}[ 2 ] PAPEL{Fore.RESET}\n'
      f'{Fore.LIGHTGREEN_EX}[ 3 ] TESOURA{Fore.RESET}\n'
      f'{Fore.LIGHTWHITE_EX}QUAL SUA ESCOLHA ?: '))
    if ler not in ppt:
        print(f"{Back.RED + Fore.LIGHTWHITE_EX}ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS ACIMA! (1 para PAPEL, 2 para PEDRA OU 3 para TESOURA)")
        exit() #ENCERRA O PROGRAMA SE A ESCOLHA FOR INVÁLIDA
    else:
#random.choice([1, 2, 3]), ESCOLHE ALEATORIAMENTE UMA DAS OPÇÕES DISPONÍVEIS
        pc = random.choice([1, 2, 3])
#MOSTRA UMA ANIMAÇÃO DO NOME  JOKENPÔ, APARECENDO SEPARADAMENTE AS SÍLABAS NA TELA
    print(f"{Fore.LIGHTRED_EX}JO", end="", flush=True)
    time.sleep(0.5)
    print(f" {Fore.LIGHTGREEN_EX}KEN", end="", flush=True)
    time.sleep(0.5)
    print(f" {Fore.LIGHTBLUE_EX}PÔ!{Fore.RESET}")
    time.sleep(0.3)
#MOSTRA AS ESCOLHAS DO JOGADOR E DO COMPUTADOS
    print(f'{Fore.LIGHTYELLOW_EX}✰{Fore.RESET}'*20)
    print (f"{Fore.LIGHTCYAN_EX}JOGADOR jogou {ppt[ler]}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}COMPUTADOR jogou {ppt[pc]}{Fore.RESET}")
    print(f'{Fore.LIGHTYELLOW_EX}✰{Fore.RESET}'*20)
# RESULTADOS
    if ler == pc:
        print(f'{Back.LIGHTWHITE_EX + Fore.BLACK}EMPATE!{Back.RESET + Fore.RESET}')
    elif (ler == 1 and pc == 3) or (ler == 2 and pc == 1) or (ler == 3 and pc == 2):
        print(f'{Back.LIGHTGREEN_EX+ Fore.LIGHTWHITE_EX}PARABÉNS, VOCÊ VENCEU!{Back.RESET + Fore.RESET}')
    else:
        print(f'{Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX}VOCÊ PERDEU!{Back.RESET + Fore.RESET}')
# Pergunta se o jogador quer continuar
    jogar_novamente = input(f'\n{Fore.LIGHTWHITE_EX}Quer jogar novamente? {Fore.LIGHTGREEN_EX}(S/N): {Fore.RESET}').strip().upper()
    if jogar_novamente != 'S':
        print(f'\n{Fore.LIGHTYELLOW_EX}Obrigado por jogar! Até a próxima!{Fore.RESET}')
        break