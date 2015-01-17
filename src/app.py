#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author: www.niwi.cz

SQLITE_DB_FILE = "songs_db.db"

class App():
    """
    Class for storing settings shared across application components.
    """

    _debug = True
    _songs_dir = ""

    @classmethod
    def is_debug(cls):
        """
        :return: Debug flag
        """
        return cls._debug

    @classmethod
    def get_songs_dir(cls):
        """
        :return: Songs collection root directory.
        """
        return cls._songs_dir

    @classmethod
    def set_songs_dir(cls, songs_dir):
        """
        :param songs_dir: New songs collection root directory.
        :return:
        """
        cls._songs_dir = songs_dir