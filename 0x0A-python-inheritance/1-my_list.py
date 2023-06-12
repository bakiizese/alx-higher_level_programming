#!/usr/bin/python3
'''inheritance from list'''


class MyList(list):
    '''my class'''

    def print_sorted(self):
        '''print sorted list'''
        print(sorted(self))
