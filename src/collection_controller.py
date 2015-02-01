# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Scanner for importing the ID3 tags from audio files
# @author: www.niwi.cz

import os
import sqlite3

from hsaudiotag import auto
from app import App, SQLITE_DB_FILE
from song import Song

class CollectionError(Exception):
    pass

class CollectionController():

    DB_COL_NAMES = ['filename', 'title', 'artist', 'album', 'duration', 'year']

    def __init__(self):
        """
        Inits the dialog.
        :return:
        """
        self.songs = None

    def scan(self):
        self.songs = []
        self._scan_dir(App.get_songs_dir())
        self._insert_data()

    def _scan_dir(self, directory):
        if App.is_debug(): print "Scanning directory %s..." % directory

        if not os.path.isdir(directory):
            raise CollectionError("Error while scanning: '%s' is not a directory!" % directory)

        for root, subdirs, files in os.walk(directory):
            for file in files:
                if not file.startswith("."):
                    song = self._decode_id3_tag(os.path.join(root, file))
                    if song:
                        self.songs.append(song)
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
        return Song(filename, file_tags.title, file_tags.artist, file_tags.album, file_tags.duration, file_tags.year)

    def _insert_data(self):

        col_names = ",".join(CollectionController.DB_COL_NAMES)
        question_marks = ",".join(["?"] * len(CollectionController.DB_COL_NAMES))

        conn = sqlite3.connect(SQLITE_DB_FILE)

        # drop the old table
        conn.execute("DROP TABLE IF EXISTS song")
        # create the new table
        conn.execute("CREATE TABLE song(%s)" % col_names)

        # fill the table with data
        conn.executemany("INSERT INTO song(%s) values (%s)" % (col_names, question_marks), [song.attrs_to_sql() for song in self.songs])

        # Print the table contents
        if App.is_debug():
            for row in conn.execute("SELECT * FROM song"):
                print row

        conn.commit()
        conn.close()

    def get_songs_count(self):
        return 0 if self.songs is None else len(self.songs)

    def get_all_songs(self):

        if self.songs is None:
            self.songs = []
            conn = sqlite3.connect(SQLITE_DB_FILE)
            conn.row_factory=sqlite3.Row
            for row in conn.execute("SELECT * FROM song ORDER BY artist, year, album, title"):
                self.songs.append(Song(row['filename'], row['title'], row['artist'], row['album'], row['duration'], row['year']))

        return self.songs
