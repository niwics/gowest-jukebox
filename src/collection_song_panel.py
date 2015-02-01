# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Sizer containing information about one single song from the collection.
# @author: www.niwi.cz

import wx


class CollectionSongPanel(wx.Panel):

    def __init__(self, parent_panel, song, previous_panel):
        """
        Init GUI
        :param args:
        :param kwargs:
        :return: None
        """
        super(CollectionSongPanel, self).__init__(parent_panel)
        self._song = song
        self._previous_panel = previous_panel
        self._next_panel = None

        self.Border

        gs = wx.GridSizer(2, 2, 5, 5)
        gs.AddMany([
            (wx.StaticText(self, label=self._song.title), wx.EXPAND),
            (wx.StaticText(self, label=self._song.album), wx.EXPAND),
            (wx.StaticText(self, label=self._song.artist), wx.EXPAND),
            (wx.StaticText(self, label=self._song.year), wx.EXPAND)
        ])
        self.SetSizer(gs)

    def set_active(self):
        self.SetBackgroundColour('#FFFF8A')

    def set_not_active(self):
        self.SetBackgroundColour(None)

    def set_next_panel(self, next_panel):
        self._next_panel = next_panel