# libraries needed

import pygame
import random
from pygame import transform
from pygame.constants import K_RIGHT, KEYUP, KEYDOWN, TEXTINPUT, K_a


# initialising
pygame.init ()

# mainscreen setup

screen_size = (500, 500)
mainscr = pygame.display.set_mode (screen_size)

pygame.display.set_caption ('Start-menu')

mainscr.fill ((30, 30, 30), rect = None)

# essential constants

icon = pygame.image.load ('ICON.ico')
pygame.display.set_icon (icon)

gameclock = pygame.time.Clock ()
gameclock.tick (120)

titlefont = pygame.font.Font ('freesansbold.ttf', 50)
normalfont = pygame.font.Font (None, 23)

song_n = random.randint (0, 8)
if song_n == 0 :
        song = pygame.mixer.Sound ('../../../../../Falling Deeper.mp3')
elif song_n == 1 :
        song = pygame.mixer.Sound ('Not Alone.mp3')
elif song_n == 2 :
        song = pygame.mixer.Sound ('Beside Me.mp3')
elif song_n == 3 :
        song = pygame.mixer.Sound ('carnage.mp3')
elif song_n == 4 :
        song = pygame.mixer.Sound ('Darkside.mp3')
elif song_n == 5 :
        song = pygame.mixer.Sound ('Focus.mp3')
elif song_n == 6 :
        song = pygame.mixer.Sound ('Ignite.mp3')
elif song_n == 7 :
        song = pygame.mixer.Sound ('Alchemy.mp3')
elif song_n == 8 :
        song = pygame.mixer.Sound ('Hunter.mp3')

color = ()

# loop variables

show_start = True
rungame = False

show_start = True
while show_start :
        for action in pygame.event.get () :
                if action.type == pygame.QUIT :
                        show_start = False

                if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :

                        pressed_key = pygame.key.get_pressed ()

                        if pressed_key [ pygame.K_ESCAPE ] :
                                show_start = False

                        if pressed_key [ pygame.K_RETURN ] :
                                rungame = True
                                show_start = False

        colorint = random.randint (0, 1)
        if colorint == 0 :
                color = (200, 1, 255)
        if colorint == 1 :
                color = (1, 150, 255)

        mainscr.fill ((20, 20, 30))
        mainscr.blit (titlefont.render ('Particle_Dodger', False, color), (70, 200))
        mainscr.blit (normalfont.render ('By - AKS', False, (255, 1, 50)), (350, 255))
        mainscr.blit (normalfont.render ('Hit Enter to continue', False, (255, 255, 255)), (70, 255))
        guide_str = "Controls :\nW-A-S-D or Arrow keys -> control player\nSpacebar -> Pause menu\n X key -> set player life to 0\nEscape -> Quit\n\n To change music :\nPause menu -> press n"
        mainscr.blit (normalfont.render ("Controls :", False, (255, 255, 255)), (70, 280))
        mainscr.blit (normalfont.render ("W-A-S-D or Arrow keys -> control player", False, (255, 255, 255)), (70, 300))
        mainscr.blit (normalfont.render ("Spacebar -> Pause menu", False, (255, 255, 255)), (70, 320))
        mainscr.blit (normalfont.render ("n on pause menu -> change music", False, (255, 255, 255)), (70, 340))
        mainscr.blit (normalfont.render ("X -> set player life to 0", False, (255, 255, 255)), (70, 360))
        mainscr.blit (normalfont.render ("Esc -> Quit", False, (255, 255, 255)), (70, 380))

        pygame.display.update ()
        pygame.display.flip ()
        gameclock.tick (25)

mainscr = pygame.display.set_mode (screen_size)
pygame.display.set_caption ("Game-Screen")

