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

  return main()

# Verifica se o alguém ganhou ou deu velha
def verificarGanho():
  if len(casasOcupadas):
    return 'velha'

# Atualiza a tela e chama o jogar()
# mudarQmJoga é passado duas funções a frente para verifQuemJoga()
def main(mudarQmJoga=True):
  os.system('cls')
  mostrarTela(tela)

  jogadaValida = True 
  jogadaValida = jogar(mudarQmJoga)

  if not jogadaValida:
    input('Jogada invalida!')
    return main(False) # parametro False para não mudar o print de quem é a vez



# ===================
#   Repetir o jogo
# ===================

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
