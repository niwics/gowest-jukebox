# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Scanner for importing the ID3 tags from audio files
# @author: www.niwi.cz

import os
import sqlite3

from hsaudiotag import auto
from app import App, SQLITE_DB_FILE

class CollectionScannerError(Exception):
    pass

class CollectionScanner(object):

    DB_COL_NAMES = ['filename', 'artist', 'title', 'album', 'duration', 'year']

    def __init__(self, directory):
        """
        Inits the dialog.
        :param directory:
        :return:
        """
        self.directory = directory
        self.songs = []

    def scan(self):
        self.songs = []
        self._scan_dir(self.directory)
        self._insert_data()

    def _scan_dir(self, directory):
        if App.is_debug(): print "Scanning directory %s..." % directory

        if not os.path.isdir(directory):
            raise CollectionScannerError("Error while scanning: '%s' is not a directory!" % directory)

        for root, subdirs, files in os.walk(directory):
            for file in files:
                if not file.startswith("."):
                    song_metadata = self._decode_id3_tag(os.path.join(root, file))
                    if song_metadata:
                        self.songs.append(song_metadata)
            for subdir in subdirs:
                if subdir.startswith("."):
                    subdirs.remove(subdir)

    def _decode_id3_tag(self, filename):
        file_tags = auto.File(filename)
        if not file_tags.artist or not file_tags.title:
            if App.is_debug(): print "No metadata detected in the file %s..." % filename
            return
        elif App.is_debug():
            print "File %s: artist: %s, title: %s" % (filename, file_tags.artist, file_tags.title)
        return filename, file_tags.artist, file_tags.title, file_tags.album, file_tags.duration, file_tags.year

    def _insert_data(self):

        col_names = ",".join(CollectionScanner.DB_COL_NAMES)
        question_marks = ",".join(["?"] * len(CollectionScanner.DB_COL_NAMES))

        conn = sqlite3.connect(SQLITE_DB_FILE)

        # drop the old table
        conn.execute("DROP TABLE IF EXISTS song")
        # create the new table
        conn.execute("CREATE TABLE song(%s)" % col_names)

        # fill the table with data
        conn.executemany("INSERT INTO song(%s) values (%s)" % (col_names, question_marks), self.songs)

        # Print the table contents
        for row in conn.execute("select * from song"):
            print row

    def get_songs_count(self):
        return len(self.songs)
