# RACE CAR

import pygame
import time
import random
pygame.init()
#Convert mp3 to .wav and enjoy songs yay!! :D

pygame.mixer.music.load('Race_Car.wav')
pygame.mixer.music.play(-1)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
carImg = pygame.image.load('car1.png')

black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)

clock = pygame.time.Clock()

racecar_width=72

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def crash():
    message_display('You Crashed')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.75)
    x_change = 0
    y_change = 0
    gameExit = False
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width =70
    thing_height =70
    dodged=0
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # gameExit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

            print(event)
        x += x_change
        y += y_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        things_dodged(dodged)
        car(x, y)

        if((x < 0) or (x > display_width - racecar_width)):
            # gameExit = True
             crash()
        if(thing_starty > display_height):
            thing_starty = -600
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            print(dodged)

        if(y < thing_starty+thing_height):
            # print("Crossed vertically")
            if(x > thing_startx and x < thing_startx+thing_width or x+racecar_width >thing_startx and x+racecar_width < thing_startx+thing_width ):
                # print("Crossed horizontally")
                crash()

        pygame.display.update()

        clock.tick(60)

game_loop()
pygame.quit()
quit()

