import pygame
from pygame.locals import *
import os
import random
pygame.init()
clock = pygame.time.Clock()
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

pygame.display.set_caption("Interface Pygame")

#Importation de toutes les images

fenetre = pygame.display.set_mode((1280, 720))
background = pygame.image.load(os.path.join('Assets',"Fond.jpg"))
perso = pygame.image.load(os.path.join('Assets',"Perso1.png")).convert_alpha()
obstacle = pygame.image.load(os.path.join('Assets',"Obstacle.png")).convert_alpha()
bloc = pygame.image.load(os.path.join('Assets',"Bloc.jpg"))
menuInterface = pygame.image.load(os.path.join('Assets',"Menu.jpg"))
guiInterface = pygame.image.load(os.path.join('Assets',"Gui.jpg"))
menuMortInterface = pygame.image.load(os.path.join('Assets',"MenuMort.jpg"))
menuScore = pygame.image.load(os.path.join('Assets',"MenuScore.jpg"))

#Importation des fichiers audios

saut = pygame.mixer.Sound(os.path.join('Assets',"Saut.mp3"))
pause = pygame.mixer.Sound(os.path.join('Assets',"Pause.mp3"))
mort = pygame.mixer.Sound(os.path.join('Assets',"Mort.mp3"))
pygame.mixer.music.load(os.path.join('Assets',"Musique.mp3"))
musique=pygame.mixer.music

persoHitBox=perso.get_rect()
obstacleHitBox=obstacle.get_rect()
blocHitBox=bloc.get_rect()

font = pygame.font.SysFont("Broadway", 50)
score = 0
pseudo=''
scores=[]
Pause=True
Mort=False

MenuAfficher=True
MenuGui=False
clicMenu=False
clicGui=False
scoreMort=False
menu='menu'
nouvellePartie=False
clicMort=False
fichier = open("data.txt", "r")
a = fichier.readlines()

for i in range(len(a)):
    a[i] = a[i].replace("\n","")
print(fichier.read())

