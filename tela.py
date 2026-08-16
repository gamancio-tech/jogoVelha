from utils import formatCasa

# Faz o layout da tela de acordo com a matriz
def mostrarTela(tela, pontos):
  print(f'Pontos:\n Jogador 1 (X): {pontos[0]}\n Jogador 2 (O): {pontos[1]}\n'+'-'*20,'\n\n')
  for rep, linha in enumerate(tela):
    for repL, casa in enumerate(linha):
      if repL != 2: 
        print(casa, end='|')
      else: 
        print(casa, end='\n')
    if rep != 2:
      print('-----------')

def layoutTela():
  initial_tela = [['','',''] for _ in range(3)]
  initial_tela = formatCasa(initial_tela)
  return initial_tela