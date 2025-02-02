import pygame

def DisplayScore(fenetre, font, score):
    scorestr = f'{score}'
    AfficherScore = font.render("SCORE: " + scorestr, 1, (0, 0, 0))
    fenetre.blit(AfficherScore, (1000 - (len(scorestr) * 20), 20))

def AddScore(ScoreList, score, pseudo):
    fichier = open("data.txt", "a")
    fichier.write(f'{score}')
    fichier.write("\n")
    fichier.write(pseudo)
    fichier.write("\n")
    if len(ScoreList) <= 10:
        ScoreList.append([score, pseudo])
    else:
        if ScoreList[9][0] < score:
            ScoreList.append([score, pseudo])
    ScoreList.sort()
    ScoreList.reverse()
    ScoreList = ScoreList[:10]
    fichier.close()
    return ScoreList
