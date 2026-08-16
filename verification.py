# Verifica casas ocupadas e quem ocupa
# @param reset -> reseta as variaveis

casasOcupadas = []

def verificarCasasOcupadas(reset, casaJogada = None):
  global casasOcupadas

  if reset:
    casasOcupadas = []
    return

  if casaJogada not in casasOcupadas:
    casasOcupadas.append(casaJogada)
    return True
  else: return False


# Faz o print de quem é a vez de jogar e muda de acordo com o aterior
# @param mudar -> muda quem joga só se for true
def verifQuemJoga(mudar=True, quemJoga='O'):
  print('\nVez de jogador', end=' ')
  if quemJoga == 'O':
    if mudar:
      quemJoga = 'X'
      print('1')
    else:
      print('2') # Precisa ser invertido para continuar o que era antes
  else:
    if mudar:
      quemJoga = "O"
      print('2')
    else:
      print('1')

  return quemJoga

# Verifica se o alguém ganhou ou deu velha
def verificarGanho(tela):
  diagonal = []
  contraDiagonal = []
  
  for l in range(len(tela)):
    diagonal.append(tela[l][l])
    contraDiagonal.append(tela[l][len(tela[l])-1-l])

    # Linhas
    if tela[l][0] == tela[l][1] == tela[l][2] and tela[l][0] != '   ': 
      if tela[l][0] == ' X ':
        return 'X'
      else:
        return 'O'

    # Colunas
    if tela[0][l] == tela[1][l] == tela[2][l] and tela[0][l] != '   ':
      if tela[0][l] == ' X ':
        return 'X'
      else:
        return 'O'
    
  # Diagonais
  if diagonal == [' X ', ' X ', ' X '] or contraDiagonal == [' X ', ' X ', ' X ']: return 'X'
  if diagonal == [' O ', ' O ', ' O '] or contraDiagonal == [' O ', ' O ', ' O ']: return 'O'

  # Velha
  if len(casasOcupadas) == 9:
    return 'velha'
  
  return False

