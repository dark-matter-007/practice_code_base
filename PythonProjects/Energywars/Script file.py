import pygame, time, math, random, pickle
from pygame.locals import *
import databalancer


# initialising
pygame.init ()
pygame.mixer.init ()

# base setup
mainscr = pygame.display.set_mode ((700, 500))
#mainscr.fill ('#000000')

# prop images
RTC = pygame.image.load ('RTC.png')
RTCrect = RTC.get_rect ()

RGC = pygame.image.load ('RedGlow.png')
RGCrect = RGC.get_rect ()

BGC = pygame.image.load ('BlueGlow.png')
BGCrect = BGC.get_rect ()

RBC = pygame.image.load ('Bullet.png')
RBC = pygame.transform.smoothscale (RBC, (10, 10))
RBCrect = RBC.get_rect ()

WGC = pygame.image.load ('WhiteGlow.png')
WGC = pygame.transform.smoothscale (WGC, (30, 30))
WGCrect = WGC.get_rect ()

# misc images
logoimg = pygame.image.load ('LOGO.png')
logoimgrect = logoimg.get_rect ()
logoimgrect.center = (600, 400)

logoico = pygame.image.load ('LOGOICO.png')
pygame.display.set_icon (logoico)

pygame.display.set_caption ('AKS Official.exe', ' a ')

# audio files
pygame.mixer.music.load (
                    r'CJ - WHOOPTY (ERS Remix) _ JOKER SCENE _ 4K(MP3_320K).mp3')
pygame.mixer.music.play (1, start = 31, fade_ms = 2)

# global constants
Main = True
gameclock = pygame.time.Clock ()
gameclock.tick (1200)


# fonts
normalfont = pygame.font.SysFont ('Orbitron', 23)
largefont = pygame.font.SysFont ('Orbitron', 30)
tinyfont = pygame.font.SysFont ('Orbitron', 10)

pygame.mouse.set_visible (False)


# intro screen
def introtext () :
        R, B, G = 1, 1, 1
        showIT = True
        while showIT :
                if R < 255 :
                        R += 1
                        G += 1
                        B += 1
                textcolour = (R, G, B)
                Text = normalfont.render ('Ashwin Sharma creations',False, textcolour)
                textrect = Text.get_rect ()
                textrect.center = ((350, 250))
                mainscr.blit (Text, textrect)
                pygame.draw.rect (mainscr, textcolour, (175, 230, 350, 40), width = 2, border_radius = 10)
                pygame.display.flip ()
                if R >= 255 :
                        time.sleep (2)
                        while R > 0 :
                                R -= 1
                                G -= 1
                                B -= 1
                                textcolour = (R, G, B)
                                Text = normalfont.render ('Ashwin Sharma creations', False, textcolour)
                                textrect = Text.get_rect ()
                                textrect.center = ((350, 250))
                                mainscr.blit (Text, textrect)
                                pygame.draw.rect (mainscr, textcolour, (175, 230, 350, 40), width = 2,
                                                  border_radius = 10)
                                pygame.display.flip ()
                                time.sleep (0.01)

                        showIT = False

                time.sleep (0.03)
                pygame.display.update ()

        return print ('intro text executed')
introtext ()


