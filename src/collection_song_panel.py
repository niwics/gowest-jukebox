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

        # fonts for labels
        title_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        title_font.SetWeight(wx.BOLD)
        title_font.SetPointSize(title_font.GetPointSize()+2)

        title_label = wx.StaticText(self, label=self._song.title)
        title_label.SetFont(title_font)
        album_label = wx.StaticText(self, label=self._song.album)
        artist_label = wx.StaticText(self, label=self._song.artist)
        year_label = wx.StaticText(self, label=self._song.year)
        for label in (album_label, artist_label, year_label):
            label.SetForegroundColour('#888888')

        gs.AddMany([
            (title_label, wx.EXPAND),
            (album_label, wx.EXPAND),
            (artist_label, wx.EXPAND),
            (year_label, wx.EXPAND)
        ])
        self.SetSizer(gs)

    @property
    def previous_panel(self):
        return self._previous_panel

    @property
    def next_panel(self):
        return self._next_panel

    @next_panel.setter
    def next_panel(self, value):
        self._next_panel = value

    def set_active(self):
        self.SetBackgroundColour('#FFFF8A')

    def set_not_active(self):
        self.SetBackgroundColour(None)
