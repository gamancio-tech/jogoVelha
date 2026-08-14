import os

# Adiciona os espaços para os dados da matriz para ficar alinhado na tela 
def formatCasa(matriz):
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] == "" or matriz[l][c] == '   ': 
        matriz[l][c] = '   '
      else:
        if matriz[l][c] not in ocupado:
          matriz[l][c] = f' {matriz[l][c]} '
  return matriz

# Faz o layout da tela de acordo com a matriz
def mostrarTela(tela):
  print(f'Pontos:\n Jogador 1 (X): {pontos[0]}\n Jogador 2 (O): {pontos[1]}\n'+'-'*20,'\n\n')
  for rep, linha in enumerate(tela):
    for repL, casa in enumerate(linha):
      if repL != 2: 
        print(casa, end="|")
      else: 
        print(casa, end="\n")
    if rep != 2:
      print('-----------')

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
    os._exit(0)

  if jogada not in range(1,10):
    return 'invalido'

  return jogada

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

# Junta as funções auxiliares e realiza a adição do input na matriz 
def jogar(mudarQmJoga = True):
  global tela
  global quemJoga

  try:
    quemJoga = verifQuemJoga(mudarQmJoga, quemJoga)
  except:
    quemJoga = verifQuemJoga(mudarQmJoga)

  jogada = receberJogada()
  if jogada == 'invalido': return False

  i = converterJogada(jogada)
  if i not in casasOcupadas:
    casasOcupadas.append(i)
  else: return False
  
  tela[i[0]][i[1]] = quemJoga
  tela = formatCasa(tela)
  ocupado.append(tela[i[0]][i[1]])

  return 

# Verifica se o alguém ganhou ou deu velha
def verificarGanho():
  if len(casasOcupadas) == 9:
    return 'velha'
  
  diagonal = []
  contraDiagonal = []
  for l in range(len(tela)):
    diagonal.append(tela[l][l])
    contraDiagonal.append(tela[l][len(tela[l])-1-l])

    # linhas
    if tela[l][0] == tela[l][1] == tela[l][2] and tela[l][0] != '   ': 
      if tela[l][0] == ' X ':
        return 'X'
      else:
        return 'O'
    # colunas
    if tela[0][l] == tela[1][l] == tela[2][l] and tela[0][l] != '   ':
      if tela[0][l] == ' X ':
        return 'X'
      else:
        return 'O'
    
  if diagonal == [' X ', ' X ', ' X ']: return 'X'
  if diagonal == [' O ', ' O ', ' O ']: return 'O'
  if contraDiagonal == [' X ', ' X ', ' X ']: return 'X'
  if contraDiagonal == [' O ', ' O ', ' O ']: return 'O'

  return False

# Atualiza a tela e chama o jogar()
# mudarQmJoga é passado duas funções a frente para verifQuemJoga()
def main(mudarQmJoga=True):
  os.system('cls')
  mostrarTela(tela)

  jogadaValida = jogar(mudarQmJoga)

  if jogadaValida != None:
    input('Jogada invalida!')
    return main(False) # parametro False para não mudar o print de quem é a vez

  game = verificarGanho()
  if game != False:
    os.system('cls')
    mostrarTela(tela)
    if game == 'velha':
      input(f'\nDeu velha!')
    else:
      input(f'\nO jogador {game} ganhou!')
      if game == 'X':
        pontos[0] += 1
      else:
        pontos[1] += 1
    return

  return main()



# ===================
#   Repetir o jogo
# ===================
pontos = [0,0]
continuar = True
while continuar:

  os.system('cls')

  # variaveis iniciais 
  ocupado = []
  casasOcupadas = []
  tela = [['','',''] for _ in range(3)]
  tela = formatCasa(tela)

  # Roda
  main()

  # Quando acaba
  continuar = input('Deseja cotinuar? [s/n] ')
  if continuar.lower() == 'n':
    continuar = False
