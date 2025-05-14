import random
import os

def limparTELA():
      #limpa o console quando requisitado para deixar o ambiente mais limpo
      os.system('cls' if os.name == 'nt' else 'clear')

def batalha_final():
    #leva para a batalha final do jogo
    print("batalha final")

def vilarejo():
    #leva para o vilarejo
    print("Vilarejo")

def vulcao():
    #leva para o vulcao
    print("vulcao")

def precipicio():
    #leva para o precipicio
    print("precipicio")

def floresta():
    #leva para a floresta
    print("floresta")

def mage():
    #status do mago
    life = 10
    atack = 5
    defense = 6
    start_point = "F"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats

def valkyrie():
    #status da guerreira
    life = 12
    atack = 6
    defense = 2
    start_point = "V"
    info_stats = f"Vida: {life}\nAtaque: {atack}\nDefesa: {defense}"
    return life, atack, defense, start_point, info_stats

#apaga restos de info do console antes de iniciar 
limparTELA()

#variaveis pre definidas para usu global
esco_persona = ""
life, atack, defense, start_Point, info_Stats = 0, 0, 0, "", ""

print("bem vindo! escolha seu personagem: ")

#validação de escolha
while esco_persona != "1" and esco_persona != "2":

 esco_persona = input("1- Mago\n2- Guerreira\n3- Informações de Personagens:")

#estrutura para decidir o personagem (previne erros)
 if esco_persona == "1":
    limparTELA()
    #carrega status do mago
    life, atack, defense, start_Point, info_Stats = mage()
 elif esco_persona == "2":
    limparTELA()
    #carrega status da guerreira
    life, atack, defense, start_Point, info_Stats = valkyrie()
 elif esco_persona == "3":
    limparTELA()

    #estrura para ver as informacoes e decidir qual personagem o uso tem mais familiaridade
    esco_info = ""

    #estrutura para decidir qual o status do personagem quer ver (previne erros)
    while esco_info != "1" and esco_info != "2" and esco_info != "3":
        print("qual dos persongens voce quer ver historia e status:?")
        esco_info = input("1- Mago\n2- Guerreira\n3- voltar\n:")
        limparTELA()
    
        if esco_info == "1":
            life, atack, defense, start_Point, info_Stats = mage() 
            
            #printa as infos com base na escolha
            print(info_Stats)
            #pausa o codigo para a visualização das infos
            Exit = input("\naperte qualquer tecla para sair:")
        
        elif esco_info == "2":
            life, atack, defense, start_Point, info_Stats = valkyrie() 
            
            #printa as infos com base na escolha
            print(info_Stats)
            #pausa o codigo para a visualização das infos
            Exit = input("\naperte qualquer tecla para sair:")
       
        elif esco_info == "3":
            
            #volta para o primeiro menu e limpa o console para uma melhor visu
            limparTELA()
        else:
           
           #impede o erro
           limparTELA()
           print("opcao invalida\n") 

    limparTELA()
 else:

    #impede o erro
    limparTELA()
    print("persongam nao encontrado ;(\n")

#passado a historia e contexto para o usu surge as opcoes!


#                                    A
#PONTO DE BAIXA ALTERAÇÃO DE CODIGO  |


#_____________________________________________________________________________________________________________________________________


#PONTO DE ALTA ALTERAÇÃO DE CODIGO  |
#                                  V


#define a variavel para usar de parametro na hora de dar respawn do personagem
if start_Point == "V":
    print("Voce escolheu a Guerreira\n")
else:
    print("Voce escolheu o Mago\n")

print("o que voce vai fazer agora? ¯\(ツ)/¯")
print()

decisao_ini = input("1- Buscar \n2- Guerreira\n3- Informações de Personagens:")