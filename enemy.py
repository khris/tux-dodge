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
import random
import math

class Enemy(character.Character):
  """Enemy Class"""

  def __init__(self, Store):
    character.Character.__init__(self, Store)
    self.Init()

  def Init(self):
    character.Character.Init(self)
    self.rect.center = imagestore.ScreenWidth // 2, imagestore.ScreenHeight // 2
    self.collision_rect.center = self.rect.center

    Angle = math.radians(random.randrange(0, 300))
    Distance = random.randrange(140, 190)
    Speed = random.uniform(0.5, 1.2)
    x = Distance * math.cos(Angle)
    y = Distance * math.sin(Angle)

    self.rect.move_ip(x, y)
    self.__Position = self.rect.center

    self.increase_x = -Speed * math.cos(Angle)
    self.increase_y = -Speed * math.sin(Angle)

  def update(self):
    self.__Position = self.__Position[0] + self.increase_x, self.__Position[1] + self.increase_y
    self.rect.center = self.__Position

    if self.rect.top < -40:
      self.rect.top = -40
      self.increase_y = -self.increase_y
    if self.rect.bottom > imagestore.ScreenHeight + 40:
      self.rect.bottom = imagestore.ScreenHeight + 40
      self.increase_y = -self.increase_y
    if self.rect.left < -40:
      self.rect.left = -40
      self.increase_x = -self.increase_x
    if self.rect.right > imagestore.ScreenWidth + 40:
      self.rect.right = imagestore.ScreenWidth + 40
      self.increase_x = -self.increase_x

    self.collision_rect.center = self.rect.center
