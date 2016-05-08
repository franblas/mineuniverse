from pyglet import image
from pyglet.graphics import TextureGroup

class Texture(object):

    texture_path = 'lib/ressources/texture.png'
    # Texture = top, bottom, sides
    textures = {
        'grass': ((1, 0), (0, 1), (0, 0)),
        'sand': ((1, 1), (1, 1), (1, 1)),
        'brick': ((2, 0), (2, 0), (2, 0)),
        'stone': ((2, 1), (2, 1), (2, 1))
    }
    texture_group = TextureGroup(image.load(texture_path).get_texture())

    def __init__(self):
        pass

    def texture_coordinate(self, x, y, n=4):
        """ Return the bounding vertices of the texture square.
        """
        m = 1.0 / n
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

    def texture_coordinates(self, top, bottom, side):
        """ Return a list of the texture squares for the top, bottom and side.
        """
        top = self.texture_coordinate(*top)
        bottom = self.texture_coordinate(*bottom)
        side = self.texture_coordinate(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result

    def texture_from_name(self, name):
        """ Get texture mapping from the list
        """
        if name not in self.textures:
            print 'Error: texture does not exist'
            return None
        top, bottom, side = self.textures.get(name, 'grass')
        return self.texture_coordinates(top, bottom, side)

class Textures(object):
    t = Texture()
    _texture_group = t.texture_group
    GRASS = t.texture_from_name('grass')
    SAND = t.texture_from_name('sand')
    STONE = t.texture_from_name('stone')
    BRICK = t.texture_from_name('brick')
