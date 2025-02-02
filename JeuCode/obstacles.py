import pygame

class Fond():
    def __init__(self):
        self.pos = 0

    def update(self, fenetre, background, Pause, Mort):
        if Pause == False and Mort == False:
            if self.pos >= -1260:
                self.pos -= 10
            else:
                self.pos = 0
            fenetre.blit(background, (self.pos, 0))
            fenetre.blit(background, (self.pos + 1280, 0))

class Pattern():
    def __init__(self, nb, pos=1280):
        self.pos = pos
        self.nb = nb
        self.obsHitBoxes = []
        self.blocsHitBoxes = []
        if self.nb == 0:
            self.posObstacles = [(5, 1), (11, 1)]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)]
        if self.nb == 1:
            self.posObstacles = [()]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)]
        if self.nb == 2:
            self.posObstacles = [()]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (8, 2), (9, 2), (10, 2), (11, 2)]
        if self.nb == 3:
            self.posObstacles = []
            self.posBlocs = [(0, 0), (1, 0), (10, 0), (11, 0), (0, 1), (1, 1), (10, 1), (11, 1)]
        if self.nb == 4:
            self.posObstacles = [(5, 0), (6, 0)]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (0, 1), (1, 1), (10, 1), (11, 1)]
        if self.nb == 5:
            self.posObstacles = [(2, 0), (3, 0), (4, 0), (7, 0), (8, 0), (9, 0)]
            self.posBlocs = [(0, 0), (1, 0), (5, 0), (6, 0), (10, 0), (11, 0), (0, 1), (1, 1), (5, 1), (6, 1), (10, 1), (11, 1)]
        if self.nb == 6:
            self.posObstacles = [(1, 0), (2, 0), (3, 0), (6, 0), (7, 0), (8, 0), (10, 0), (11, 0)]
            self.posBlocs = [(0, 0), (0, 1), (4, 0), (4, 1), (5, 0), (5, 1), (9, 0), (9, 1)]
        if self.nb == 7:
            self.posObstacles = [(0, 0), (1, 0), (10, 1), (11, 1)]
            self.posBlocs = [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)]
        if self.nb == 8:
            self.posObstacles = [(0, 0), (1, 0), (5, 1), (6, 1), (10, 2), (11, 2)]
            self.posBlocs = [(2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)]
        if self.nb == 9:
            self.posObstacles = [(1, 0), (2, 0), (3, 0), (5, 0), (6, 0), (7, 0), (9, 0), (10, 0), (11, 0)]
            self.posBlocs = [(0, 0), (4, 0), (8, 0), (4, 1), (8, 1), (8, 2)]
        if self.nb == 10:
            self.posObstacles = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (7, 0), (8, 0), (9, 0)]
            self.posBlocs = [(0, 0), (0, 1), (6, 0), (10, 0), (10, 1)]
        if self.nb == 11:
            self.posObstacles = [(1, 0), (2, 0), (3, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]
            self.posBlocs = [(0, 0), (4, 0), (10, 0), (4, 1)]
        if self.nb == 12:
            self.posObstacles = [(2, 1), (5, 1), (9, 1)]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (3, 1), (4, 1), (3, 2), (4, 2), (10, 1), (11, 1), (10, 2), (11, 2)]
        if self.nb == 13:
            self.posObstacles = [(1, 0), (2, 0), (3, 0), (10, 1)]
            self.posBlocs = [(0, 0), (4, 0), (10, 0), (4, 1)]
        if self.nb == 14:
            self.posObstacles = [(0, 1), (5, 2), (11, 2)]
            self.posBlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (5, 1), (11, 1)]

    def update(self, fenetre, obstacle, bloc, Pause, Mort):
        if Pause == False and Mort == False:
            self.obsHitBoxes = []
            self.blocsHitBoxes = []
            self.pos -= 10
            if self.posObstacles != [()]:
                for obs in self.posObstacles:
                    fenetre.blit(obstacle, (self.pos + obs[0] * 100, 500 - obs[1] * 100))
                    obsHitBox = obstacle.get_rect()
                    obsHitBox.width /= 2
                    obsHitBox.height /= 2
                    obsHitBox.topleft = self.pos + 25 + obs[0] * 100, 549 - obs[1] * 100
                    self.obsHitBoxes.append(obsHitBox)
            if self.posBlocs != [()]:
                for blocs in self.posBlocs:
                    fenetre.blit(bloc, (self.pos + blocs[0] * 100, 500 - blocs[1] * 100))
                    blocHitBox = bloc.get_rect()
                    blocHitBox.topleft = self.pos + blocs[0] * 100, 499 - blocs[1] * 100
                    self.blocsHitBoxes.append(blocHitBox)

    def getObsHitBoxes(self):
        return self.obsHitBoxes

    def getBlocsHitBoxes(self):
        return self.blocsHitBoxes

    def getPos(self):
        return self.pos
