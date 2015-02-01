# -*- coding: utf-8 -*-
#
# GoWest Jukebox player
# Main GUI Frame
# @author: www.niwi.cz

import wx

from settings_dialog import SettingsDialog
from collection_panel import CollectionPanel
from queue_panel import QueuePanel


APP_NAME = "GoWest Jukebox"

APP_SETTINGS = 1
APP_EXIT = 2


class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        """
        Init GUI
        :param args:
        :param kwargs:
        :return: None
        """
        super(MainFrame, self).__init__(None)

        self._collection_panel = None

        self.init_ui()

    def init_ui(self):
        """
        Initializes the window GUI.
        :return:
        """
        menu_bar = wx.MenuBar()
        app_menu = wx.Menu()

        # menu items
        settings_item = wx.MenuItem(app_menu, APP_SETTINGS, '&Settings\tCtrl+S')
        settings_item.SetBitmap(wx.Bitmap('cog.png'))
        app_menu.AppendItem(settings_item)

        quit_item = app_menu.Append(APP_EXIT, 'Quit', 'Quit')
        quit_item.SetBitmap(wx.Bitmap('door_out.png'))

        menu_bar.Append(app_menu, '&Application')
        self.SetMenuBar(menu_bar)

        # menu actions
        self.Bind(wx.EVT_MENU, self.display_settings_action, id=APP_SETTINGS)
        self.Bind(wx.EVT_MENU, self.quit_action, id=APP_EXIT)

        # collection action
        self.Bind(wx.EVT_CHAR_HOOK, self.onKey)

        self._queue_panel = QueuePanel(self)
        self.refresh_components()

        #self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL) #TODO show fullscreen
        self.SetTitle(APP_NAME)
        self.Centre()
        self.Show(True)

    def onKey(self, evt):
        if not self._collection_panel:
            return

        if evt.GetKeyCode() == wx.WXK_UP:
            self._collection_panel.previous_action()
        elif evt.GetKeyCode() == wx.WXK_DOWN:
            self._collection_panel.next_action()
        elif evt.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_SPACE):
            self._queue_panel.enqueue(self._collection_panel.get_current_song())
        else:
            evt.Skip()

    def display_settings_action(self, e):
        """
        Action handler for displaying the settings dialog.
        :param e:
        :return: None
        """
        dialog = SettingsDialog(None)
        dialog.set_refresh_callback(self.refresh_components)
        dialog.ShowModal()
        dialog.Destroy()

    def refresh_components(self):
        old_sizer = self.GetSizer()
        if old_sizer:
            del old_sizer

        # main layout
        self._collection_panel = CollectionPanel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self._queue_panel, 2, wx.EXPAND | wx.ALL, 2)
        hbox.Add(self._collection_panel, 3, wx.EXPAND | wx.ALL, 2)
        self.SetSizer(hbox)
        self.Layout()   # redraw layout

    def quit_action(self, e):
        """
        Action handler for exiting the application.
        :param e:
        :return: None
        """
        self.Close()