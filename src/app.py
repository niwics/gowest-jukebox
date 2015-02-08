#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author: www.niwi.cz

import os
import sqlite3


class App():
    """
    Class for storing settings shared across application components.
    """
    _debug = False
    _songs_dir = ""
    _sqlite_db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "songs_db.db")


    @classmethod
    def load_settings_from_db(cls):
        """
        Loads app settings from the SQLite DB
        :return:
        """
        conn = sqlite3.connect(cls._sqlite_db_file)
        conn.row_factory = sqlite3.Row

        # loads the songs_dir; empty if not found
        try:
            for row in conn.execute("SELECT `value` FROM settings WHERE `key` = 'songs_dir' "):
                cls._songs_dir = row["value"]
        except sqlite3.OperationalError, e:
            print "SQLite DB %s: Could not load the key 'songs_dir' from the 'settings' table. Error: %s" % \
                  (cls._sqlite_db_file, e)
        if cls.is_debug(): print "App songs_dir: '%s'" % cls._songs_dir

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
        if cls.is_debug(): print "Setting songs_dir to: '%s'" % songs_dir
        conn = sqlite3.connect(cls._sqlite_db_file)
        # create the new table
        conn.execute("CREATE TABLE IF NOT EXISTS settings(`key` PRIMARY KEY, `value`)")
        # insert the value
        conn.execute("REPLACE INTO settings (`key`, `value`) VALUES ('songs_dir', '%s')" % songs_dir)
        conn.commit()
        conn.close()

        cls._songs_dir = songs_dir