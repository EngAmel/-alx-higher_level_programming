#!/usr/bin/python3
'''square module'''


from models.rectangle import Rectangle


class Square (Rectangle):
    '''square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''__str__'''

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)