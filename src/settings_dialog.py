# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# App settings dialog
# @author: www.niwi.cz

import wx

from app import App
from collection_controller import CollectionController, CollectionError


class SettingsDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        """
        Inits the dialog.
        :param args:
        :param kw:
        :return: None
        """
        super(SettingsDialog, self).__init__(*args, **kw)

        self.directory_textfield = None
        self.refresh_callback = None

        self.init_ui()
        #self.SetSize((250, 200))
        self.SetTitle("Jukebox settings")


    def init_ui(self):
        """
        Initializes the dialog GUI.
        :return: None
        """
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='Music source')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # label
        hbox1.Add(wx.StaticText(pnl, label='Music collection directory'))
        # input field
        self.directory_textfield = wx.TextCtrl(pnl, value=App.get_songs_dir(), size=(150, 35))
        self.directory_textfield.Bind(wx.EVT_LEFT_UP, self.select_dir_dialog)
        hbox1.Add(self.directory_textfield, flag=wx.LEFT, border=5)
        # scan button
        scan_button = wx.Button(pnl, label="Scan")
        scan_button.Bind(wx.EVT_BUTTON, self.start_scanning)
        hbox1.Add(scan_button, flag=wx.LEFT)
        # add panel and sizers
        sbs.Add(hbox1)
        pnl.SetSizer(sbs)

        # bottom dialog buttons
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(self, label='Ok')
        ok_button.Bind(wx.EVT_BUTTON, self.close_action)
        hbox2.Add(ok_button)
        close_button = wx.Button(self, label='Close')
        close_button.Bind(wx.EVT_BUTTON, self.close_action)
        hbox2.Add(close_button, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)


    def select_dir_dialog(self, e):
        """
        Displays the system dialog for selecting the directory to scan.
        :param e: Event object
        :return:
        """
        dialog = wx.DirDialog(None, "Please choose your project directory:", style=1,
                              defaultPath=self.directory_textfield.GetValue(), pos = (10,10))
        # change the dir if dialog succeeded
        if dialog.ShowModal() == wx.ID_OK:
            new_songs_dir = dialog.GetPath()
            self.directory_textfield.SetValue(new_songs_dir)
            App.set_songs_dir(new_songs_dir)

    def start_scanning(self, e):
        """
        Scans the collection in the directory set in dialog textfield.
        :param e: Event object
        :return:
        """
        collection_ctrl = CollectionController()
        try:
            collection_ctrl.scan()
        except CollectionError, e:
            dial = wx.MessageDialog(None, 'Error while scanning song files: %s' % e, 'Error while scanning', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
            return
        if self.refresh_callback:
            self.refresh_callback()
        dial = wx.MessageDialog(None, '%s song files were successfully loaded.' % collection_ctrl.get_songs_count(), 'Scanning completed', wx.OK)
        dial.ShowModal()

    def set_refresh_callback(self, refresh_callback):
        """
        Sets the callback which will be called after re-scanning the collection.
        :param refresh_callback:
        :return:
        """
        self.refresh_callback = refresh_callback

    def close_action(self, e):
        """
        Action handler for closing the settings dialog.
        :param e: Event object
        :return:
        """
        self.Destroy()