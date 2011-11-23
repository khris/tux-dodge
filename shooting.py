#!/usr/bin/env python

############################################################################
#    Copyright (C) 2006 by khris                                           #
#    khris.mana@gmail.com                                                  #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

from __future__ import division
import os
import pygame
import character
import imagestore
import hero
import enemy
import copy
from pygame.locals import *

def main():
  TitleColor = pygame.color.Color('#000000')
  BackgroundColor = pygame.color.Color('#AAAAFF')
  HalftoneColor = pygame.color.Color('0x000000AA')
  DefaultColorkey = pygame.color.Color('#FF00FF')

  pygame.init()
  Screen = pygame.display.set_mode((imagestore.ScreenWidth, imagestore.ScreenHeight))
  pygame.display.set_caption(u'Tux Dodge!')

  HeroImage_Up = imagestore.ImageStore(u'tux_up.png', Cols = 4, Colorkey = DefaultColorkey)
  HeroImage_Down = imagestore.ImageStore(u'tux_down.png', Cols = 4, Colorkey = DefaultColorkey)
  HeroImage_Left = imagestore.ImageStore(u'tux_left.png', Cols = 4, Colorkey = DefaultColorkey)
  HeroImage_Right = imagestore.ImageStore(u'tux_right.png', Cols = 4, Colorkey = DefaultColorkey)
  Tux = hero.Hero(HeroImage_Down)
  Tux.Store[u'up'] = HeroImage_Up
  Tux.Store[u'down'] = HeroImage_Down
  Tux.Store[u'left'] = HeroImage_Left
  Tux.Store[u'right'] = HeroImage_Right
  HeroGroup = pygame.sprite.RenderPlain(Tux)

  EnemyImage = imagestore.ImageStore(u'enemy.png', Colorkey = DefaultColorkey)
  EnemyGroup = pygame.sprite.RenderPlain()
  for x in range(100):
    EnemyGroup.add(enemy.Enemy(EnemyImage))

  MainClock = pygame.time.Clock()
  MainFont = pygame.font.SysFont(u'sans', 20, bold = True)
  pygame.key.set_repeat(100, 30)
  GameMode = 'Wait'
  Die = False
  StartTime = 0
  EndTime = 0

  while 1:
    MainClock.tick(imagestore.DefaultFPS)

    if GameMode == 'Wait':
      for event in pygame.event.get():
        if event.type == QUIT:
          return
        if event.type == KEYUP and event.key == K_RETURN:
          StartTime = pygame.time.get_ticks()
          GameMode = 'Play'

      Screen.fill(TitleColor)

      TitleText = MainFont.render(u'Tux Dodge! version 0.1', False, pygame.color.Color('#FFFFFF'))
      TitleTextRect = TitleText.get_rect()
      TitleTextRect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2 - MainFont.get_height() // 2
      Screen.blit(TitleText, TitleTextRect)

      TitleText = MainFont.render(u'press enter key', False, pygame.color.Color('#FFFFFF'))
      TitleTextRect = TitleText.get_rect()
      TitleTextRect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2 + MainFont.get_height() // 2
      Screen.blit(TitleText, TitleTextRect)

    if GameMode == 'Play':
      for event in pygame.event.get():
        if event.type == QUIT:
          return
        if event.type == KEYUP:
          if Die == False:
            Tux.Mode = u'normal'
          elif event.key == K_RETURN:
            Tux.Init()
            HeroGroup.add(Tux)
            for bullet in EnemyGroup.sprites():
              bullet.Init()
            Die = False
            GameMode = 'Wait'

      KeySet = pygame.key.get_pressed()
      move_x = 0;
      move_y = 0;

      if KeySet[K_LEFT] == True:
        Tux.Mode = u'left'
        move_x = -1
      if KeySet[K_RIGHT] == True:
        Tux.Mode = u'right'
        move_x = 1
      if KeySet[K_UP] == True:
        Tux.Mode = u'up'
        move_y = -1
      if KeySet[K_DOWN] == True:
        Tux.Mode = u'down'
        move_y = 1

      if Die == False:
        Tux.Move(move_x, move_y)
        HeroGroup.update()
        EnemyGroup.update()

        Crash = character.groupcollide(HeroGroup, EnemyGroup, True, True)

        if len(Crash) > 0:
          Die = True
          EndTime = (pygame.time.get_ticks() - StartTime) / 1000

      Screen.fill(BackgroundColor)
      HeroGroup.draw(Screen)
      EnemyGroup.draw(Screen)

      if Die == True:
        TitleText = MainFont.render(u'game over', False, pygame.color.Color('#FFFFFF'))
        TitleTextRect = TitleText.get_rect()
        TitleTextRect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2 - MainFont.get_height()
        Screen.blit(TitleText, TitleTextRect)

        TitleText = MainFont.render(u'time : ' + unicode(EndTime) + 's', False, pygame.color.Color('#FFFFFF'))
        TitleTextRect = TitleText.get_rect()
        TitleTextRect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2
        Screen.blit(TitleText, TitleTextRect)

        TitleText = MainFont.render(u'press enter key', False, pygame.color.Color('#FFFFFF'))
        TitleTextRect = TitleText.get_rect()
        TitleTextRect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2 + MainFont.get_height()
        Screen.blit(TitleText, TitleTextRect)

    pygame.display.flip()

main()
