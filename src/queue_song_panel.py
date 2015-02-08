# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Sizer containing information about one single song from the collection.
# @author: www.niwi.cz

import wx


class QueueSongPanel(wx.Panel):

    FIRST_SONG_BG_COLOR = '#8888AA'

    def __init__(self, parent_panel, song):
        """
        Init GUI
        :return: None
        """
        super(QueueSongPanel, self).__init__(parent_panel)
        self._song = song

        main_hsizer = wx.BoxSizer(wx.HORIZONTAL)

        # album image
        img = wx.Image("../music-notes.png", wx.BITMAP_TYPE_ANY)
        img = img.Scale(100, 100)
        image_ctrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img))
        main_hsizer.Add(image_ctrl, 0, wx.ALL, 10)

        # song info panel
        info_panel = wx.Panel(self)
        info_vsizer = wx.BoxSizer(wx.VERTICAL)

        title_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        title_font.SetWeight(wx.BOLD)
        title_font.SetPointSize(title_font.GetPointSize()+2)
        title_label = wx.StaticText(info_panel, label=song.title)
        title_label.SetFont(title_font)
        info_vsizer.Add(title_label, flag=wx.EXPAND|wx.ALL, border=4)

        others_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        others_font.SetPointSize(others_font.GetPointSize()+1)

        artist_label = wx.StaticText(info_panel, label=song.artist)
        artist_label.SetFont(others_font)
        info_vsizer.Add(artist_label, flag=wx.EXPAND|wx.ALL, border=4)

        album_label = wx.StaticText(info_panel, label=song.album)
        album_label.SetFont(others_font)
        info_vsizer.Add(album_label, flag=wx.EXPAND|wx.ALL, border=4)

        year_label = wx.StaticText(info_panel, label=song.year)
        year_label.SetFont(others_font)
        info_vsizer.Add(year_label, flag=wx.EXPAND|wx.ALL, border=4)

        info_panel.SetBackgroundColour(self.FIRST_SONG_BG_COLOR)
        info_panel.SetSizer(info_vsizer)
        main_hsizer.Add(info_panel, flag=wx.EXPAND|wx.ALL, border=4)

        self.SetBackgroundColour(self.FIRST_SONG_BG_COLOR)
        self.SetSizer(main_hsizer)

    @property
    def previous_panel(self):
        return self._previous_panel

    @property
    def next_panel(self):
        return self._next_panel

    @next_panel.setter
    def next_panel(self, value):
        self._next_panel = value

    @property
    def song(self):
        return self._song

    def set_active(self):
        self.SetBackgroundColour('#FFFF8A')

    def set_not_active(self):
        self.SetBackgroundColour(None)
