import pygame

class Joueur():
    def __init__(self, saut):
        self.hauteur = 500
        self.hauteurPassee = 500
        self.etat = "sol"
        self.cpt = 0
        self.enCollision = False
        self.score = 0
        self.mort = False
        self.image = pygame.image.load("./Assets/Perso1.png").convert_alpha()
        self.saut_sound = saut

    def saut(self):
        if self.etat == "sol":
            self.saut_sound.play()
            self.cpt = 20
            self.etat = "monte"

    def update(self, obsHitBoxes, blocsHitBoxes, fenetre, perso, Pause, Mort):
        if Pause == False and Mort == False:
            self.score += 1
            persoHitBox = perso.get_rect()
            persoHitBox.topleft = 300, self.hauteur
            if self.etat == "monte":
                if self.cpt != 0:
                    self.hauteur -= self.cpt
                    self.cpt -= 1
                else:
                    self.etat = "tombe"
            for hitBoxes in obsHitBoxes:
                if hitBoxes.colliderect(persoHitBox):
                    self.mort = True
            total = 0
            for hitBoxes in blocsHitBoxes:
                if hitBoxes.colliderect(persoHitBox):
                    if self.etat != "monte":
                        self.hauteur = hitBoxes.top - 99
                        self.etat = "sol"
                        self.cpt = 0
                    if self.hauteurPassee + 98 > hitBoxes.top and hitBoxes.left == 340:
                        self.mort = True
                else:
                    total += 1
                if self.etat == "tombe" and hitBoxes.top - self.hauteur - 99 < -self.cpt and hitBoxes.left < 400 and hitBoxes.right > 300:
                    self.cpt = -(hitBoxes.top - self.hauteur - 99)
                if total == len(blocsHitBoxes) and self.etat == "sol" and self.hauteur < 500:
                    self.etat = "tombe"
            if self.etat == "tombe":
                if 500 - self.hauteur < -self.cpt:
                    self.cpt = -(500 - self.hauteur)
                elif self.hauteur < 500:
                    self.hauteur -= self.cpt
                    self.cpt -= 1
                else:
                    self.hauteur = 500
                    self.etat = "sol"
            self.hauteurPassee = self.hauteur
            fenetre.blit(perso, (300, self.hauteur))

    def getCoord(self):
        return 300, self.hauteur

    def getScore(self):
        return self.score

    def getMort(self):
        return self.mort

    def getImage(self):
        return self.image

    def getEtat(self):
        return self.etat
