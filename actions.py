from verification import verificarCasasOcupadas
from os import _exit

from verification import verifQuemJoga
from utils import converterJogada, formatCasa
from robot import calcularJogada

# JOGADA ROBO
def jogadaRobo(tela, quemJoga):
  input('Vez do robo\n(aperte enter para ver o movimento)')
  
  jogada = calcularJogada(tela, quemJoga) # Recebe lista com linha e coluna
  tela[jogada[0]][jogada[1]] = quemJoga

  verificarCasasOcupadas(False, jogada)
  # ---------------------------
  tela = formatCasa(tela) # ver formatar direto na hora que escreve na tela
  # ---------------------------

# JOGADA PLAYER
def jogadaPlayer(tela, quemJoga):
  jogada = receberJogada()
  if jogada == 'invalido': return False

  i = converterJogada(jogada) # [0,0]
  jogadaValida = verificarCasasOcupadas(False, i)

  if not jogadaValida: return False
  
  tela[i[0]][i[1]] = formatCasa(tela, quemJoga)

  return

# Recebe o input do usuário
def receberJogada():
  try: 
    print('(Digite 0 para encerrar o jogo)')
    jogada = int(input('Digite uma casa de 1 a 9 para jogar: ')) 
  except ValueError:
    print('Digite um número!')
    return 'invalido'

  # Encerrar o jogo
  if jogada == 0:
    _exit(0)

  if jogada not in range(1,10):
    return 'invalido'

  return jogada

# Junta as funções auxiliares e realiza a adição do input na matriz 
def jogar(mudarQmJoga = True, tela = []):
  global quemJoga
  
  # Verificar de quem é a vez
  try:
    quemJoga = verifQuemJoga(mudarQmJoga, quemJoga)
  except:
    quemJoga = verifQuemJoga(mudarQmJoga)

  # Vez do robo
  if quemJoga == 'O':
    jogadaRobo(tela, quemJoga)
    return

  # Vez do jogador
  validar = jogadaPlayer(tela, quemJoga) # False se a jogada não for valida
  return validar