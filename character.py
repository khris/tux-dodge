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

import pygame
import imagestore
import copy

def spritecollide(sprite, group, dokill):
    crashed = []
    spritecollide = sprite.collision_rect.colliderect
    if dokill:
        for s in group.sprites():
            if spritecollide(s.collision_rect):
                s.kill()
                crashed.append(s)
    else:
        for s in group:
            if spritecollide(s.collision_rect):
                crashed.append(s)
    return crashed

def groupcollide(groupa, groupb, dokilla, dokillb):
    crashed = {}
    SC = spritecollide
    if dokilla:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa:
            c = SC(s, groupb, dokillb)
            if c:
                crashed[s] = c
    return crashed

class Character(pygame.sprite.Sprite):
  """Character Class"""

  def __init__(self, Store):
    pygame.sprite.Sprite.__init__(self)

    self.Store = {u'normal' : Store}
    self.Init()

  def Init(self):
    self.Mode = u'normal'
    self.__NextImageIndex = 0
    self.image, self.__NextImageIndex = self.Store[self.Mode].Get(self.__NextImageIndex)
    self.rect = self.image.get_rect()
    self.collision_rect = copy.deepcopy(self.rect)

  def update(self):
    self.image, self.__NextImageIndex = self.Store[self.Mode].Get(self.__NextImageIndex)

  def Move(self, x, y):
    self.rect.move_ip(x, y)
    self.collision_rect.move_ip(x, y)
