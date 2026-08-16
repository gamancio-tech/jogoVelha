from os import system
from tela import mostrarTela
from actions import jogar
from verification import verificarGanho


# Atualiza a tela e chama o jogar()
# mudarQmJoga é passado duas funções a frente para verifQuemJoga()
# pyrefly: ignore [parse-error]
def main(tela, mudarQmJoga=True, pontos=0):
  system('cls')
  mostrarTela(tela, pontos)

  jogadaValida = jogar(mudarQmJoga, tela)

  if jogadaValida != None:
    input('Jogada invalida!')
    return main(tela, False, pontos) # parametro False para não mudar o print de quem é a vez

  game_status = verificarGanho(tela)
  if game_status != False:
    system('cls')
    mostrarTela(tela, pontos)
    if game_status == 'velha':
      input(f'\nDeu velha!')
    else:
      input(f'\nO jogador {game_status} ganhou!')
      pontos = pontuar(game_status, pontos)
    return pontos

  return main(tela, True, pontos)

def pontuar(winner, pontos=[0,0]):
  player1 = pontos[0]
  player2 = pontos[1]

  if winner == None:
    pass
  elif winner == 'X':
    player1 += 1
  else:
    player2 += 1
    
  return [player1, player2]
