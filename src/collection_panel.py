# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Sizer containing information about one single song from the collection.
# @author: www.niwi.cz

import wx
from wx.lib.scrolledpanel import ScrolledPanel

from collection_controller import CollectionController
from collection_song_panel import CollectionSongPanel


class CollectionPanel(ScrolledPanel):

    def __init__(self, parent):
        """
        Init GUI
        :param args:
        :param kwargs:
        :return: None
        """
        super(CollectionPanel, self).__init__(parent)

        self._current_active_song_panel = None

        self.SetupScrolling()
        self.SetBackgroundColour('#FAFAFA')

        vbox = wx.BoxSizer(wx.VERTICAL)

        # add all songs ordered by artist-album-song name
        collection_ctr = CollectionController()
        previous_panel = None
        for song in collection_ctr.get_all_songs():
            song_panel = CollectionSongPanel(self, song, previous_panel)
            vbox.Add(song_panel, flag=wx.EXPAND|wx.TOP, border=3)
            if previous_panel:
                previous_panel.next_panel = song_panel;
            else:
                self._current_active_song_panel = song_panel
            previous_panel = song_panel


        # set the first panel as active
        if self._current_active_song_panel:
            self._current_active_song_panel.set_active()

        self.SetSizer(vbox)

    def previous_action(self):
        if self._current_active_song_panel and self._current_active_song_panel._previous_panel:
            self._current_active_song_panel._previous_panel.set_active()
            self._current_active_song_panel.set_not_active()
            self._current_active_song_panel = self._current_active_song_panel._previous_panel

    def next_action(self):
        if self._current_active_song_panel and self._current_active_song_panel._next_panel:
            self._current_active_song_panel._next_panel.set_active()
            self._current_active_song_panel.set_not_active()
            self._current_active_song_panel = self._current_active_song_panel._next_panel

    def add_action(self):
        if self._current_active_song_panel:
            pass