for i in range(len(a)//2):
    scores.append([int(a[i*2])])
    scores[i].append(a[i*2+1])
fichier.close()

def MenuScores():
    fenetre.blit(menuScore,(0,0))
    Scores = font.render("Scores", 1, (0, 0, 0))
    fenetre.blit(Scores, (550,20))
    if len(scores) > 0:
        if len(scores) <=10:
            length=len(scores) 
        else:
            length=10
        for i in range(length):
            lscore = f'{scores[i][0]}'
            place = f'{i + 1}'
            DisplayRank = font.render(place, 1, (0, 0, 0))
            DisplayPseudo = font.render(scores[i][1], 1, (0, 0, 0))
            DisplayScoreList = font.render(lscore, 1, (0, 0, 0))
            fenetre.blit(DisplayRank, (50, 100 + i * 50))
            fenetre.blit(DisplayPseudo, (120, 100 + i * 50))
            fenetre.blit(DisplayScoreList, (1000, 100 + i * 50))
    return

def DisplayScore(score):
    if joueur.mort==False and MenuAfficher==False and MenuGui==False:
        scorestr = f'{score}'
        AfficherScore = font.render("SCORE: "+scorestr, 1, (0,0,0))
        fenetre.blit(AfficherScore,(1000-(len(scorestr)*20),20))

def MenuPseudo():
    fenetre.blit(menuMortInterface, (0, 0))
    EntrerPseudo = font.render("Enter a name: ", 1, (0,0,0))
    fenetre.blit(EntrerPseudo, (450, 50))
    return

def Lettre(lettre):
    if 33 <= lettre <= 126:
        lettre = chr(lettre)
        lettre = f'{lettre}'
    else:
        lettre = ""
    return lettre

def Write(pseudo):
    DisplayPseudo = font.render(pseudo, 1, (0,0,0))
    fenetre.blit(DisplayPseudo, (50, 200))
    return

def AddScore(ScoreList, score, pseudo):
    fichier=open("data.txt","a")
    fichier.write(f'{score}')
    fichier.write("\n")
    fichier.write(pseudo)
    fichier.write("\n")
    if len(ScoreList) <= 10:
        ScoreList.append([score, pseudo])
    else:
        if ScoreList[9][0]<score:
            ScoreList.append([score, pseudo])
    ScoreList.sort()
    ScoreList.reverse()
    ScoreList = ScoreList[0:10]
    fichier.close()
    return ScoreList

def Menu():
    global ROUGE,BLEU,clicMenu,Pause,continuer,MenuAfficher,MenuGui,scores,menu,nouvellePartie
    left=640
    top=360
    width=500
    height=150
    fenetre.blit(menuInterface,(0,0))
    Bloc3=(640-width/2,360-height,width,height)
        
    
    Bouton_rect3=pygame.Rect(Bloc3)
        
    text3 = font.render("Commencer", True, (0, 0, 0))
    menuInterface.blit(text3, (width // 1 - text3.get_width() // 10, 250))
    
    Bloc4=(640-width/2,600-height,width,height)
        
    
    Bouton_rect4=pygame.Rect(Bloc4)
    
    text4 = font.render("Scores", True, (0, 0, 0))
    menuInterface.blit(text4, (width // 1 - text4.get_width() // 10, 500))

    if Bouton_rect3.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            menu='jeu'
            nouvellePartie=True
            MenuAfficher=False
            MenuGui=False
            Pause=False
            pygame.mouse.set_pos(675,100)
            musique.play()
    
    if Bouton_rect4.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            menu='scores'
            pygame.mouse.set_pos(675,100)

def MenuPause():
    global ROUGE,BLEU,Pause,clicGui,MenuAfficher,MenuGui,menu
    left=640
    top=360
    width=500
    height=150
    fenetre.blit(guiInterface,(0,0))
    Bloc=(640-width/2,360-height,width,height)
        
    
    Bouton_rect=pygame.Rect(Bloc)
        
    Bloc2=(640-width/2,600-height,width,height)
        
    
    Bouton_rect2=pygame.Rect(Bloc2)
        
    if Bouton_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            Pause=False
            menu='jeu'
            pygame.mouse.set_pos(675,100)
            
    if Bouton_rect2.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            menu='menu'
            pygame.mouse.set_pos(675,100)
        
    text = font.render("Reprendre", True, (0, 0, 0))
    guiInterface.blit(text, (width // 1 - text.get_width() // 10, 250))
        
    text2 = font.render("Menu", True, (0, 0, 0))
    guiInterface.blit(text2, (width // 1 - text2.get_width() // 10, 500))

def DisplayScore(score):
    scorestr = f'{score}'
    AfficherScore = font.render("SCORE: "+scorestr, 1, (0,0,0))
    fenetre.blit(AfficherScore,(1000-(len(scorestr)*20),20))

class Joueur():
    def __init__(self):
        self.hauteur=500
        self.hauteurPassee=500
        self.etat="sol"
        self.cpt=0
        self.enCollision=False
        self.score=0
        self.mort=False
        self.image=pygame.image.load("./Assets/Perso1.png").convert_alpha()
        
    def saut(self):
        if self.etat=="sol":
            saut.play()
            self.cpt=20
            self.etat="monte"

    def update(self,obsHitBoxes,blocsHitBoxes):
        if Pause==False and Mort==False:
            self.score+=1
            persoHitBox=perso.get_rect()
            persoHitBox.topleft=300,self.hauteur
            if self.etat=="monte":
                if self.cpt!=0:
                    self.hauteur-=self.cpt
                    self.cpt-=1
                else:
                    self.etat="tombe"
            for hitBoxes in obsHitBoxes:
                if hitBoxes.colliderect(persoHitBox)==True:
                    self.mort=True
            total=0
            for hitBoxes in blocsHitBoxes:
                if hitBoxes.colliderect(persoHitBox)==True:
                    if self.etat!="monte":
                        self.hauteur=hitBoxes.top-99
                        self.etat="sol"
                        self.cpt=0
                    if self.hauteurPassee+98>hitBoxes.top and hitBoxes.left==340:
                        print("mort")
                        self.mort=True
                else:
                    total+=1
                if self.etat=="tombe" and hitBoxes.top-self.hauteur-99<-self.cpt and hitBoxes.left<400 and hitBoxes.right>300:
                    self.cpt=-(hitBoxes.top-self.hauteur-99)
                if total==len(blocsHitBoxes) and self.etat=="sol" and self.hauteur<500:
                    self.etat="tombe"
            if self.etat=="tombe":
                if 500-self.hauteur<-self.cpt:
                    self.cpt=-(500-self.hauteur)
                elif self.hauteur<500:
                    self.hauteur-=self.cpt
                    self.cpt-=1
                else:
                    self.hauteur=500
                    self.etat="sol"
            self.hauteurPassee=self.hauteur
            fenetre.blit(perso,(300,self.hauteur))
    
    def getCoord(self):
        return 300,self.hauteur
    
    def getScore(self):
        return self.score
    
    def getMort(self):
        return self.mort
    
    def getImage(self):
        return self.image

    def getEtat(self):
        return self.etat
            
class Fond():
    def __init__(self):
        self.pos=0

    def update(self):
        if Pause==False and Mort==False:
            if self.pos>=-1260:
                self.pos-=10
            else:
                self.pos=0
            fenetre.blit(background,(self.pos,0))
            fenetre.blit(background,(self.pos+1280,0))

class Pattern():
    def __init__(self,nb,pos=1280):
        self.pos=pos
        self.nb=nb
        self.obsHitBoxes=[]
        self.blocsHitBoxes=[]
        if self.nb==0:
            self.posObstacles=[(5,1),(11,1)]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0)]
        if self.nb==1:
            self.posObstacles=[()]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1)]
        if self.nb==2:
            self.posObstacles=[()]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(8,2),(9,2),(10,2),(11,2)]
        if self.nb==3:
            self.posObstacles=[]
            self.posBlocs=[(0,0),(1,0),(10,0),(11,0),(0,1),(1,1),(10,1),(11,1)]
        if self.nb==4:
            self.posObstacles=[(5,0),(6,0)]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(7,0),(8,0),(9,0),(10,0),(11,0),(0,1),(1,1),(10,1),(11,1)]
        if self.nb==5:
            self.posObstacles=[(2,0),(3,0),(4,0),(7,0),(8,0),(9,0)]
            self.posBlocs=[(0,0),(1,0),(5,0),(6,0),(10,0),(11,0),(0,1),(1,1),(5,1),(6,1),(10,1),(11,1)]
        if self.nb==6:
            self.posObstacles=[(1,0),(2,0),(3,0),(6,0),(7,0),(8,0),(10,0),(11,0)]
            self.posBlocs=[(0,0),(0,1),(4,0),(4,1),(5,0),(5,1),(9,0),(9,1)]
        if self.nb==7:
            self.posObstacles=[(0,0),(1,0),(10,1),(11,1)]
            self.posBlocs=[(6,0),(7,0),(8,0),(9,0),(10,0),(11,0)]
        if self.nb==8:
            self.posObstacles=[(0,0),(1,0),(5,1),(6,1),(10,2),(11,2)]
            self.posBlocs=[(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(7,1),(8,1),(9,1),(10,1),(11,1)]
        if self.nb==9:
            self.posObstacles=[(1,0),(2,0),(3,0),(5,0),(6,0),(7,0),(9,0),(10,0),(11,0)]
            self.posBlocs=[(0,0),(4,0),(8,0),(4,1),(8,1),(8,2)]
        if self.nb==10:
            self.posObstacles=[(1,0),(2,0),(3,0),(4,0),(5,0),(7,0),(8,0),(9,0)]
            self.posBlocs=[(0,0),(0,1),(6,0),(10,0),(10,1)]
        if self.nb==11:
            self.posObstacles=[(1,0),(2,0),(3,0),(5,0),(6,0),(7,0),(8,0),(9,0)]
            self.posBlocs=[(0,0),(4,0),(10,0),(4,1)]
        if self.nb==12:
            self.posObstacles=[(2,1),(5,1),(9,1)]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(3,1),(4,1),(3,2),(4,2),(10,1),(11,1),(10,2),(11,2)]
        if self.nb==13:
            self.posObstacles=[(1,0),(2,0),(3,0),(10,1)]
            self.posBlocs=[(0,0),(4,0),(10,0),(4,1)]
        if self.nb==14:
            self.posObstacles=[(0,1),(5,2),(11,2)]
            self.posBlocs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(5,1),(11,1)]
        

    def update(self):
        if Pause==False and Mort==False:
            self.obsHitBoxes=[]
            self.blocsHitBoxes=[]
            self.pos-=10
            if self.posObstacles!=[()]:
                for obs in self.posObstacles:
                    fenetre.blit(obstacle,(self.pos+obs[0]*100,500-obs[1]*100))
                    obsHitBox=obstacle.get_rect()
                    obsHitBox.width/=2
                    obsHitBox.height/=2
                    obsHitBox.topleft=self.pos+25+obs[0]*100,549-obs[1]*100
                    self.obsHitBoxes.append(obsHitBox)
            if self.posBlocs!=[()]:
                for blocs in self.posBlocs:
                    fenetre.blit(bloc,(self.pos+blocs[0]*100,500-blocs[1]*100))
                    blocHitBox=bloc.get_rect()
                    blocHitBox.topleft=self.pos+blocs[0]*100,499-blocs[1]*100
                    self.blocsHitBoxes.append(blocHitBox)
    
    def getObsHitBoxes(self):
        return self.obsHitBoxes
    
    def getBlocsHitBoxes(self):
        return self.blocsHitBoxes

    def getPos(self):
        return self.pos
    
joueur=Joueur()
fond=Fond()
pattern1=Pattern(1)
pattern2=Pattern(2,3080)
persocpt=0
musiqueFin=False
    
continuer = True
while continuer :
    clock.tick(60)
    if menu == "menu":
        Menu()

    elif menu == "scores":
        MenuScores()

    elif menu=='pseudo':
        MenuPseudo()
        Write(pseudo)
    
    elif menu=='pause':
        MenuPause()

    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if menu == "pseudo":
                MenuPseudo()
                lettre = event.key  
                if len(pseudo) < 32:
                    if lettre == 8:
                        pseudo = pseudo[:-1]
                    elif lettre==13:
                        scores = AddScore(scores, score, pseudo)
                        pseudo = ""
                        menu='menu'
                    else:
                        pseudo += Lettre(lettre)
                Write(pseudo)
            if event.key==K_UP or event.key==MOUSEBUTTONDOWN or event.key==K_SPACE:
                if menu=='jeu':
                    joueur.saut()
                
            elif event.key==K_ESCAPE:
                if menu=='jeu':
                    Pause=not Pause
                    menu='pause'
                    pause.play()
                    musique.pause()
                elif menu=='pause':
                    menu="jeu"
                    Pause=not Pause
                    pause.play()
                    musique.unpause()
                elif menu=='scores':
                    menu='menu'
            
        elif event.type == QUIT:
            continuer = False
    if score<1000:
        alea=random.randint(0,2)
    elif 1000<=score<2000:
        alea=random.randint(3,5)
    elif 2000<=score<3000:
        alea=random.randint(6,8)
    elif 3000<=score<4000:
        alea=random.randint(9,11)
    else:
        alea=random.randint(12,14)
    
    if nouvellePartie==True:
        joueur=Joueur()
        fond=Fond()
        pattern1=Pattern(1)
        pattern2=Pattern(2,3080)
        nouvellePartie=False
    score=joueur.getScore()
    Mort=joueur.getMort()
    if Mort == True:
        musique.stop()
        if menu=='jeu':
            mort.play()
            lettre=''
            menu='pseudo'
    persocpt+=1
    if joueur.getEtat()=="monte":
        perso=pygame.image.load(os.path.join('Assets',"PersoSaut.png")).convert_alpha()
    elif joueur.getEtat()=="tombe":
        perso=pygame.image.load(os.path.join('Assets',"Perso.png")).convert_alpha()
    else:
        if persocpt==4:
            perso=pygame.image.load(os.path.join('Assets',"Perso1.png")).convert_alpha()
        if persocpt==8:
            perso=pygame.image.load(os.path.join('Assets',"Perso2.png")).convert_alpha()
    if persocpt==8:
        persocpt=0
    persoHitBox.topleft=joueur.getCoord()
    fond.update()
    if pattern1.getPos()<-1200:
        pattern1=Pattern(alea,2400)
    if pattern2.getPos()<-1200:
        pattern2=Pattern(alea,2400)
    pattern1.update()
    pattern2.update()
    obsHitBoxes1=pattern1.getObsHitBoxes()
    blocsHitBoxes1=pattern1.getBlocsHitBoxes()
    obsHitBoxes2=pattern2.getObsHitBoxes()
    blocsHitBoxes2=pattern2.getBlocsHitBoxes()
    if pattern1.getPos()<-1200:
        joueur.update(obsHitBoxes2,blocsHitBoxes2)
    elif pattern1.getPos()>500:
        joueur.update(obsHitBoxes2,blocsHitBoxes2)
    else:
        joueur.update(obsHitBoxes1,blocsHitBoxes1)
    if menu=='jeu':
        if musique.get_busy()==False:
            musique.play()
        DisplayScore(score)
    pygame.display.update()
pygame.quit()
