Sequencia de código

primeira vez rodando -> entra no while repetir o jogo

define variaveis padrões: 
- tela -> matriz principal
- ocupado -> usado em formatCasa() para não colocar espaço denovo nos itens que já foram jogados (talvez compense tirar essa variavel e fazer uma verificação direta)
- casasOcupadas -> de 1 a 9 quais casas já foram ocupadas, recebe a casa ocupada em jogar() antes de formatar a casa

vai para o main()

main():
 atualiza a tela
 faz a chamada da função joga() uma das principais, concentra quase toda a lógica

joga ()