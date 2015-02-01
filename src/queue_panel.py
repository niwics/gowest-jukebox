# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Sizer containing information about one single song from the collection.
# @author: www.niwi.cz

from pygame import mixer

import wx
from wx.lib.scrolledpanel import ScrolledPanel


class QueuePanel(ScrolledPanel):

    def __init__(self, parent):
        """
        Init GUI
        :return: None
        """
        super(QueuePanel, self).__init__(parent)

        self.SetupScrolling()

        self._vsizer = wx.BoxSizer(wx.VERTICAL)

        # fonts for labels
        empty_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        empty_font.SetWeight(wx.BOLD)
        empty_font.SetPointSize(empty_font.GetPointSize()+2)
        empty_label = wx.StaticText(self, label="Press enter or space \nto play the selected song!", style=wx.ALIGN_CENTER)
        empty_label.SetFont(empty_font)
        self._vsizer.Add(empty_label, flag=wx.EXPAND|wx.ALL, border=4)

        self.SetSizer(self._vsizer)

    def enqueue(self, song):
        self._vsizer.Clear(True)

        title_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        title_font.SetWeight(wx.BOLD)
        title_font.SetPointSize(title_font.GetPointSize()+2)
        title_label = wx.StaticText(self, label=song.title)
        title_label.SetFont(title_font)
        self._vsizer.Add(title_label, flag=wx.EXPAND|wx.ALL, border=4)

        others_font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        others_font.SetPointSize(others_font.GetPointSize()+1)

        artist_label = wx.StaticText(self, label=song.artist)
        artist_label.SetFont(others_font)
        self._vsizer.Add(artist_label, flag=wx.EXPAND|wx.ALL, border=4)

        album_label = wx.StaticText(self, label=song.album)
        album_label.SetFont(others_font)
        self._vsizer.Add(album_label, flag=wx.EXPAND|wx.ALL, border=4)

        year_label = wx.StaticText(self, label=song.year)
        year_label.SetFont(others_font)
        self._vsizer.Add(year_label, flag=wx.EXPAND|wx.ALL, border=4)

        self.play(song)

        self.Layout()   # redraw

    def play(self, song):
        try:
            mixer.init()
            mixer.music.load(song.filename)
            mixer.music.play()
        except KeyError, e:
            dial = wx.MessageDialog(None, 'Error while playing song file %s: %s' % (song.filename, e), 'Error while playing', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()