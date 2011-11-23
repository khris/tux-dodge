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
import os, pygame

DefaultFPS = 60
ScreenWidth, ScreenHeight = 320, 240

class ImageStore:
  """Image Store"""

  def __init__(self, FileName, Cols = 1, Rows = 1, Colorkey = None):
    try:
      print u'Loading : ', os.path.join(u'resource', FileName)
      Picture = pygame.image.load(os.path.join(u'resource', FileName))
    except pygame.error, message:
      print 'Can\'t load image file : ', FileName
      raise SystemExit, message

    Picture = Picture.convert()
    ClipWidth = Picture.get_width() // Cols
    ClipHeight = Picture.get_height() // Rows

    if Colorkey is not None:
      Picture.set_colorkey(Colorkey)

    self.__PictureList = []

    for y in range(Rows):
      for x in range(Cols):
        self.__PictureList.append(Picture.subsurface(pygame.Rect(ClipWidth * x, ClipWidth * y, ClipWidth, ClipHeight)))

    self.__LastTime = 0
    self.__Interval = len(self.__PictureList) / DefaultFPS

  def Get(self, Index):
    NowTime = pygame.time.get_ticks()

    if ((NowTime - self.__LastTime) / 1000) >= self.__Interval:
      IncreseValue = 1
      self.__LastTime = NowTime
    else:
      IncreseValue = 0

    if Index > (len(self.__PictureList) - 1) or Index < 0:
      return self.__PictureList[0], IncreseValue
    else:
      return self.__PictureList[Index], Index + IncreseValue
