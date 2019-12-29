try:
    import pygame
except:
    print('O modulo nao foi instalado')
from random import randrange
pygame.init() # iniciacao do pygame

#####################################
# cores
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(173,216,230)
########################################

#####################
# largura e altura da tela
largura=640
altura=480
##########################
tamanho = 10 # tamanho para criacao da cobra


relogio = pygame.time.Clock() 
fundo = pygame.display.set_mode((largura,altura)) # criacao da tela
placar = 40 # tamanho para criacao do placar

pygame.display.set_caption("Snake") # nome do jogo


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam) # fonte da escrita 
    texto1 = font.render(msg, True, cor) # texto a ser escrito
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho]) # criacao da cobra

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho]) # criacao da maca

def jogo():
    sair = True
    fimdejogo = False
    pos_x=randrange(0,largura-tamanho,10) # gerando numeros aleatorios de 0 a largura-tamanho passo 10 para a
    pos_y=randrange(0,altura-tamanho-placar,10) # gerando numeros aleatorios de 0 a altura-tamanho passo 10
    maca_x=randrange(0,largura-tamanho,10) # gerando numeros aleatorios de 0 a largura-tamanho passo 10
    maca_y=randrange(0,altura-tamanho-placar,10) # gerando numeros aleatorios de 0 a altura-tamanho passo 10
    velocidade_x=0 # velocidade inicial da cobra eixo x
    velocidade_y=0 # velocidade inicial da cobra eixo y
    CobraXY = [] # lista para criacao da cobra vazia
    CobraComp = 1
    pontos = 0
    qt_maca = 0
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x=randrange(0,largura-tamanho,10)
                        pos_y=randrange(0,altura-tamanho-placar,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho-placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                    	sair = False
                    	fimdejogo = False
                    
                        
            fundo.fill(azul)
            texto("Fim de jogo", vermelho, 50, 65, 30)
            texto('Pontuação final: '+str(pontos)+' pontos',preto,50,65,80)
            texto("Para continuar tecle C ou S para sair", vermelho, 32, largura/10, altura/2)
            if qt_maca == 4:
                fundo.fill(azul)
                texto('Parabens voce Ganhou ',vermelho,50,10,altura-30)
                texto("Para continuar tecle C ou S para sair", vermelho, 32, largura/10, altura/2)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
        if sair:
	        fundo.fill(azul)
	        pos_x+=velocidade_x
	        pos_y+=velocidade_y

        
        
        
        
        
       ##############################################################
       # para criar uma nova maca quando a cobra 
        if pos_x == maca_x and pos_y == maca_y:    
            maca_x=randrange(0,largura-tamanho,10)
            maca_y=randrange(0,altura-tamanho-placar,10)
            CobraComp += 1
            pontos+=5
            qt_maca +=1
            
        if pos_x + tamanho > largura:
            fimdejogo = True
        if pos_x < 0:
            fimdejogo = True
        if pos_y + tamanho > altura - 42:
            fimdejogo = True
        if pos_y < 0:
           fimdejogo = True
        
        if qt_maca == 4:
            fimdejogo = True
        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True
        pygame.draw.rect(fundo, branco, [0, altura-placar, largura, placar]) # retangulo x,y,largura,altura
        texto('Pontuação: '+str(pontos),verde,40,10,altura-30)
        cobra(CobraXY)
        maca(maca_x,maca_y)
        pygame.display.update()
        relogio.tick(15)

jogo()
pygame.quit()
