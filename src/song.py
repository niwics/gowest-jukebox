#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author: www.niwi.cz


class Song():
    """
    Class for storing one single song attributes.
    """

    def __init__(self, filename, title, artist, album, duration, year):
        self.filename = filename
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.year = year

    def attrs_to_sql(self):
        return (self.filename, self.title, self.artist, self.album, self.duration, self.year)