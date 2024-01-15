#!usr/bin/python3
'''rectangle module'''


from models.base import Base


class Rectangle(Base):
    '''rectangle class'''


    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''__width -> width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''

        self.__width = value

    @property
    def height(self):
        '''height -> height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''

        self.__height = value

    @property
    def x(self):
        '''__x -> x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''

        self.__x = value

    @property
    def y(self):
        '''y -> y'''

        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''

        self.__y = value
