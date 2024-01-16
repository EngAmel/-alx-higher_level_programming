#!/usr/bin/python3
'''Square module'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''__str__'''

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter Size'''

        return self.width

    @size.setter
    def size(self, value):
        '''setter'''

        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''update args'''

        if id:
            self.id = id
        if size:
            self.size = size
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
