#Anotações:

#Game loop:Basicamente consiste em inicializar o game e logo depois fazer todos os processos ou seja (prossedimentos) que são passados para o mesmo
#1 passo inicialização do game
#2 passo calcular as regras no caso verificar se a alguma redução de Hp ou algo parecido com isso !
#3 passo desenhar na tela no caso exibir o que foi feito na tela durante a jogada
#4 capturar eventos:capturar se o mouse foi precionado ou teclado
# 5 finalização:Quando basicamente o jogo da game over

#Tipos de eventos:

# Quit = ocorre quando o usuario clica no botão de fechar a tela
# Activeevent = Tela do pygame foi ativada ou escondida
# Keydown = Uma ou mais teclas foram precionadas
# Keyup = Uma ou mais teclas foram soltas
# Mousemotion = Mouse foi movido
# Mousebuttondown = Um ou mais botoes foram prencionados
# MousebuttonNup = um ou mais botões foram soltos
# Videoresize = Tela do pygame teve o tamanho alterado
# UserEvent = Ocorreu algum evento de usuario


#-------------------------------------------------#

# Propriedades dos eventos que vao ser utilizados

# Keydown = unicode,key,mod
# Keyup = Key,mod
# Mousemotion = pos,rel,buttons