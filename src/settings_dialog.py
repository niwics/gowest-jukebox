# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# App settings dialog
# @author: www.niwi.cz

import wx


class SettingsDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        """
        Inits the dialog.
        :param args:
        :param kw:
        :return: None
        """
        super(SettingsDialog, self).__init__(*args, **kw)

        self.init_ui()
        #self.SetSize((250, 200))
        self.SetTitle("Jukebox settings")


    def init_ui(self):
        """
        Initializes the dialog GUI.
        :return: None
        """
        pass


    def close_action(self, e):
        """
        Action handler for closing the dialog.
        :param e:
        :return:
        """
        self.Destroy()