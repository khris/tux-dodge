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
import pygame
import imagestore
import character
import copy

class Hero(character.Character):
  """Hero Class"""

  def __init__(self, Store):
    character.Character.__init__(self, Store)
    self.Init()

  def Init(self):
    character.Character.Init(self)
    self.rect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2
    self.collision_rect.width -= 6
    self.collision_rect.height -= 6
    self.collision_rect.center = self.rect.center

  def update(self):
    if self.Mode != u'normal':
      character.Character.update(self)

    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > imagestore.ScreenHeight:
      self.rect.bottom = imagestore.ScreenHeight
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > imagestore.ScreenWidth:
      self.rect.right = imagestore.ScreenWidth
    
    self.collision_rect.center = self.rect.center