# game screen
def startgame () :
        highscore = 1000
        asteroidlist, enemylist = [ ], [ ]

        def spawnenemy ( xpos, ypos ) :
                enemy = { 'xvelo' : random.randint (-5, 5), 'yvelo' : random.randint (-5, 5), 'mass' : 5, 'xpos' : xpos,
                          'ypos' : ypos }
                enemylist.append (enemy)
                RGC.set_alpha (60)
                RGCrect.center = (enemy [ 'xpos' ], enemy [ 'ypos' ])
                mainscr.blit (RGC, RGCrect)

        def spawnasteroid ( xpos, ypos ) :
                asteroid = { 'xvelo' : random.randint (-3, 3), 'yvelo' : random.randint (-3, 3), 'mass' : 5,
                             'xpos' : xpos, 'ypos' : ypos }
                asteroidlist.append (asteroid)
                BGC.set_alpha (60)
                BGCrect.center = (asteroid [ 'xpos' ], asteroid [ 'ypos' ])
                mainscr.blit (BGC, BGCrect)


        score = 0

        graph = pygame.image.load ('black raw graph.png')
        graph = pygame.transform.smoothscale (graph, (1700, 1700))
        graph.set_alpha (100)
        graphrect = graph.get_rect ()

        WGC = pygame.image.load ('WhiteGlow.png')
        WGC = pygame.transform.smoothscale (WGC, (100, 100))
        WGC.set_alpha (100)
        WGCrect = WGC.get_rect ()

        Alive = True
        health = 10
        player = { 'image' : WGC, 'Gxpos' : 350, 'Gypos' : 250, 'xvelo' : 0, 'yvelo' : 0, 'mass' : 2, 'xblit' : 350,
                   'yblit' : 250, 'xpos' : 350, 'ypos' : 250, 'bypos' : 250, 'bxpos' : 350 }
        WGCrect.center = (player [ 'xblit' ], player [ 'yblit' ])

        cursor = pygame.image.load ('TarC.png')
        cursor = pygame.transform.smoothscale (cursor, (30, 30))
        cursorrect = cursor.get_rect ()

        WFS = pygame.Surface ((1000, 1000))
        WFS.set_alpha (40)
        WFS.fill ((255, 255, 255))

        bulletlist, enemybulletlist = [ ], [ ]

        scorebg = pygame.Surface ((700, 500))
        scorebg.set_alpha (40)

        prevPxpos, prevPypos = 350, 250

        def newgraphpos () :
                if 500 > player [ 'Gypos' ] > 0 and 700 > player [ 'Gxpos' ] > 0 :
                        graphrect.center = (player [ 'Gxpos' ], player [ 'Gypos' ])
                elif (500 > player [ 'Gypos' ] > 0) == False :
                        player [ 'Gypos' ] = 347
                        graphrect.center = (player [ 'Gxpos' ], player [ 'Gypos' ])
                elif (700 > player [ 'Gxpos' ] > 0) == False :
                        player [ 'Gxpos' ] = 412
                        graphrect.center = (player [ 'Gxpos' ], player [ 'Gypos' ])

        def shootenemybullet ( x1, y1, x2, y2 ) :
                enemybullet = { 'x2' : x2, 'y2' : y2, 'x1' : x1, 'y1' : y1, 'xpos' : myenemy [ 'xpos' ],
                                'ypos' : myenemy [ 'ypos' ], 'bxpos' : player['xblit'], 'bypos' : player['yblit'] }
                enemybulletlist.append (enemybullet)

        def shootbullet ( x1, y1, x2, y2 ) :
                bullet = { 'x2' : x2, 'y2' : y2, 'x1' : x1, 'y1' : y1, 'xpos' : player [ 'xblit' ],
                           'ypos' : player [ 'yblit' ] }
                bulletlist.append (bullet)

        pausebg = pygame.Surface((700,500))
        pausebg.set_alpha(60)

        def pause () :
                Pause = True
                while Pause :
                        pygame.draw.rect (pausebg, '#000000', (0,0,700,500), width = 0, border_radius = 5)
                        mainscr.blit (pausebg)
                        for actions in pygame.event.get ():
                                if actions.type in [ pygame.KEYDOWN ] :
                                        Pause = False
                                else :
                                        time.sleep (0.1)

        while Alive :
                try :
                        mainscr.fill ((0, 0, 0))

                        newgraphpos ()

                        player [ 'Gxpos' ] += player [ 'xvelo' ] ;
                        player [ 'Gypos' ] += player [ 'yvelo' ]
                        player [ 'xpos' ] += player [ 'xvelo' ] ;
                        player [ 'ypos' ] += player [ 'yvelo' ]

                        mousecor = pygame.mouse.get_pos ()

                        if mousecor [ 0 ] > 400 :
                                if player [ 'xblit' ] > 275 :
                                        player [ 'xblit' ] -= 2
                                        player [ 'Gxpos' ] -= 2
                                        player [ 'xpos' ] -= 2
                        if mousecor [ 0 ] < 300 :
                                if player [ 'xblit' ] < 425 :
                                        player [ 'xblit' ] += 2
                                        player [ 'Gxpos' ] += 2
                                        player [ 'xpos' ] += 2
                        if mousecor [ 1 ] < 200 :
                                if player [ 'yblit' ] < 325 :
                                        player [ 'yblit' ] += 2
                                        player [ 'Gypos' ] += 2
                                        player [ 'ypos' ] += 2
                        if mousecor [ 1 ] > 300 :
                                if player [ 'yblit' ] > 175 :
                                        player [ 'yblit' ] -= 2
                                        player [ 'Gypos' ] -= 2
                                        player [ 'ypos' ] -= 2

                        mainscr.blit (graph, graphrect)

                        mainscr.blit (WGC, WGCrect)

                        for myast in asteroidlist :
                                mainscr.blit (BGC, (myast [ 'xpos' ], myast [ 'ypos' ]))
                                for cbullet in bulletlist :
                                        if (math.fabs (cbullet [ 'xpos' ] - myast [ 'xpos' ] - 28) < 20) and (
                                                            math.fabs (cbullet [ 'ypos' ] - myast [ 'ypos' ] - 30) < 20) :
                                                mainscr.blit (WFS, (0, 0))
                                                pygame.display.flip ()
                                                time.sleep (0.4)
                                                asteroidlist.remove (myast)
                                                bulletlist.remove (cbullet)
                                                score += 1
                                                if score > highscore :
                                                        databalancer.score = score
                                                        highscore = score
                                myast [ 'xpos' ] = myast [ 'xpos' ] + player [ 'xpos' ] - prevPxpos + myast [ 'xvelo' ]
                                myast [ 'ypos' ] = myast [ 'ypos' ] + player [ 'ypos' ] - prevPypos + myast [ 'yvelo' ]

                        for myenemy in enemylist :
                                mainscr.blit (RGC, (myenemy [ 'xpos' ], myenemy [ 'ypos' ]))
                                for cbullet in bulletlist :
                                        if (math.fabs (cbullet [ 'xpos' ] - myenemy [ 'xpos' ] - 28) < 20) and (
                                                            math.fabs (cbullet [ 'ypos' ] - myenemy [ 'ypos' ] - 30) < 20) :
                                                mainscr.blit (WFS, (0, 0))
                                                pygame.display.flip ()
                                                time.sleep (0.4)
                                                enemylist.remove (myenemy)
                                                bulletlist.remove (cbullet)
                                                score += 3
                                                if score > highscore :
                                                        databalancer.score = score
                                                        highscore = score
                                myenemy [ 'xpos' ] = myenemy [ 'xpos' ] + player [ 'xpos' ] - prevPxpos + myenemy [ 'xvelo' ]
                                myenemy [ 'ypos' ] = myenemy [ 'ypos' ] + player [ 'ypos' ] - prevPypos + myenemy [ 'yvelo' ]
                                if (math.fabs (myenemy [ 'xpos' ] - player [ 'xblit' ]) < 650) and (
                                                    math.fabs (myenemy [ 'ypos' ] - player [ 'yblit' ]) < 450) :
                                        shoot_decision = random.randint (0, 100)
                                        if shoot_decision == 10 :
                                                shootenemybullet (player [ 'bxpos' ], player [ 'bypos' ], myenemy [ 'xpos' ],
                                                                  myenemy [ 'ypos' ])

                        if len (bulletlist) > 0 :
                                for cbullet in bulletlist :
                                        cbullet [ 'xpos' ] += (cbullet [ 'x2' ] - cbullet [ 'x1' ]) / 20
                                        cbullet [ 'ypos' ] += (cbullet [ 'y2' ] - cbullet [ 'y1' ]) / 20
                                        RBCrect.center = (cbullet [ 'xpos' ], cbullet [ 'ypos' ])
                                        mainscr.blit (RBC, RBCrect)
                                        for abullet in enemybulletlist :
                                                if math.fabs (( cbullet['xpos'] - abullet['xpos']) + (cbullet['ypos'] - abullet['ypos'])) < 2 :
                                                        bulletlist.remove(cbullet)
                                                        enemybulletlist.remove(abullet)

                        if len (enemybulletlist) > 0 :
                                for cenemybullet in enemybulletlist :
                                        cenemybullet [ 'bxpos' ] += (player['xpos'] - prevPxpos) + player['xvelo']
                                        cenemybullet [ 'bypos' ] += (player['ypos'] - prevPypos) + player ['yvelo']

                                        cenemybullet [ 'xpos' ] -= ((cenemybullet ['x2'] - cenemybullet [ 'bxpos' ])) / 100
                                        cenemybullet [ 'ypos' ] -= ((cenemybullet [ 'y2' ] - cenemybullet [ 'bypos' ])) / 100
                                        if mousecor [ 1 ] > 300 :
                                                if player [ 'yblit' ] > 175 :
                                                        cenemybullet [ 'ypos' ] -= 2
                                        if mousecor [ 1 ] < 200 :
                                                if player [ 'yblit' ] < 325 :
                                                        cenemybullet [ 'ypos' ] += 2
                                        if mousecor [ 0 ] < 300 :
                                                if player [ 'xblit' ] < 425 :
                                                        cenemybullet [ 'xpos' ] += 2
                                        if mousecor [ 0 ] > 400 :
                                                if player [ 'xblit' ] > 275 :
                                                        cenemybullet [ 'xpos' ] -= 2

                                        RBCrect.center = (cenemybullet [ 'xpos' ], cenemybullet [ 'ypos' ])
                                        mainscr.blit (RBC, RBCrect)
                                        if (math.fabs (cenemybullet [ 'xpos' ] - player [ 'xblit' ]) < 50) and (
                                                            math.fabs (cenemybullet [ 'ypos' ] - player [ 'yblit' ]) < 50) :
                                                enemybulletlist.remove (cenemybullet)
                                                health -= 1

                        if math.fabs (player [ 'xvelo' ] + player [ 'yvelo' ]) < 0.9 :
                                backG = pygame.Surface ((125, 30))
                                backG.set_alpha (60)
                                backG.fill ((255, 0, 0))
                                mainscr.blit (backG, (player [ 'xblit' ] + 25, player [ 'yblit' ] - 5))
                                mainscr.blit (tinyfont.render ('I don\'t sense it safe', True, '#FFFFFF'),
                                              (player [ 'xblit' ] + 30, player [ 'yblit' ]))
                                mainscr.blit (tinyfont.render ('to be stationary !', True, '#FFFFFF'),
                                              (player [ 'xblit' ] + 30, player [ 'yblit' ] + 10))

                        WGCrect.center = (player [ 'xblit' ], player [ 'yblit' ])
                        cursorrect.center = mousecor
                        mainscr.blit (cursor, cursorrect)

                        for action in pygame.event.get () :
                                if action.type == pygame.QUIT :
                                        Alive = False
                                        homescreen ()
                                if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :
                                        key = pygame.key.get_pressed ()
                                        if key [pygame.K_p] :
                                                pause()
                                        if key [ pygame.K_x ] :
                                                shootbullet (player [ 'xblit' ], player [ 'yblit' ], mousecor [ 0 ],
                                                             mousecor [ 1 ])
                                        if key [ pygame.K_q ] :
                                                Alive = False
                                                homescreen ()
                                        if key [ pygame.K_w ] or key [ pygame.K_UP ] :
                                                if player [ 'yvelo' ] < 10 :
                                                        player [ 'yvelo' ] += 2

                                        if key [ pygame.K_s ] or key [ pygame.K_DOWN ] :
                                                if player [ 'yvelo' ] > -10 :
                                                        player [ 'yvelo' ] -= 2

                                        if key [ pygame.K_d ] or key [ pygame.K_RIGHT ] :
                                                if player [ 'xvelo' ] > -10 :
                                                        player [ 'xvelo' ] -= 2

                                        if key [ pygame.K_a ] or key [ pygame.K_LEFT ] :
                                                if player [ 'xvelo' ] < 10 :
                                                        player [ 'xvelo' ] += 2
                                if action.type == pygame.MOUSEBUTTONDOWN :
                                        shootbullet (player [ 'xblit' ], player [ 'yblit' ], mousecor [ 0 ], mousecor [ 1 ])



                        prevPxpos = player [ 'xpos' ]
                        prevPypos = player [ 'ypos' ]

                        if player [ 'xvelo' ] > 0 :
                                player [ 'xvelo' ] -= 0.02
                        if player [ 'xvelo' ] < 0 :
                                player [ 'xvelo' ] += 0.02

                        if player [ 'yvelo' ] > 0 :
                                player [ 'yvelo' ] -= 0.02
                        if player [ 'yvelo' ] < 0 :
                                player [ 'yvelo' ] += 0.02

                        if math.fabs (player [ 'xvelo' ] + player [ 'yvelo' ]) > 0.9 :
                                if player [ 'xvelo' ] > 0.4 :
                                        choice = random.randint (0, 100)
                                        if choice == 25 :
                                                spawnasteroid (0, random.randint (10, 691))
                                        if choice == 75 :
                                                spawnenemy (0, random.randint (10, 691))
                                if player [ 'xvelo' ] < -0.4 :
                                        choice = random.randint (0, 100)
                                        if choice == 25 :
                                                spawnasteroid (700, random.randint (10, 590))
                                        if choice == 75 :
                                                spawnenemy (700, random.randint (10, 590))
                                if player [ 'yvelo' ] > 0.4 :
                                        choice = random.randint (0, 100)
                                        if choice == 25 :
                                                spawnasteroid (random.randint (10, 690), 0)
                                        if choice == 75 :
                                                spawnenemy (random.randint (10, 690), 0)
                                if player [ 'yvelo' ] < -0.4 :
                                        choice = random.randint (0, 100)
                                        if choice == 25 :
                                                spawnasteroid (random.randint (10, 690), 700)
                                        if choice == 75 :
                                                spawnenemy (random.randint (10, 690), 700)

                        pygame.draw.polygon (scorebg, '#FF0000', ((20, 0), (20, 20), (230, 20), (250, 0)))
                        pygame.draw.polygon (scorebg, '#FFFFFF', ((0, 0), (0, 20), (20, 20), (20, 0)))
                        pygame.draw.polygon(scorebg, '#AAFF00', ((600, 480), (580, 500), (700, 500), (700, 480)))
                        scoretext = tinyfont.render (f'score : {score}   |   highscore = {highscore}', True, (255, 255, 255))
                        healthtext = tinyfont.render (f'Health : {health}', True, (255,255,255))
                        mainscr.blit (scorebg, (0, 0))
                        mainscr.blit (scoretext, (30, 5))
                        mainscr.blit (healthtext, (640, 483))

                        pygame.draw.rect(mainscr, '#FFFFFF', (0,0,700,500),width = 2, border_radius = 5 )

                        if health == 0 :
                                Alive = False

                        pygame.display.update ()
                        gameclock.tick (120)


                except :
                        continue


