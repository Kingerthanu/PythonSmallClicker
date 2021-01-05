import pygame
import sys
import random
import os

screen = pygame.display.set_mode((900, 680))  # Setting Screen Res
pygame.init()  # Starting 'Pygame'
x = 0  # Simple locational variables of square
y = 0
clickAbl = pygame.draw.rect(
    screen, pygame.Color("Blue"), (random.randint(1, 900-30), random.randint(1, 680-30), 25, 25))  # Creating single Clicking Object
arrOfEntities = []
arrOfEntities.append(clickAbl)  # Keep Track of Active Entities
countr = 0  # The Counting of Successive Clicks
pyIco = pygame.display.set_icon(pygame.image.load(
    'Stock.jpg'))  # Finds 'Stock.jpg' in Relative Path
# Sets font wanted for impeding render
texFnt = pygame.font.SysFont('Calibri', 35)
# Name of our Program in window
pygame.display.set_caption("Simple Clicker Counter")
tex = texFnt.render(str(countr), True, (255, 255, 255)
                    )  # Creates our Text object
# Prints text to screen and saves it in variable texObj
texObj = screen.blit(tex, (20, 20))
pygame.display.update()
while(1):
    for event in pygame.event.get():  # Catches unique behaivior given to pygame screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouspos = pygame.mouse.get_pos()
            if clickAbl.collidepoint(mouspos):
                countr += 1
                screen.fill(pygame.Color("Black"))
                clickAbl = pygame.draw.rect(
                    screen, pygame.Color("Blue"), (random.randint(1, 900-30), random.randint(1, 680-30), 25, 25))
                tex = texFnt.render(str(countr), True, (255, 255, 255))
                screen.blit(tex, (20, 20))
                pygame.display.update()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and countr != 0:
            countr = 0
            tex = texFnt.render(str(countr), True, (255, 255, 255))
            screen.fill(pygame.Color("Black"))
            screen.blit(tex, (20, 20))
            clickAbl = pygame.draw.rect(
                screen, pygame.Color("Blue"), (random.randint(1, 900-30), random.randint(1, 680-30), 25, 25))
            pygame.display.update()
        if event.type == pygame.QUIT:
            print("Done")
            pygame.quit()
