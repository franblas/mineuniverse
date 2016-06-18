
import random
import numpy as np

from texture import Textures

"""
Basic block generators in order to create a specific biodome or object.
See the _initialize method on the `world.py` file
"""

class Generators(object):

    def __init__(self):
        pass

class BaseWorld(object):

    def __init__(self, n, add_block):
        s = 1  # step size
        y = 0  # initial y height
        for x in xrange(-n, n + 1, s):
            for z in xrange(-n, n + 1, s):
                # create a layer stone an grass everywhere.
                add_block((x, y - 2, z), Textures.GRASS, immediate=False)
                add_block((x, y - 3, z), Textures.STONE, immediate=False)

class Flat(object):

    def __init__(self, add_block, x, z, y):
        print 'Flat'
        a, b, c = x, z, y
        a_sign = np.sign(a)
        b_sign = np.sign(b)
        print a, b
        for x in xrange(a - a_sign * 50, a + a_sign * 50, 1):
            for z in xrange(b - b_sign * 50, b + b_sign * 50, 1):
                # create a layer stone an grass everywhere.
                add_block((x, -2, z), Textures.GRASS, immediate=True)
                add_block((x, -3, z), Textures.STONE, immediate=True)

class Square(object):

    def __init__(self, add_block, x, z, y, h, t):
        a, b, c = x, z, y # x, z, y positions
        s = int(h / 2) # 2 * s is the side length
        for y in xrange(c, c + h):
            for x in xrange(a - s, a + s + 1):
                for z in xrange(b - s, b + s + 1):
                    add_block((x, y, z), t, immediate=False)

class Dome(object):

    def __init__(self, add_block, x, z, y, h, t, reverse=False, no_fill=False, immediate=False):
        a, b, c = x, z, y # x, z, y positions
        s = int(h / 2) # 2 * s is the side length
        y_start, y_stop, i = c, c + h, 1
        if reverse: y_start, y_stop, i = c, c - h, -1
        for y in xrange(y_start,  y_stop, i):
            for x in xrange(a - s, a + s + 1):
                for z in xrange(b - s, b + s + 1):
                    if reverse:
                        if -((x - a) ** 2) - ((z - b) ** 2) < -((s + 1) ** 2):
                            continue
                        if -((x - a) ** 2) -((y - c) ** 2) < -((s + 1) ** 2):
                            continue
                        if -((z - b) ** 2) -((y - c) ** 2) < -((s + 1) ** 2):
                            continue
                        if no_fill:
                            if -((x - a) ** 2) - ((z - b) ** 2) > -((y + s - c) ** 2):
                                continue
                    else:
                        if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
                            continue
                        if (x - a) ** 2 + (y - c) ** 2 > (s + 1) ** 2:
                            continue
                        if (z - b) ** 2 + (y - c) ** 2 > (s + 1) ** 2:
                            continue
                        if no_fill:
                            if (x - a) ** 2 + (z - b) ** 2 < (y - s - c) ** 2:
                                continue
                    add_block((x, y, z), t, immediate=immediate)

class Sphere(object):

    def __init__(self, add_block, x, z, y, h, t, no_fill, immediate):
        Dome(add_block, x, z, y, h, t, no_fill=no_fill, immediate=immediate)
        Dome(add_block, x, z, y, h, t, reverse=True, no_fill=no_fill, immediate=immediate)

class Pyramid(object):

    def __init__(self, add_block, x, z, y, h, t, reverse=False, d=1):
        a, b, c = x, z, y # x, z, y positions
        s = int(h / 2)  # 2 * s is the side length of the hill
        y_start, y_stop, i = c, c + h, 1
        if reverse: y_start, y_stop, i = c, c - h, -1
        for y in xrange(y_start, y_stop, i):
            for x in xrange(a - s, a + s + 1):
                for z in xrange(b - s, b + s + 1):
                    add_block((x, y, z), t, immediate=False)
            s -= d

class Hill(object):

    def __init__(self, add_block, x, z, y, h, t, reverse=False, d=1):
        """
            d: how quickly to taper off the hills
        """
        a, b, c = x, z, y # x, z, y positions
        s = int(h / 2)  # 2 * s is the side length of the hill
        y_start, y_stop, i = c, c + h, 1
        if reverse: y_start, y_stop, i = c, c - h, -1
        for y in xrange(y_start, y_stop, i):
            for x in xrange(a - s, a + s + 1):
                for z in xrange(b - s, b + s + 1):
                    if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
                        continue
                    if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
                        continue
                    add_block((x, y, z), t, immediate=False)
            s -= d

class DoubleHill(object):

    def __init__(self, add_block, x, z, y, h, t, d=1):
        Hill(add_block=add_block, x=x, z=z, y=y, h=h, t=t, d=d)
        Hill(add_block=add_block, x=x, z=z, y=y, h=h, t=t, d=d, reverse=True)

class Planet(object):

    def __init__(self, add_block):
        pass

class BioDome(object):

    # Jungle, sea, forest, mountain, beach, rock

    def __init__(self):
        pass
