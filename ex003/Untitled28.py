#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
from pygame.locals import *
from sys import exit


# In[28]:


pygame.init()

largura = 640
altura = 480
x = largura/2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('IA game')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    if y >= altura:
        y = 0
        
    y = y + 5
        
    pygame.display.update()


# In[ ]:



