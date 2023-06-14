#!/usr/bin/python3
'''class student'''


class Student:
    '''student'''

    def __init__(self, first_name, last_name, age):
        '''intial new'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''def student rep'''
        return self.__dict__