# game_homescreen
def homescreen () :
        Home = True
        print ('user entered game home')

        pointer = { 'xcor' : 300, 'ycor' : 60 }

        def back_polygon ( x_loc ) :
                pygame.draw.polygon (mainscr, (30, 30, 30),
                                     [ (-20, 5), (-20, 495), (x_loc, 495), (x_loc - 50, 5) ], width = 0)
                # pygame.draw.polygon (mainscr, (250, 250, 250),
                #                      [ (x_loc - 55, 5), (x_loc - 5, 495), (x_loc, 495), (x_loc - 50, 5) ], width = 0)
                #
                pygame.draw.polygon (mainscr, (50, 50, 50),
                                     [ (x_loc - 45, 5), (x_loc + 5, 495), (x_loc + 10, 495), (x_loc - 40, 5) ],
                                     width = 0)

                pygame.draw.rect (mainscr, (250, 250, 250), [ x_loc - 380, 40, 150, 50 ], width = 2, border_radius = 15)
                pygame.draw.rect (mainscr, (250, 250, 250), [ x_loc - 380, 120, 150, 50 ], width = 2,
                                  border_radius = 15)
                pygame.draw.rect (mainscr, (250, 250, 250), [ x_loc - 380, 190, 150, 50 ], width = 2,
                                  border_radius = 15)
                pygame.draw.line (mainscr, '#FF0000', (x_loc - 400, 320), (x_loc - 100, 320), width = 3)

        for x_loc in range (0, 400, 2) :
                mainscr.fill ((0, 0, 0))
                back_polygon (x_loc)
                mainscr.blit (normalfont.render ('Start', False, (255, 255, 255)), (x_loc - 360, 55))
                mainscr.blit (normalfont.render ('Settings', False, (255, 255, 255)), (x_loc - 370, 135))
                mainscr.blit (normalfont.render ('Quit - Q', False, (255, 255, 255)), (x_loc - 370, 205))
                mainscr.blit (largefont.render ('Energy fights', False, '#FFFFFF'), (x_loc - 370, 300))
                RTCrect.center = (x_loc - 101, 320)
                mainscr.blit (RTC, RTCrect)

                pygame.display.flip ()

        def slide_left () :
                for x_loc in range (400, 0, -2) :
                        mainscr.fill ((0, 0, 0))
                        back_polygon (x_loc)
                        mainscr.blit (normalfont.render ('Start', False, (255, 255, 255)), (x_loc - 360, 55))
                        mainscr.blit (normalfont.render ('Settings', False, (255, 255, 255)), (x_loc - 370, 135))
                        mainscr.blit (normalfont.render ('Quit - Q', False, (255, 255, 255)), (x_loc - 370, 205))
                        mainscr.blit (largefont.render ('Energy fights', False, '#FFFFFF'), (x_loc - 370, 300))
                        RTCrect.center = (x_loc - 101, 320)
                        mainscr.blit (RTC, RTCrect)

                        pygame.display.flip ()

        WGCrect.center = (250, 60)

        WGCrectcenters = [ (180, 50), (180, 130), (180, 200) ]
        WGCCindex = 0

        while Home :
                mainscr.blit (WGC, WGCrectcenters [ WGCCindex ])
                for action in pygame.event.get () :
                        if action.type == pygame.QUIT :
                                print ('user exitted home')
                                slide_left ()
                                mainscr.fill ((0, 0, 0))
                                mainscr.blit (normalfont.render ('exiting home...', False, (255, 255, 255)), (250, 300))
                                pygame.display.flip ()
                                time.sleep (2)
                                Home = False
                        if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :
                                key = pygame.key.get_pressed ()
                                if key [ pygame.K_q ] :
                                        print ('user exitted home')
                                        slide_left ()
                                        mainscr.fill ((0, 0, 0))
                                        mainscr.blit (largefont.render ('exiting home...', False, (255, 255, 255)),
                                                      (250, 200))
                                        pygame.display.flip ()
                                        time.sleep (2)
                                        Home = False
                                if key [ pygame.K_DOWN ] :
                                        if WGCCindex == 2 :
                                                WGCindex = 0
                                        if WGCCindex < 2 :
                                                WGCCindex += 1

                                        x_loc = 398
                                        mainscr.fill ((0, 0, 0))
                                        back_polygon (x_loc)
                                        mainscr.blit (normalfont.render ('Start', False, (255, 255, 255)),
                                                      (x_loc - 360, 55))
                                        mainscr.blit (normalfont.render ('Settings', False, (255, 255, 255)),
                                                      (x_loc - 370, 135))
                                        mainscr.blit (normalfont.render ('Quit - Q', False, (255, 255, 255)),
                                                      (x_loc - 370, 205))
                                        mainscr.blit (largefont.render ('Energy fights', False, '#FFFFFF'),
                                                      (x_loc - 370, 300))
                                        RTCrect.center = (x_loc - 101, 320)
                                        mainscr.blit (RTC, RTCrect)

                                        pygame.display.flip ()
                                if key [ pygame.K_UP ] :
                                        if WGCCindex == 0 :
                                                WGCCindex = 2
                                        if WGCCindex > 0 :
                                                WGCCindex -= 1

                                        x_loc = 399
                                        mainscr.fill ((0, 0, 0))
                                        back_polygon (x_loc)
                                        mainscr.blit (normalfont.render ('Start', False, (255, 255, 255)),
                                                      (x_loc - 360, 55))
                                        mainscr.blit (normalfont.render ('Settings', False, (255, 255, 255)),
                                                      (x_loc - 370, 135))
                                        mainscr.blit (normalfont.render ('Quit - Q', False, (255, 255, 255)),
                                                      (x_loc - 370, 205))
                                        mainscr.blit (largefont.render ('Energy fights', False, '#FFFFFF'),
                                                      (x_loc - 370, 300))
                                        RTCrect.center = (x_loc - 101, 320)
                                        mainscr.blit (RTC, RTCrect)

                                        pygame.display.flip ()
                                if key [ pygame.K_RETURN ] :
                                        if WGCCindex == 2 :
                                                print ('user exitted home')
                                                slide_left ()
                                                mainscr.fill ((0, 0, 0))
                                                mainscr.blit (
                                                                    normalfont.render ('exiting home...', False,
                                                                                       (255, 255, 255)),
                                                                    (250, 300))
                                                pygame.display.flip ()
                                                time.sleep (2)
                                                Home = False
                                        if WGCCindex == 0 :
                                                Home = False
                                                slide_left ()
                                                startgame ()
                pygame.display.update ()
