import pygame

def Menu(fenetre, menuInterface, font, global_vars):
    global menu, clicMenu, nouvellePartie, Pause, MenuAfficher, MenuGui
    menu = global_vars['menu']
    Pause = global_vars['Pause']
    MenuAfficher = global_vars['MenuAfficher']
    MenuGui = global_vars['MenuGui']
    fenetre.blit(menuInterface, (0, 0))

    text_commencer = font.render("Commencer", True, (0, 0, 0))
    text_scores = font.render("Scores", True, (0, 0, 0))

    commencer_rect = text_commencer.get_rect(center=(640, 360))
    scores_rect = text_scores.get_rect(center=(640, 460))

    fenetre.blit(text_commencer, commencer_rect)
    fenetre.blit(text_scores, scores_rect)

    if commencer_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            global_vars['menu'] = 'jeu'
            global_vars['nouvellePartie'] = True
            global_vars['MenuAfficher'] = False
            global_vars['MenuGui'] = False
            global_vars['Pause'] = False
            pygame.mouse.set_pos(675, 100)
            pygame.mixer.music.play()

    if scores_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            global_vars['menu'] = 'scores'
            pygame.mouse.set_pos(675, 100)

def MenuScores(fenetre, menuScore, font, scores):
    fenetre.blit(menuScore, (0, 0))
    Scores = font.render("Scores", 1, (0, 0, 0))
    fenetre.blit(Scores, (550, 20))
    if len(scores) > 0:
        length = min(len(scores), 10)
        for i in range(length):
            lscore = f'{scores[i][0]}'
            place = f'{i + 1}'
            DisplayRank = font.render(place, 1, (0, 0, 0))
            DisplayPseudo = font.render(scores[i][1], 1, (0, 0, 0))
            DisplayScoreList = font.render(lscore, 1, (0, 0, 0))
            fenetre.blit(DisplayRank, (50, 100 + i * 50))
            fenetre.blit(DisplayPseudo, (120, 100 + i * 50))
            fenetre.blit(DisplayScoreList, (1000, 100 + i * 50))

def MenuPseudo(fenetre, menuMortInterface, font):
    fenetre.blit(menuMortInterface, (0, 0))
    EntrerPseudo = font.render("Enter a name: ", 1, (0, 0, 0))
    fenetre.blit(EntrerPseudo, (450, 50))

def Lettre(lettre):
    if 33 <= lettre <= 126:
        lettre = chr(lettre)
        lettre = f'{lettre}'
    else:
        lettre = ""
    return lettre

def Write(fenetre, font, pseudo):
    DisplayPseudo = font.render(pseudo, 1, (0, 0, 0))
    fenetre.blit(DisplayPseudo, (50, 200))

def MenuPause(fenetre, guiInterface, font, global_vars):
    global Pause, clicGui, MenuAfficher, MenuGui, menu
    Pause = global_vars['Pause']
    menu = global_vars['menu']
    fenetre.blit(guiInterface, (0, 0))

    text_reprendre = font.render("Reprendr  e", True, (0, 0, 0))
    text_menu = font.render("Menu", True, (0, 0, 0))

    reprendre_rect = text_reprendre.get_rect(center=(640, 360))
    menu_rect = text_menu.get_rect(center=(640, 460))

    fenetre.blit(text_reprendre, reprendre_rect)
    fenetre.blit(text_menu, menu_rect)

    if reprendre_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            global_vars['Pause'] = False
            global_vars['menu'] = 'jeu'
            pygame.mouse.set_pos(675, 100)

    if menu_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            global_vars['menu'] = 'menu'
            pygame.mouse.set_pos(675, 100)
