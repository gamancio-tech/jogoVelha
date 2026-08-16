from tkinter import VERTICAL
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

  jogada_robo = analisarCasasLivres(tela_robo, tela, joga, livres) # Ve se ganha na próxima jogada em alguma casa livre
  if jogada_robo != None:
    return jogada_robo

  jogada_robo = analisarCasasLivres(tela_robo, tela, jogador, livres)

  if jogada_robo == None:
    jogada_robo = choice(livres)

  return jogada_robo
  

def verGanhar(tela_robo, tela, quemJoga, livres, casa):
  tela_robo = [linha[:] for linha in tela] # Fazer cópia verdadeira
  tela_robo = formatCasa(tela_robo)

  tela_robo[livres[casa][0]][livres[casa][1]] = quemJoga
  estado = verificarGanho(tela_robo)
  if (estado) and estado.lower() in ['x','o']:
    estado = formatCasa(tela, estado)

  if estado == quemJoga:
    jogada_robo = livres[casa]
    return jogada_robo 

def analisarCasasLivres(tela_robo, tela, joga, livres):
  for casa in range(len(livres)):
    ganhou = verGanhar(tela_robo, tela, joga, livres, casa)
    if ganhou:
      return ganhou