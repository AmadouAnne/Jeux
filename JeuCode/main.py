import pygame
from pygame.locals import *
import os
import random
from character import Joueur
from obstacles import Pattern, Fond
from score import DisplayScore, AddScore
from menus import Menu, MenuScores, MenuPseudo, MenuPause, Write, Lettre

pygame.init()
clock = pygame.time.Clock()
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

pygame.display.set_caption("Interface Pygame")

fenetre = pygame.display.set_mode((1280, 720))
background = pygame.image.load(os.path.join('Assets', "Fond.jpg"))
perso = pygame.image.load(os.path.join('Assets', "Perso1.png")).convert_alpha()
obstacle = pygame.image.load(os.path.join('Assets', "Obstacle.png")).convert_alpha()
bloc = pygame.image.load(os.path.join('Assets', "Bloc.jpg"))
menuInterface = pygame.image.load(os.path.join('Assets', "Menu.jpg"))
guiInterface = pygame.image.load(os.path.join('Assets', "Gui.jpg"))
menuMortInterface = pygame.image.load(os.path.join('Assets', "MenuMort.jpg"))
menuScore = pygame.image.load(os.path.join('Assets', "MenuScore.jpg"))

saut = pygame.mixer.Sound(os.path.join('Assets', "Saut.mp3"))
pause = pygame.mixer.Sound(os.path.join('Assets', "Pause.mp3"))
mort = pygame.mixer.Sound(os.path.join('Assets', "Mort.mp3"))
pygame.mixer.music.load(os.path.join('Assets', "Musique.mp3"))
musique = pygame.mixer.music

persoHitBox = perso.get_rect()
font = pygame.font.SysFont("Broadway", 50)
score = 0
pseudo = ''
scores = []
Pause = True
Mort = False

MenuAfficher = True
MenuGui = False
clicMenu = False
clicGui = False
scoreMort = False
menu = 'menu'
nouvellePartie = False
clicMort = False
fichier = open("data.txt", "r")
a = fichier.readlines()

for i in range(len(a)):
    a[i] = a[i].replace("\n", "")
print(fichier.read())

for i in range(len(a) // 2):
    scores.append([int(a[i * 2])])
    scores[i].append(a[i * 2 + 1])
fichier.close()

joueur = Joueur(saut)
fond = Fond()
pattern1 = Pattern(1)
pattern2 = Pattern(2, 3080)
persocpt = 0
musiqueFin = False

continuer = True
while continuer:
    clock.tick(60)
    if menu == "menu":
        Menu(fenetre, menuInterface, font, globals())

    elif menu == "scores":
        MenuScores(fenetre, menuScore, font, scores)

    elif menu == 'pseudo':
        MenuPseudo(fenetre, menuMortInterface, font)
        Write(fenetre, font, pseudo)

    elif menu == 'pause':
        MenuPause(fenetre, guiInterface, font, globals())

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if menu == "pseudo":
                MenuPseudo(fenetre, menuMortInterface, font)
                lettre = event.key
                if len(pseudo) < 32:
                    if lettre == 8:
                        pseudo = pseudo[:-1]
                    elif lettre == 13:
                        scores = AddScore(scores, score, pseudo)
                        pseudo = ""
                        menu = 'menu'
                    else:
                        pseudo += Lettre(lettre)
                Write(fenetre, font, pseudo)
            if event.key == K_UP or event.key == MOUSEBUTTONDOWN or event.key == K_SPACE:
                if menu == 'jeu':
                    joueur.saut()
            elif event.key == K_ESCAPE:
                if menu == 'jeu':
                    Pause = not Pause
                    menu = 'pause'
                    pause.play()
                    musique.pause()
                elif menu == 'pause':
                    menu = "jeu"
                    Pause = not Pause
                    pause.play()
                    musique.unpause()
                elif menu == 'scores':
                    menu = 'menu'
        elif event.type == QUIT:
            continuer = False
    if score < 1000:
        alea = random.randint(0, 2)
    elif 1000 <= score < 2000:
        alea = random.randint(3, 5)
    elif 2000 <= score < 3000:
        alea = random.randint(6, 8)
    elif 3000 <= score < 4000:
        alea = random.randint(9, 11)
    else:
        alea = random.randint(12, 14)

    if nouvellePartie:
        joueur = Joueur(saut)
        fond = Fond()
        pattern1 = Pattern(1)
        pattern2 = Pattern(2, 3080)
        nouvellePartie = False
    score = joueur.getScore()
    Mort = joueur.getMort()
    if Mort:
        musique.stop()
        if menu == 'jeu':
            mort.play()
            lettre = ''
            menu = 'pseudo'
    persocpt += 1
    if joueur.getEtat() == "monte":
        perso = pygame.image.load(os.path.join('Assets', "PersoSaut.png")).convert_alpha()
    elif joueur.getEtat() == "tombe":
        perso = pygame.image.load(os.path.join('Assets', "Perso.png")).convert_alpha()
    else:
        if persocpt == 4:
            perso = pygame.image.load(os.path.join('Assets', "Perso1.png")).convert_alpha()
        if persocpt == 8:
            perso = pygame.image.load(os.path.join('Assets', "Perso2.png")).convert_alpha()
    if persocpt == 8:
        persocpt = 0
    persoHitBox.topleft = joueur.getCoord()
    fond.update(fenetre, background, Pause, Mort)
    if pattern1.getPos() < -1200:
        pattern1 = Pattern(alea, 2400)
    if pattern2.getPos() < -1200:
        pattern2 = Pattern(alea, 2400)
    pattern1.update(fenetre, obstacle, bloc, Pause, Mort)
    pattern2.update(fenetre, obstacle, bloc, Pause, Mort)
    obsHitBoxes1 = pattern1.getObsHitBoxes()
    blocsHitBoxes1 = pattern1.getBlocsHitBoxes()
    obsHitBoxes2 = pattern2.getObsHitBoxes()
    blocsHitBoxes2 = pattern2.getBlocsHitBoxes()
    if pattern1.getPos() < -1200:
        joueur.update(obsHitBoxes2, blocsHitBoxes2, fenetre, perso, Pause, Mort)
    elif pattern1.getPos() > 500:
        joueur.update(obsHitBoxes2, blocsHitBoxes2, fenetre, perso, Pause, Mort)
    else:
        joueur.update(obsHitBoxes1, blocsHitBoxes1, fenetre, perso, Pause, Mort)
    if menu == 'jeu':
        if not musique.get_busy():
            musique.play()
        DisplayScore(fenetre, font, score)
    pygame.display.update()
pygame.quit()
