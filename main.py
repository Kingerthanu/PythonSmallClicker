import pygame
import sys
import random
import os

screen = pygame.display.set_mode((900, 680))  # Setting Screen Res
pygame.init()  # Starting 'Pygame'
# Direct Path to Backrnd
# Sets background to same res as Screen
x = 0  # Simple locational variables of square
y = 0
clickAbl = pygame.draw.rect(
    screen, pygame.Color("Blue"), (random.randint(1, 900-30), random.randint(1, 680-30), 25, 25))
arrOfEntities = []
arrOfEntities.append(clickAbl)
countr = 0

pyIco = pygame.display.set_icon(pygame.image.load('Stock.jpg'))

texFnt = pygame.font.SysFont('Calibri', 35)
pygame.display.set_caption("Simple Clicker Counter")
tex = texFnt.render(str(countr), True, (255, 255, 255))
texObj = screen.blit(tex, (20, 20))
pygame.display.update()
while(1):
    for event in pygame.event.get():
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