if rungame :
        mainscr.fill ((30, 30, 30))
        pygame.mixer.Sound.play (song)

        score = 0
        playerlife = 10
        playerx, playery = 0, 0
        playerhead = 0
        playerspeed = 1
        player = pygame.image.load ('Arrow.png')
        player = pygame.transform.scale (player, (20, 20))
        player = pygame.transform.rotate (player, 270)
        mainscr.blit (player, (playerx, playery))

        particle1 = pygame.image.load ('Particle.png')
        particle1x, particle1y = random.randint (0, 500), 0

        particle2 = pygame.image.load ('Particle.png')
        particle2x, particle2y = random.randint (0, 500), 0

        particle3 = pygame.image.load ('Particle.png')
        particle3x, particle3y = random.randint (0, 500), 0

        particle4 = pygame.image.load ('Particle.png')
        particle4x, particle4y = random.randint (0, 500), 0

        yparticlespeed = 0.5

        particle5 = pygame.image.load ('Particle.png')
        particle5x, particle5y = 0, random.randint (0, 500)

        particle6 = pygame.image.load ('Particle.png')
        particle6x, particle6y = 0, random.randint (0, 500)

        particle7 = pygame.image.load ('Particle.png')
        particle7x, particle7y = 0, random.randint (0, 500)

        particle8 = pygame.image.load ('Particle.png')
        particle8x, particle8y = 0, random.randint (0, 500)

        xparticlespeed = 0.5


        def pausegame () :
                pause = True

                while pause == True :

                        mainscr.fill ((30, 30, 50))

                        colorint = random.randint (0, 1)
                        if colorint == 0 :
                                color = (200, 1, 255)
                        if colorint == 1 :
                                color = (1, 150, 255)
                        mainscr.blit (titlefont.render ('Pause menu', False, color), (100, 230))
                        mainscr.blit (normalfont.render ('press SpaceBar to continue', False, (255, 200, 255)),
                                      (100, 280))
                        mainscr.blit (normalfont.render ('press n for next music', False, (255, 200, 255)), (100, 310))

                        for action in pygame.event.get () :
                                if action.type == pygame.QUIT :
                                        pause = False
                                        rungame = False

                                if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :
                                        action = pygame.key.get_pressed ()
                                        if action [ pygame.K_SPACE ] :
                                                pause = False
                                        if action [ pygame.K_n ] :

                                                pygame.mixer.stop ()
                                                song_n = random.randint (0, 8)
                                                if song_n == 0 :
                                                        song = pygame.mixer.Sound ('../../../../../Falling Deeper.mp3')
                                                elif song_n == 1 :
                                                        song = pygame.mixer.Sound ('Not Alone.mp3')
                                                elif song_n == 2 :
                                                        song = pygame.mixer.Sound ('Beside Me.mp3')
                                                elif song_n == 3 :
                                                        song = pygame.mixer.Sound ('carnage.mp3')
                                                elif song_n == 4 :
                                                        song = pygame.mixer.Sound ('Darkside.mp3')
                                                elif song_n == 5 :
                                                        song = pygame.mixer.Sound ('Focus.mp3')
                                                elif song_n == 6 :
                                                        song = pygame.mixer.Sound ('Ignite.mp3')
                                                elif song_n == 7 :
                                                        song = pygame.mixer.Sound ('Alchemy.mp3')
                                                elif song_n == 8 :
                                                        song = pygame.mixer.Sound ('Hunter.mp3')
                                                pygame.mixer.Sound.play (song)

                                        if action [ pygame.K_ESCAPE ] :
                                                pause = False
                                                rungame = False

                        pygame.display.update ()
                        pygame.display.flip ()
                        gameclock.tick (25)


        highscore = int (0)

