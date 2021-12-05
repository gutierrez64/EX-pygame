#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pygame
from pygame.locals import *
from sys import exit


# In[10]:


pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('IA game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


# In[ ]:




