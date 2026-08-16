from verification import verificarGanho
from random import choice
from utils import formatCasa

def calcularJogada(tela, joga):
  if joga == 'O':
    jogador = 'X'
  else:
    jogador = 'O'
  joga = formatCasa(None, joga)
  jogador = formatCasa(None, jogador)
  
  tela_robo = [linha[:] for linha in tela] # Fazer cópia verdadeira
  tela_robo = formatCasa(tela_robo)

  livres = [] # Indices livres [l,c]
  jogada_robo = []

  for l in range(len(tela_robo)):
    for c in range(len(tela_robo)):

      if tela_robo[l][c] == '   ':
        livres.append([l, c])

  if len(livres) < 0:
    return 

  analisarCasasLivres(tela_robo, tela, joga, livres) # Ve se ganha na próxima jogada em alguma casa livre
  analisarCasasLivres(tela_robo, tela, jogador, livres)
    
  jogada_robo = choice(livres)
  return jogada_robo
  

def verGanhar(tela_robo, tela, quemJoga, livres, casa):
  tela_robo = [linha[:] for linha in tela] # Fazer cópia verdadeira
  tela_robo = formatCasa(tela_robo)

  tela_robo[livres[casa][0]][livres[casa][1]] = quemJoga
  estado = verificarGanho(tela_robo)

  #input(f'{tela_robo} e {estado} | {quemJoga}')

  if estado == quemJoga.strip(' '):
    jogada_robo = livres[casa]
    return jogada_robo

def analisarCasasLivres(tela_robo, tela, joga, livres):
  for l in range(len(livres)):
    ganhou = verGanhar(tela_robo, tela, joga, livres, l)
    if ganhou:
      return ganhou