homescreen ()


# game_backend mainloop
while Main :
        pygame.mouse.set_visible (True)
        for action in pygame.event.get () :
                if action.type == pygame.QUIT :
                        Main = False
                if action.type in [ pygame.KEYUP, pygame.KEYDOWN ] :
                        key = pygame.key.get_pressed ()
                        if key [ pygame.K_q ] :
                                mainscr.fill ((0, 0, 0))
                                mainscr.blit (largefont.render ('Quitting...', False, '#FFFFFF'), (300, 200))
                                pygame.display.flip ()
                                time.sleep (2)
                                Main = False
                                quit ()

        mainscr.fill ('#000001')
        mainscr.blit (logoimg, logoimgrect)

        pygame.draw.polygon (mainscr, '#FFFFFF', [ (30, 20), (20, 50), (160, 50), (180, 20) ], width = 0)
        mainscr.blit (normalfont.render ('Quit - Q', False, (0, 0, 0)), (40, 25))

        mainscr.blit (normalfont.render ('The game has been created by the author alone.', False, '#5555FF'), (25, 70))
        mainscr.blit (normalfont.render ('Keep supporting me !', True, '#5555FF'), (25, 95))
        mainscr.blit (normalfont.render ('Thanking you for giving the game a chance', False, '#5555FF'), (25, 120))

        pygame.display.update ()