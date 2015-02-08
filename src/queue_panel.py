# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Sizer containing information about one single song from the collection.
# @author: www.niwi.cz

from pygame import mixer

import wx
from wx.lib.scrolledpanel import ScrolledPanel
from wx.lib.wordwrap import wordwrap

from collection_controller import CollectionController
from queue_song_panel import QueueSongPanel


class QueuePanel(ScrolledPanel):

    EMPTY_TEXT = "Press enter or space to play the selected song.\nUse arrow keys to move in your music collection."
    NO_SONGS_TEXT = "Import your music via Application > Settings menu"

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
        self.empty_label = wx.StaticText(self, label=self._get_basic_label_text(), style=wx.ALIGN_CENTER)
        self.empty_label.SetFont(empty_font)
        self._vsizer.Add(self.empty_label, flag=wx.EXPAND|wx.ALL, border=4)

        self.SetSizer(self._vsizer)

        self.Bind(wx.EVT_SIZE, self._on_size)


    def enqueue(self, song):
        """
        Enwueue the selected song - actualize the queue panel and play it.
        :param song:
        :return:
        """
        self._vsizer.Clear(True)
        self.empty_label = None

        self._vsizer.Add(QueueSongPanel(self, song), flag=wx.EXPAND|wx.ALL, border=4)

        self._play(song)

        self.Layout()   # redraw

    def _play(self, song):
        """
        Play the given song.
        :param song:
        :return:
        """
        try:
            file = open(song.filename, 'rb')
            mixer.init()
            mixer.music.load(file)  # cannot pass the song.filename directly because of possible UnicodeDecodeError
            mixer.music.play()
        except Exception, e:
            dial = wx.MessageDialog(None, 'Error while playing song file %s: %s' % (song.filename, e), 'Error while playing', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()

    def _on_size(self, event):
        """
        Resize the empty label text - wrap into lines.
        :param event:
        :return:
        """
        if self.empty_label:
            width = event.GetSize()[0]
            wrapped_text = wordwrap(self._get_basic_label_text(), width, wx.ClientDC(self.empty_label))
            self.empty_label.SetLabel(wrapped_text)

    def _get_basic_label_text(self):
        collection_ctr = CollectionController()
        return self.NO_SONGS_TEXT if collection_ctr.get_songs_count() == 0 else self.EMPTY_TEXT