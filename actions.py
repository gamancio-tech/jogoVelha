from verification import verificarCasas
from os import _exit

from verification import verifQuemJoga
from utils import converterJogada, formatCasa

# Recebe o input do usuário
def receberJogada():
  try: 
    print('(Digite 0 para encerrar o jogo)')
    jogada = int(input('Digite uma casa de 1 a 9 para jogar: ')) 
  except ValueError:
    print("Digite um número!")
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
  
  try:
    quemJoga = verifQuemJoga(mudarQmJoga, quemJoga)
  except:
    quemJoga = verifQuemJoga(mudarQmJoga)

  jogada = receberJogada()
  if jogada == 'invalido': return False

  i = converterJogada(jogada)
  jogadaValida = verificarCasas(False, i)

  if not jogadaValida: return False
  
  tela[i[0]][i[1]] = quemJoga
  tela = formatCasa(tela)

  return 
