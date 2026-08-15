
# Adiciona os espaços para os dados da matriz para ficar alinhado na tela 
def formatCasa(tela):
  for l in range(len(tela)):
    for c in range(len(tela[l])):
      if tela[l][c] == "" or tela[l][c] == '   ': 
        tela[l][c] = '   '
      else:
        if ' ' not in tela[l][c]:
          tela[l][c] = f' {tela[l][c]} '
  return tela


# Converte de 1 a 9 recebido pelo usuário para o indice da matriz
def converterJogada(jogada):
  match jogada:
      case 1:
        indice = [0,0]
      case 2:
        indice = [0,1]
      case 3:
        indice = [0,2]
      case 4:
        indice = [1,0]
      case 5:
        indice = [1,1]
      case 6:
        indice = [1,2]
      case 7:
        indice = [2,0]
      case 8:
        indice = [2,1]
      case 9:
        indice = [2,2]
  return indice
