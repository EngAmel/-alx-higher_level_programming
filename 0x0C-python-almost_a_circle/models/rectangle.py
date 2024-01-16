#!/usr/bin/python3
'''rectangle module'''


from models.base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self.valid_int("width", width, False)
        self.__width = width
        self.valid_int("height", height, False)
        self.__height = height
        self.valid_int("x", x)
        self.__x = x
        self.valid_int("y", y)
        self.__y = y

    @property
    def width(self):
        '''__width -> width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''

        self.valid_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height -> height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''

        self.valid_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''__x -> x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''

        self.valid_int("x", value)
        self.__x = value

    @property
    def y(self):
        '''y -> y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''

        self.valid_int("y", value)
        self.__y = value

    def valid_int(self, name, value, eq=True):
        '''valdiation method'''

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        
    def area(self):
        '''traingle area'''

        return self.width * self.height
