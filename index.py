from os import system
from tela import layoutTela
from verification import verificarCasasOcupadas
from main import main

# ===================
#   Repetir o jogo
# ===================
continuar = True
pontos = [0,0]
while continuar:
  system('cls')

  # variaveis iniciais 
  tela = layoutTela()
  verificarCasasOcupadas(True)

  # Roda
  pontos = main(tela, True, pontos)

  # Quando acaba
  continuar = input('Deseja cotinuar? [s/n] ')
  if continuar.lower() == 'n':
    continuar = False

