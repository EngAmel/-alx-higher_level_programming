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

    def display(self):
        '''desplay traingle'''

        for z in range(self.y):
            print("")

        for w in range(self.height):
            for n in range(self.x):
                print(" ", end="")
            for h in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        '''__str__'''

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x,
                   self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''update args'''

        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        '''update kwargs.'''

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