while rungame :

        for action in pygame.event.get () :
                if action.type == pygame.QUIT :
                        rungame = False

                elif action.type == pygame.KEYDOWN :

                        pressed_key = pygame.key.get_pressed ()

                        if pressed_key [ pygame.K_x ] :
                                playerlife = 0.02

                        if pressed_key [ pygame.K_ESCAPE ] :
                                rungame = False

                        elif pressed_key [ pygame.K_SPACE ] :
                                pausegame ()

                        elif pressed_key [ pygame.K_DOWN ] or pressed_key [ pygame.K_s ] :
                                if playerhead == 0 :
                                        player = pygame.transform.rotate (player, 270)
                                elif playerhead == 90 :
                                        player = pygame.transform.rotate (player, 180)
                                elif playerhead == 180 :
                                        player = pygame.transform.rotate (player, 90)
                                elif playerhead == 270 :
                                        pass
                                playerhead = 270

                        elif pressed_key [ pygame.K_UP ] or pressed_key [ pygame.K_w ] :
                                if playerhead == 0 :
                                        player = pygame.transform.rotate (player, 90)
                                elif playerhead == 90 :
                                        pass
                                elif playerhead == 180 :
                                        player = pygame.transform.rotate (player, 270)
                                elif playerhead == 270 :
                                        player = pygame.transform.rotate (player, 180)
                                playerhead = 90

                        elif pressed_key [ pygame.K_RIGHT ] or pressed_key [ pygame.K_d ] :
                                if playerhead == 0 :
                                        pass
                                elif playerhead == 90 :
                                        player = pygame.transform.rotate (player, 270)
                                elif playerhead == 180 :
                                        player = pygame.transform.rotate (player, 180)
                                elif playerhead == 270 :
                                        player = pygame.transform.rotate (player, 90)
                                playerhead = 0

                        elif pressed_key [ pygame.K_LEFT ] or pressed_key [ pygame.K_a ] :
                                if playerhead == 0 :
                                        player = pygame.transform.rotate (player, 180)
                                elif playerhead == 90 :
                                        player = pygame.transform.rotate (player, 90)
                                elif playerhead == 180 :
                                        pass
                                elif playerhead == 270 :
                                        player = pygame.transform.rotate (player, 270)
                                playerhead = 180

        if playerhead == 0 :
                playerx += 1
        elif playerhead == 180 :
                playerx -= 1
        elif playerhead == 270 :
                playery += 1
        elif playerhead == 90 :
                playery -= 1

        if playerx > 500 :
                playerx = 0
        elif playerx < 0 :
                playerx = 500
        elif playery < 0 :
                playery = 500
        elif playery > 500 :
                playery = 0

        mainscr.fill ((30, 30, 30))

        mainscr.blit (player, (playerx, playery))

        mainscr.blit (particle1, (particle1x, particle1y))
        mainscr.blit (particle2, (particle2x, particle2y))
        mainscr.blit (particle3, (particle3x, particle3y))
        mainscr.blit (particle4, (particle4x, particle4y))
        mainscr.blit (particle5, (particle5x, particle5y))
        mainscr.blit (particle6, (particle6x, particle6y))
        mainscr.blit (particle7, (particle7x, particle7y))
        mainscr.blit (particle8, (particle8x, particle8y))

        particle1y += yparticlespeed
        particle2y += yparticlespeed - 0.05
        particle3y -= yparticlespeed + 0.08
        particle4y += yparticlespeed + 0.03

        particle5x += xparticlespeed
        particle6x -= xparticlespeed + 0.03
        particle7x -= xparticlespeed - 0.01
        particle8x += xparticlespeed - 0.03

        if particle1y > 500 :
                score += 1
                particle1y = 10
                particle1x = random.randint (0, 500)
                yparticlespeed += 0.02
                playerspeed += 0.02

        if particle2y > 500 :
                score += 1
                particle2y = 10
                particle2x = random.randint (0, 500)
                playerspeed += 0.02

        if particle3y < 0 :
                score += 1
                particle3y = 500
                particle3x = random.randint (0, 500)

        if particle4y > 500 :
                score += 1
                particle4y = 10
                particle4x = random.randint (0, 500)

        if particle5x > 500 :
                score += 1
                particle5x = 0
                particle5y = random.randint (0, 500)
                xparticlespeed += 0.01
                playerspeed += 0.005

        if particle6x < 0 :
                score += 1
                particle6x = 500
                particle6y = random.randint (0, 500)

        if particle7x < 0 :
                score += 1
                particle7x = 500
                particle7y = random.randint (0, 500)

        if particle8x > 500 :
                score += 1
                particle8x = 0
                particle8y = random.randint (0, 500)

        life_str = str (playerlife)
        if '.' in life_str :
                pointIndex = life_str.index ('.')
                end = pointIndex + 2
                life_str = life_str [ 0 :end ]

        mainscr.blit (normalfont.render (str ('Score : ' + str (score)), False, (150, 1, 255)), (2, 0))
        mainscr.blit (normalfont.render ('By - AKS :)', False, (150, 1, 255)), (400, 470))
        mainscr.blit (normalfont.render (str ('Player life : ' + life_str), False, (150, 1, 255)), (2, 20))
        if highscore != 0 :
                mainscr.blit (normalfont.render (str ('Highscore : ' + str (highscore)), False, (150, 1, 255)),
                              (2, 470))
        elif highscore == 0 :
                mainscr.blit (normalfont.render ('Playing for first time : no highscore yet', False, (150, 1, 250)),
                              (2, 470))

        if ((((playerx - particle1x) ** 2) + ((playery - particle1y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle2x) ** 2) + ((playery - particle2y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle3x) ** 2) + ((playery - particle3y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle4x) ** 2) + ((playery - particle4y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle5x) ** 2) + ((playery - particle5y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle6x) ** 2) + ((playery - particle6y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle7x) ** 2) + ((playery - particle7y) ** 2)) ** (1 / 2)) < 20 or \
                            ((((playerx - particle8x) ** 2) + ((playery - particle8y) ** 2)) ** (1 / 2)) < 20 :
                playerlife -= 0.01

        if playerlife < 0.1 :

                deathloop = True
                while deathloop == True :
                        rungame = False
                        mainscr.fill ((20, 20, 30))
                        colorint = random.randint (0, 1)
                        if colorint == 0 :
                                color = (150, 1, 255)
                        if colorint == 1 :
                                color = (1, 150, 255)
                        mainscr.blit (titlefont.render ("you've been killed :(", False, color), (50, 100))
                        mainscr.blit (titlefont.render ("you've been killed :(", False, color), (50, 100))
                        mainscr.blit (normalfont.render ("Ended up on score : " + str (score), False, (255, 255, 255)),
                                      (50, 170))
                        mainscr.blit (normalfont.render ("Press any key to continue", False, (255, 255, 255)),
                                      (50, 200))

                        for action in pygame.event.get () :
                                if action.type == pygame.QUIT :
                                        deathloop = False
                                        show_start = False
                                if action.type == pygame.KEYDOWN :
                                        show_start = True
                                        deathloop = False
                                        while show_start :
                                                for action in pygame.event.get () :
                                                        if action.type == pygame.QUIT :
                                                                show_start = False

                                                        if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :

                                                                pressed_key = pygame.key.get_pressed ()

                                                                if pressed_key [ pygame.K_ESCAPE ] :
                                                                        show_start = False

                                                                if pressed_key [ pygame.K_RETURN ] :
                                                                        rungame = True
                                                                        show_start = False
                                                                        deathloop = False
                                                                        playerlife = 10
                                                                        if score > highscore :
                                                                                highscore = score
                                                                        score = 0
                                                                        xparticlespeed = 0.5
                                                                        yparticlespeed = 0.5

                                                colorint = random.randint (0, 1)
                                                if colorint == 0 :
                                                        color = (200, 1, 255)
                                                if colorint == 1 :
                                                        color = (1, 150, 255)

                                                mainscr.fill ((30, 30, 30))
                                                mainscr.blit (titlefont.render ('Particle_Dodger', False, color),
                                                              (70, 200))
                                                mainscr.blit (normalfont.render ('By - AKS', False, (255, 1, 50)),
                                                              (350, 260))
                                                mainscr.blit (normalfont.render ('Hit Enter to continue', False,
                                                                                 (255, 255, 255)), (120, 255))

                                                pygame.display.update ()
                                                pygame.display.flip ()
                                                gameclock.tick(25)

                        pygame.display.update ()
                        gameclock.tick(25)

        pygame.display.update ()

        gameclock.tick (25)

quit ()
